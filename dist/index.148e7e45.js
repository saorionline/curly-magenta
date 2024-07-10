const e=document.getElementById("app"),t=[{title:"Genética de la Salud",year:2024,src:"https://images.pexels.com/photos/6988530/pexels-photo-6988530.jpeg?auto=compress&cs=tinysrgb&w=600",alt:"Herramientas para mejorar la salud"},{title:"Conocimiento de la Salud",year:2024,src:"https://images.pexels.com/photos/6988707/pexels-photo-6988707.jpeg?auto=compress&cs=tinysrgb&w=600",alt:"Reducción de enfermedades"},{title:"Bienestar Interno",year:2024,src:"https://images.pexels.com/photos/3952247/pexels-photo-3952247.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load",alt:"Opciones para tomar decisiones"}];let s=0;(s=>{e.innerHTML="";let a=t[0],l=document.createElement("section");l.classList.add("Items"),l.innerHTML=`
    <article class="Card">
      <img src="${a.src}">
      <h2>
        ${a.title} <small>Precio $ ${a.alt}</small>
      </h2>
    </article>
  `,e.appendChild(l)})(0);
//# sourceMappingURL=index.148e7e45.js.map
