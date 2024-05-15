# Step 1

### Research Parcel
Parcel is a popular bundler that provides a simple and efficient way to bundle JavaScript files. It's a great choice for small to medium-sized projects.

### Basic Usage and API Integration
You can find tutorials online that cover the basics of Parcel and how to integrate it with APIs. Here's a brief overview:

* Initialize the project `npm init -y`
* Install Parcel using npm or yarn: `npm install parcel` or `yarn add parcel`
* Create a `parcel.config.js` file to configure Parcel
* Use the `parcel` command to bundle your JavaScript files
  
# Step 2  

### Create Basic Files
Create the following files in your project directory:

* `index.html`: the main HTML file for your prototype
* `styles.css`: the CSS file for styling your prototype
* `script.js`: the JavaScript file for interacting with the API and updating the HTML

### Project Structure
Your project structure should look like this:

#### project/ index.html styles.css script.js parcel.config.js

# Step 3

### Install Parcel -Integrate
Install Parcel as a development dependency using `npm install -D parcel` for Development setting up environment  or `npm install parcel`

### Create a `parcel.config.js` File
Create a `parcel.config.js` file with the following configuration:
```javascript
module.exports = {
  // Enable sourcemaps for debugging
  sourcemaps: true,
  // Output bundled files to a `dist` directory
  outDir: './dist',
};
```
#### Update script.js to Use Parcel
Update your script.js file to use Parcel:
```javascript
// script.js
import './styles.css';

// Your JavaScript code here
```

#### Run Parcel
Run Parcel using the parcel command: npx parcel script.js

This will bundle your JavaScript files and output them to a dist directory.


# Step 4: Fetch Data from the Platzi Fake Store API**

### Use the `fetch` API
Use the `fetch` API to make a GET request to the Platzi Fake Store API:

# Step 5: Display Data in Your Prototype**

### Populate HTML with Product Data
Use the retrieved data to populate your HTML with product information:

```javascript
// script.js
fetch('https://platzi-fake-store-api.herokuapp.com/products')
  .then(response => response.json())
  .then(data => {
    const productsContainer = document.getElementById('products');

    data.forEach(product => {
      const productHTML = `
        <div>
          <img src="${product.image}" alt="${product.name}">
          <h2>${product.name}</h2>
          <p>Price: ${product.price}</p>
        </div>
      `;

      productsContainer.innerHTML += productHTML;
    });
  })
  .catch(error => console.error(error));   
  ```

# Update index.html
Update your index.html file to include a container for the product data:
```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Platzi Fake Store Prototype</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="products"></div>
  <script src="script.js"></script>
</body>
</html>
```