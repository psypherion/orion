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
from orion import Orion

app = Orion()


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
<template>
    <footer
        style="
        left: 0;
        bottom: 0;
        width: 100%;
        padding: 10px;
        background-color: rgba(255,255,255,0.18);
        position: fixed;
        display: flex;
        justify-content: center;
        align-items: center;"
    >
        <p
        style="
        text-align: center;
        margin: 0;
        color: #ccc;
        background-color: transparent"
        >© 2025 Orion</p>
    </footer>
</template>

<script>
    document.querySelector('footer').addEventListener('click', () => {
        alert('You clicked the footer!');
    });
</script>
```
### Path: components/counter.html
```html
<style>
    #count {
        font-size: 20px;
    }
    .counter_button {
        padding: 10px 20px;
        border-radius: 10px;
        outline: none;
        border: none;
        cursor: pointer;
        background-color: #007bff;
        color: white;
    }
    #count {
        font-size: 20px;
        text-align: center;
    }
</style>

<template>
    <div style="min-width: 500px; display: flex; align-items: center; justify-content: space-between; padding: 10px 0">
        <button id="decrement" class="counter_button">-</button>
        <span id="count">0</span>
        <button id="increment" class="counter_button">+</button>
    </div>
</template>

<script>
  let count = 0;
    const countEl = document.querySelector('#count');
    document.querySelector('#decrement').addEventListener('click', () => {
      if (count === 0) return;
        count--;
        countEl.textContent = String(count);
    });
    document.querySelector('#increment').addEventListener('click', () => {
        count++;
        countEl.textContent = String(count);
    });
</script>
```
### Path: components/file_uploader.html
```html
<style>
    #file {
        display: none;
    }
    #upload {
        display: block;
        margin: 10px auto;
    }
    #pseudo-input {
        min-width: 500px;
        min-height: 300px;
        border: 2px dashed rgba(255, 255, 255, 0.07);
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
    }
    #filename {
        margin: 0;
        text-align: center;
        background-color: transparent;
    }
    .action_button {
        width: 200px;
        padding: 10px 20px;
        margin: 10px;
        border-radius: 10px;
        outline: none;
        border: none;
        cursor: pointer;
        background-color: #007bff;
        color: white;
    }
    #clear {
        background-color: #dc3545;
    }
    #message {
        visibility: hidden;
        padding: 10px;
        background-color: transparent;
    }

</style>


<template>
    <input type="file" id="file" name="file" />
    <div id="pseudo-input">
        <p id="filename">No file chosen</p>
    </div>
    <div style="display: flex">
        <button id="upload" class="action_button">Upload</button>
        <button id="clear" class="action_button">Clear</button>
    </div>
</template>

<script>
    const hiddenInput = document.querySelector('#file');
    const pseudoInput = document.querySelector('#pseudo-input');
    pseudoInput.addEventListener('click', () => {
        hiddenInput.click();
    });
    hiddenInput.addEventListener('change', () => {
        document.querySelector('#filename').textContent = hiddenInput.files[0].name;
    });
    document.querySelector('#clear').addEventListener('click', (ev) => {
        ev.stopPropagation();
        hiddenInput.value = '';
        document.querySelector('#filename').textContent = 'No file chosen';
        pseudoInput.style.borderColor = 'rgba(255, 255, 255, 0.07)';
    });
    document.querySelector('#upload').addEventListener('click', async () => {
        if (!hiddenInput.files.length) {
            alert('No file chosen');
            return;
        }
        const formData = new FormData();
        formData.append('file', hiddenInput.files[0]);
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        if (response.ok) {
            pseudoInput.style.borderColor = 'rgba(40,167,69,0.56)';
        } else {
            pseudoInput.style.borderColor = 'rgba(220,53,69,0.87)';
        }
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
    <{./components/counter}>
    <{./components/file_uploader}>
    <{./components/footer}>
    <script></script>
</body>
</html>
```
## Screenshots
![image](/assets/screenshot.png)