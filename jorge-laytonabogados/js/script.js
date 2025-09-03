document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('appointmentForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Previene el envío tradicional del formulario
        console.log("Formulario enviado"); // Verifica que el evento se está capturando

        // Resto del código...
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const date = document.getElementById('date').value;
        const time = document.getElementById('time').value;

        const message = `Nombre: ${name}\nEmail: ${email}\nCelular: ${phone}\nFecha: ${date}\nHora: ${time}`;
        const whatsappLink = `https://wa.me/573014699561?text=${encodeURIComponent(message)}`;
        window.open(whatsappLink, '_blank');
    });
});
