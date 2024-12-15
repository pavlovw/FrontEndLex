

//=====================BOTON DE MENU==================
// Asegura que el script se ejecute después de que el DOM esté listo

$(document).ready(function() {
    // Evento para mostrar el menú desplegable cuando se hace clic en el botón
    $('#btn-menu').on('click', function() {
        $('.menu-overlay').fadeIn(); // Mostrar el menú con una transición
    });

    // Evento para cerrar el menú cuando se hace clic en la "X"
    $('.close-menu').on('click', function() {
        $('.menu-overlay').fadeOut(); // Ocultar el menú con una transición
    });
});


//=====================CARRUSEL =================================

document.addEventListener("DOMContentLoaded", () => {
    const carouselWrapper = document.querySelector(".carousel-wrapper");
    const slides = document.querySelectorAll(".carousel-item");
    const totalSlides = slides.length; // Número total de diapositivas
    let currentSlide = 0; // Índice de la diapositiva actual

    function updateSlide() {
        const offset = -100 * currentSlide; // Desplazamiento para el carrusel
        carouselWrapper.style.transform = `translateX(${offset}%)`; // Desplaza el carrusel
    }

    // Navegación a la diapositiva anterior
    document.querySelector(".carousel-control-prev").addEventListener("click", () => {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides; // Cambia a la diapositiva anterior
        updateSlide(); // Actualiza el carrusel
    });

    // Navegación a la siguiente diapositiva
    document.querySelector(".carousel-control-next").addEventListener("click", () => {
        currentSlide = (currentSlide + 1) % totalSlides; // Cambia a la siguiente diapositiva
        updateSlide(); // Actualiza el carrusel
    });
});

//==================CONTADOR CARRITO======================
document.addEventListener("DOMContentLoaded", function() {
    const cartCounter = document.querySelector(".content-shopping-cart .number");
    let itemCount = 0;

    // Función para actualizar el contador del carrito
    function updateCartCounter() {
        cartCounter.textContent = `(${itemCount})`;
    }

    // Función para agregar un producto al carrito
    function addToCart() {
        itemCount++; // Incrementar el contador
        updateCartCounter(); // Actualizar el contador del carrito
    }

    // Evento click para agregar producto al hacer clic en el botón "Agregar al carrito"
    document.querySelectorAll(".btn-primary").forEach(button => {
        button.addEventListener("click", addToCart);
    });
});


function iniciarMap(){
    var coord = {lat:-33.4330059 ,lng: -70.6149044};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 15,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}






