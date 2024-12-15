let currentIndex = 1;
const items = document.querySelectorAll('.carousel-item');
const totalItems = items.length;
const intervalTime = 10000; 
let slideInterval;


document.querySelector('.carousel-inner').style.animation = 'none';


function updateSlide() {
    document.querySelector('.carousel-inner').style.transform = `translateX(-${currentIndex * 100}%)`;
}

function moveSlide(direction) {
    currentIndex = (currentIndex + direction + totalItems) % totalItems;
    updateSlide();
}

function nextSlide() {
    moveSlide(1);
}

function startSlideInterval() {
    slideInterval = setInterval( intervalTime);
}

function stopSlideInterval() {
    clearInterval(slideInterval); 
    setTimeout(() => {
        startSlideInterval(); 
    }, 5000); // si no se mueve el carrusel(por el usuario) en 5 segundos vuelve a moverse solo cada 7 segundos
}
document.querySelector('.prev').addEventListener('click', () => { moveSlide(1);stopSlideInterval();});
document.querySelector('.next').addEventListener('click', () => {moveSlide(-1);stopSlideInterval();});

startSlideInterval();
