document.addEventListener("DOMContentLoaded", () => {
    // Inicializar la actualización de información de la cuenta
    const infoForms = document.querySelectorAll('.card form');
    
    infoForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const inputs = form.querySelectorAll('input');
            let infoData = {};
            inputs.forEach(input => {
                infoData[input.name] = input.value;
            });

            // Aquí puedes agregar la lógica para actualizar la información
            console.log('Información actualizada:', infoData);

            alert('Información actualizada correctamente.');
        });
    });

    // Mostrar la sección por defecto (Dashboard) al cargar la página
    document.getElementById("tu-cuenta").style.display = "block";
    document.getElementById("dashboard").style.display = "none";
    document.getElementById("gestionar-usuarios").style.display = "none";
    document.getElementById("gestionar-causas").style.display = "none";
    document.getElementById("gestionar-contratos").style.display = "none";
    document.getElementById("reportes").style.display = "none";

    // Obtener todos los enlaces del navbar-left y del menu-overlay
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

    // Eventos para gestionar usuarios
    document.querySelectorAll('#gestionar-usuarios .usuario button').forEach(button => {
        button.addEventListener('click', function() {
            const action = button.textContent;
            const userName = button.closest('.usuario').querySelector('h3').textContent;
            
            if (action === 'Editar') {
                // Lógica para editar usuario
                alert('Editando usuario: ' + userName);
            } else if (action === 'Eliminar') {
                // Lógica para eliminar usuario
                alert('Eliminando usuario: ' + userName);
            }
        });
    });

    // Eventos para gestionar causas
    document.querySelectorAll('#gestionar-causas .causa button').forEach(button => {
        button.addEventListener('click', function() {
            const action = button.textContent;
            const causeName = button.closest('.causa').querySelector('h3').textContent;

            if (action === 'Ver Documentación') {
                // Lógica para ver documentación de la causa
                alert('Viendo documentación de: ' + causeName);
            } else if (action === 'Actualizar Estado') {
                // Lógica para actualizar estado de la causa
                alert('Actualizando estado de: ' + causeName);
            }
        });
    });

    // Eventos para gestionar contratos y documentos
    document.querySelectorAll('#gestionar-contratos .documento button').forEach(button => {
        button.addEventListener('click', function() {
            const action = button.textContent;
            const docName = button.closest('.documento').querySelector('h3').textContent;

            if (action === 'Ver Contrato' || action === 'Ver Documento') {
                // Lógica para ver contrato o documento
                alert('Viendo: ' + docName);
            } else if (action === 'Actualizar Contrato' || action === 'Actualizar Documento') {
                // Lógica para actualizar contrato o documento
                alert('Actualizando: ' + docName);
            }
        });
    });

    // Eventos para generar reportes
    document.querySelectorAll('#reportes .card button').forEach(button => {
        button.addEventListener('click', function() {
            const reportType = button.closest('.card').querySelector('h3').textContent;

            // Lógica para generar reportes
            alert('Generando reporte: ' + reportType);
        });
    });
});



//=============================================================================================================================

    // Script para manejar la edición de usuarios
    
