// Detectar el evento de scroll
window.addEventListener('scroll', function() {
    // Obtener la posición actual de desplazamiento
    var scrollPosition = window.scrollY;

    // Obtener el navbar
    var navbar = document.getElementById('navbar');

    // Si la posición de desplazamiento es mayor que 0, agregar la clase 'scrolled', sino, quitarla
    if (scrollPosition > 0) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});


document.addEventListener('DOMContentLoaded', function () {
    const btnMenu = document.getElementById('btn-menu');
    const menuOverlay = document.getElementById('menu-overlay');
    const menuIcon = btnMenu.querySelector('.menu-icon');
    const closeIcon = document.createElement('span');
    const navbar = document.getElementById('navbar');

    closeIcon.innerHTML = '&times;';
    closeIcon.classList.add('close-icon');

    btnMenu.appendChild(closeIcon);

    btnMenu.addEventListener('click', function () {
        if (menuOverlay.classList.contains('open')) {
            menuOverlay.classList.remove('open');
            menuIcon.style.display = 'block';
            closeIcon.style.display = 'none';
            navbar.style.backgroundColor = '';
            navbar.style.transition = 'none';
        } else {
            menuOverlay.classList.add('open');
            menuIcon.style.display = 'none';
            closeIcon.style.display = 'block';
            navbar.style.backgroundColor = '#2D2F36';
            navbar.style.transition = 'none';
        }
    });

    menuOverlay.addEventListener('click', function (e) {
        if (e.target === menuOverlay) {
            menuOverlay.classList.remove('open');
            menuIcon.style.display = 'block';
            closeIcon.style.display = 'none';
        }
    });
});




