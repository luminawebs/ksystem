document.addEventListener("DOMContentLoaded", function () {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'es-ES';
    recognition.continuous = true;
    recognition.interimResults = false;

    const commands = {
        "llamar": () => window.location.href = "tel:+12624847309",
        "whatsapp": () => window.location.href = "whatsapp://send?phone=+12624847309&text=K@%20Hola.%20Me%20gustaria%20Cotizar%20un%20Servicio",
    };

    let modalInstance;
    let hasError = false;

    function openModal() {
        const modalElement = document.getElementById('reconocimiento');
        modalInstance = new bootstrap.Modal(modalElement);
        modalInstance.show();
    }

    function closeModal() {
        if (modalInstance) {
            modalInstance.hide();
        }
    }

    const startButton = document.getElementById('startVoice');
    if (startButton) {
        startButton.addEventListener('click', () => {
            try {
                recognition.start();
                openModal();
            } catch (error) {
                console.error("Error al iniciar el reconocimiento de voz:", error);
            }
        });
    }

    recognition.onresult = function (event) {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
            transcript += event.results[i][0].transcript;
        }
        transcript = transcript.toLowerCase();
        console.log("Texto reconocido:", transcript);

        if (commands[transcript]) {
            console.log(`Ejecutando comando: ${transcript}`);
            commands[transcript]();
            closeModal();
        } else {
            console.log("Comando no reconocido.");
        }
    };

    recognition.onerror = function (event) {
        hasError = true;
        console.error("Error de reconocimiento de voz:", event.error);
        closeModal();

        if (event.error === 'not-allowed') {
            alert("Permiso denegado. Activa el micrófono en la configuración del navegador.");
        }
    };

    recognition.onend = function () {
        if (!hasError) {
            recognition.start();
        } else {
            hasError = false;
        }
    };
});
