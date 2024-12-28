# Orion 

#### Your web framework redefined.

Orion is a web framework that is designed to be simple, fast, and easy to use. It is built on top of the [Starlette](https://www.starlette.io/) ASGI framework and is designed to be a drop-in replacement for it. Orion is designed to be simple and easy to use, with a focus on performance and ease of use.

## Features
- Simple and easy to use
- Fast and lightweight
- Built on top of Starlette
- Automatic static routing
- Less boilerplate code
- Easy to extend and customize
- Built-in database support (SQLite3)
- Built-in JWT support (Coming soon)
- Built-in OAuth support (Coming soon)

## Installation
To install Orion, you can use pip:

```bash
pip install git+https://github.com/jnsougata/orion.git
```

## Quickstart
Here is a simple example of how to create a simple web application using Orion:

```python
from orion.client import Client

app = Client()


@app.on_startup()
async def startup():
    print("Starting up...")

@app.on_shutdown()
async def shutdown():
    print("Shutting down...")

if __name__ == '__main__':
    app.run()
```