import os
import re
import uvicorn
import jinja2
from  starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.requests import Request

from typing import Dict, Any, Optional, List
from .enums import UseAuthBool, DBScope


class _View:
    def __init__(
        self,
        *,
        file_path: str,
        route: str,
        use_auth: UseAuthBool = UseAuthBool.FALSE,
        db_scope: DBScope = DBScope.READONLY,
        method: Optional[str] = None
    ):
        self.file_path = file_path
        self.route = route
        self.use_auth = use_auth
        self.db_scope = db_scope
        self.methods = method or "GET"

class Client(Starlette):
    def __init__(
        self,
        views_dir: str = 'views',
        public_dir: str = 'public',
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.views_dir = views_dir
        self.public_dir = public_dir
        self.__jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self.views_dir)
        )
        self._view_map: Dict[str, _View] = {}
        self._attach_views()
        self.mount('/public', StaticFiles(directory=self.public_dir), name='public')

    @staticmethod
    def __build_matched_raw_route(request: Request):
        params = request.path_params
        path = request.url.path
        for key, value in params.items():
            path = path.replace(value, f"{{{key}}}")
        return path

    @staticmethod
    def __parse_config(html: str) -> Dict[str, Any]:
        pattern = r"<!--<cfg>(.*?)</cfg>-->"
        conf = {}
        matched = re.search(pattern, html, re.DOTALL)
        if not matched:
            return conf
        conf_str = matched.group(1)
        for pair in conf_str.split(','):
            key, value = pair.split(':')
            conf[key.strip()] = value.strip()
        return conf


    async def _handler(self, request: Request, *args, **kwargs):
        view = self._view_map[self.__build_matched_raw_route(request)]
        template = self.__jinja_env.get_template(view.file_path)
        return HTMLResponse(template.render(request=request, view=view, *args, **kwargs))

    def _attach_views(self):
        for root, dirs, files in os.walk(self.views_dir):
            for file in files:
                if file.endswith('.html'):
                    path = os.path.join(root, file)
                    with open(path, 'r') as f:
                        route = f"{path}"[:-5].replace(self.views_dir, '')
                        if route == '/index':
                            route = '/'
                        config = self.__parse_config(f.read())
                        view = _View(
                            file_path=path.replace(self.views_dir, '')[1:],
                            route=route,
                            use_auth=UseAuthBool(config.get('use_auth', 'false')),
                            db_scope=DBScope(int(config.get('db_scope', '1'))),
                            method=config.get('method')
                        )
                        self._view_map[route] = view
                        self.add_route(route, self._handler)




    def run(
        self,
        host: str='localhost',
        port: int=8000,
        *args,
        **kwargs
    ):
        uvicorn.run(self, host=host, port=port, *args, **kwargs)