# Step 1

### Research Parcel
Parcel is a popular bundler that provides a simple and efficient way to bundle JavaScript files. It's a great choice for small to medium-sized projects.

### Basic Usage and API Integration
You can find tutorials online that cover the basics of Parcel and how to integrate it with APIs. Here's a brief overview:

* Initialize the project `npm init -y`

# Step 2

### Install Parcel -Integrate
* Install Parcel as a development dependency using npm: `npm install -D parcel`

# Step 3 
### Create Basic Files
Create the following files in your project directory:

* `index.html`: the main HTML file for your prototype
* `styles.css`: the CSS file for styling your prototype
* `index.js`: the JavaScript file for interacting with the API and updating the HTML

### Project Structure
Your project structure should look like this:

#### project/ index.html styles.css index.js

# Step 4
#### Update index.html
Update your index.html file to include a container for the product data:

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Saori Clone Store Prototype</title>
  <link type="text/css" rel="stylesheet" href="styles.css">
</head>
<body>
<!--  Instead of this <div id="products"></div>
  <script src="script.js"></script> -->
    <main class="Main">
    <include src="partials/header.html"></include>
    <div id="app"></div>
  </main>
</body>
</html>
```

# Step 5
Estilizar la Single Page

[Rock-Explorer styles.css](https://github.com/saorionline/rock-explorer/blob/main/src/styles.css)


# Step 6
* Estructurar la lógica de la API
[Rock Explorer index.js](https://github.com/saorionline/rock-explorer/blob/main/src/index.js)

* Revisar en Inspect > Network que sea un array

# Step 7
Añadir los script para el entorno local
[Rock Explorer package.json](https://github.com/saorionline/rock-explorer/blob/main/package.json)

# Step 8

Now that I've added new changes and resources I need to see if it works with 

`npm run build`

`npm run start`

# Step 9
**To finish the process with the installation of Git Hub Pages**

`npm install gh -pages -D`

***After updates and testing***

`npm run deploy`