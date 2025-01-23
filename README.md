# Orion 

#### Your web framework redefined.

Orion is a lightweight, high-performance, and modular web framework built on the Starlette ASGI framework. It is designed to be simple, fast, and user-friendly, with a strong focus on performance, ease of use, and modularity. Orion provides developers with the flexibility to extend and customize its functionality, making it an excellent choice for building modern and scalable web applications.

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
> ⚠️ Currently the CSS and JS is globally scoped. 
So there is a chance of namespace collision for both CSS and JS.
To avoid this, one can use inline CSS or stick to a naming convention for CSS and JS.
In the future, it will be scoped to the component.
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
    document.querySelector('footer').addEventListener('click', () => {
        alert('Footer clicked');
    });
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