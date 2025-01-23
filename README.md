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
## Basic File Structure
```
.
├── main.py
├── views/
│   ├── index.html
│   ├── users/{user_id}.html
│   └── users/{user_id}/guilds/{guild_id}.html
├── public/
│   ├── style.css
│   └── script.js
└── components/
    ├── navbar.html
    └── footer.html
```
## Creating Component
#### Path: components/footer.html
```html
<style>
    footer{
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        position: fixed;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    footer p {
        text-align: center;
        margin: 0;
        color: black;
    }
</style>

<template>
    <footer>
        <p>© 2025 Orion</p>
    </footer>
</template>

<script>
</script>
```
## Importing Component
#### Path: views/index.html
```html
<!--<cfg>method: GET, use_auth: false, database_scope: readonly</cfg>-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Orion</title>
    <link rel="stylesheet" href="/public/style.css">
    <style></style>
</head>
<body>
    <p>The route is: {{view.route}}</p>
    <{./components/footer}>
    <script></script>
</body>
</html>
```