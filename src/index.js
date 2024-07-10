const $app = document.getElementById("app");
const imagesBook = [
  {
    title: "Genética de la Salud",
    year: 2024,
    src: "https://images.pexels.com/photos/6988530/pexels-photo-6988530.jpeg?auto=compress&cs=tinysrgb&w=600",
    alt: "Herramientas para mejorar la salud"
  },
  {
    title: "Conocimiento de la Salud",
    year: 2024,
    src: "https://images.pexels.com/photos/6988707/pexels-photo-6988707.jpeg?auto=compress&cs=tinysrgb&w=600",
    alt: "Reducción de enfermedades"
  },
  {
    title: "Bienestar Interno",
    year: 2024,
    src: "https://images.pexels.com/photos/3952247/pexels-photo-3952247.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load",
    alt: "Opciones para tomar decisiones"

  },
];

let currentImageIndex = 0; // Keeps track of the current image

const displayImage = (index) => {
  $app.innerHTML = ""; // Clear previous content
  const image = imagesBook[index];
  const newItem = document.createElement("section");
  newItem.classList.add("Items");
  newItem.innerHTML = `
    <article class="Card">
      <img src="${image.src}">
      <h2>
        ${image.title} 
      </h2>
      <h3><small>${image.alt}</small></h3>
    </article>
  `;
  $app.appendChild(newItem);
  currentImageIndex = index;
};

// Display the first image by default
displayImage(currentImageIndex);

// Add buttons or functionality to call next/previous images
// (This part is not included in the code snippet, but you can add buttons 
// with click events that call displayImage with the desired index)
