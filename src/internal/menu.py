from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn
import json

with open('src/internal/data/menu.json') as f:
    menu_data = json.load(f)

# Route to serve the menu data
async def menu_endpoint(request):
    return JSONResponse(menu_data)

# Route to get food item by food_id
async def food_detail_endpoint(request):
    food_id = request.path_params.get("food_id")
    food_item = menu_data["menu"].get(food_id)
    if food_item:
        return JSONResponse(food_item)
    return JSONResponse({"error": "Food item not found"}, status_code=404)

# Application setup
app = Starlette(debug=True, routes=[
    Route("/menu", menu_endpoint),
    Route("/menu/{food_id}", food_detail_endpoint)
])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
