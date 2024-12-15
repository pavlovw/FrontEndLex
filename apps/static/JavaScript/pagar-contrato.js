document.addEventListener('DOMContentLoaded', function() {
    var btnPagar = document.getElementById("btnPagar");
    if (btnPagar) {
        btnPagar.addEventListener("click", function(event) {
            event.preventDefault(); // Evitar el envío del formulario por defecto

            var opt = "VISA"; // Podrías obtener el tipo de tarjeta desde un elemento select
            var codigo = document.getElementById("numero_tarjeta").value.replace(/-/g, ''); 
            var VISA = /^4[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$/;
            var MASTERCARD = /^5[1-5][0-9]{2}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$/;
            var AMEX = /^3[47][0-9]{2}-?[0-9]{6}-?[0-9]{5}$/;
            var msg = "Tarjeta Inválida"; 
            var errorElement = document.getElementById("msgerror"); 
            errorElement.innerHTML = ""; 
            var nombreTarjeta = document.getElementById("nombre_tarjeta").value.trim();
            var cvv = document.getElementById("cvv").value.trim();
            
            if (opt.trim() === "" || codigo.trim() === "" || document.getElementById("fecha_vencimiento").value.trim() === "" || nombreTarjeta === "" || cvv === "") {
                errorElement.innerHTML = "Por favor, complete todos los campos";
                return;
            }

            var currentDate = new Date();
            var inputDateParts = document.getElementById("fecha_vencimiento").value.split('/');
            var inputMonth = parseInt(inputDateParts[0]);
            var inputYear = parseInt(inputDateParts[1]) + 2000;
            var inputDate = new Date(inputYear, inputMonth - 1, 1);

            if (currentDate > inputDate) {
                errorElement.innerHTML = "La fecha de expiración de la tarjeta es inválida";
                return;
            }

            if (luhn(codigo)) {
                switch (opt) {
                    case "VISA":
                        if (!codigo.match(VISA)) {
                            errorElement.innerHTML = msg; 
                            return;
                        }
                        break;
                    case "MASTERCARD":
                        if (!codigo.match(MASTERCARD)) {
                            errorElement.innerHTML = msg;
                            return;
                        }
                        break;
                    case "AMEX":
                        if (!codigo.match(AMEX)) {
                            errorElement.innerHTML = msg;
                            return;
                        }
                        break;
                    default:
                        errorElement.innerHTML = "Seleccione un tipo de tarjeta válido";
                        return;
                }
            } else {
                errorElement.innerHTML = msg;
                return;
            }
            
            // Simulación de pago exitoso, muestra el mensaje
            showPaymentSuccessMessage();
        });
    }

    function luhn(value) {
        if (/[^0-9-\s]+/.test(value)) return false;
        let nCheck = 0,
            bEven = false;
        value = value.replace(/\D/g, "");
        for (var n = value.length - 1; n >= 0; n--) {
            var cDigit = value.charAt(n),
                nDigit = parseInt(cDigit, 10);
            if (bEven && (nDigit *= 2) > 9) nDigit -= 9;
            nCheck += nDigit;
            bEven = !bEven;
        }
        return nCheck % 10 == 0;
    }

    function showPaymentSuccessMessage() {
        var paymentSuccessMessage = document.getElementById('payment-success-message');
        if (paymentSuccessMessage) {
            paymentSuccessMessage.classList.remove('hidden');
            // Coloca el mensaje de pago exitoso en el centro de la pantalla
            paymentSuccessMessage.style.top = `${window.innerHeight / 2 - paymentSuccessMessage.offsetHeight / 2}px`;
            paymentSuccessMessage.style.left = `${window.innerWidth / 2 - paymentSuccessMessage.offsetWidth / 2}px`;
        }


    }
});
