# Deprecated Config
* Create a `parcel.config.js` file to configure Parcel
* Use the `parcel` command to bundle your JavaScript files
  
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


##### Deprecated Fetch Data from the Platzi Fake Store API**

### Use the `fetch` API
Use the `fetch` API to make a GET request to the Platzi Fake Store API:

##### Deprecated Display Data in Your Prototype**

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

# Step 4

### Fetch Data from Platzi Fake Store API

# Option1

Open `script.js` and add this

```javascript
// script.js
const BASE_URL = 'https://fakeapi.platzi.com/api/products';

async function fetchProducts() {
    try {
        const response = await fetch(BASE_URL);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching products:', error)
    }
}

// Call the fetchProducts function and handle the data
fetchProducts().then(products => {
  // Use the products data to display them in your prototype
  displayProducts(products);
});

function displayProducts(products) {
  // This function will iterate through the products array and
  // create HTML elements to display product information.
  // Update the following logic to display images, names, and prices.
  const productList = document.getElementById('product-list');
  for (const product of products) {
    const productItem = document.createElement('li');
    productItem.textContent = product.name;
    productList.appendChild(productItem);
  }
}
```
# Option2 
### Use the `fetch` API
Use the `fetch` API to make a GET request to the Platzi Fake Store API:

```javascript
// script.js
fetch('https://platzi-fake-store-api.herokuapp.com/products')
  .then(response => response.json())
  .then(data => {
    // Use the retrieved data to populate your HTML
  })
  .catch(error => console.error(error));
  ```

### Use Axios (Optional)
Alternatively, you can use Axios to make the API request:  
```javascript
// script.js
import axios from 'axios';

axios.get('https://platzi-fake-store-api.herokuapp.com/products')
  .then(response => {
    // Use the retrieved data to populate your HTML
  })
  .catch(error => console.error(error));
   ```

