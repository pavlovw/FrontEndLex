document.addEventListener("DOMContentLoaded", () => {
    const updateForm = document.getElementById('update-form');
    
    updateForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const email = document.getElementById('email').value;
        const address = document.getElementById('address').value;

        // Aquí puedes agregar la lógica para actualizar la información
        console.log('Información actualizada:', { email, address });

        alert('Información actualizada correctamente.');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Mostrar la sección por defecto (Dashboard) al cargar la página
    document.getElementById("tu-cuenta").style.display = "block";
    document.getElementById("dashboard").style.display = "none";
    document.getElementById("mis-causas").style.display = "none";
    document.getElementById("contratos-documentos").style.display = "none";

    // Obtener todos los enlaces del navbar-left
    var links = document.querySelectorAll(".navbar-left ul li a, .menu-overlay ul li a");

    // Agregar evento de clic a cada enlace
    links.forEach(function(link) {
        link.addEventListener("click", function(event) {
            // Obtener el id de la sección correspondiente al enlace
            var sectionId = link.getAttribute("href").substring(1);

            // Ocultar todas las secciones
            document.querySelectorAll(".section").forEach(function(section) {
                section.style.display = "none";
            });

            // Mostrar la sección correspondiente al enlace seleccionado
            document.getElementById(sectionId).style.display = "block";

            // Remover la clase 'selected' de todos los enlaces
            links.forEach(function(link) {
                link.classList.remove("selected");
            });

            // Agregar la clase 'selected' al enlace seleccionado
            link.classList.add("selected");

            // Evitar el comportamiento por defecto del enlace
            event.preventDefault();
        });
    });
});




