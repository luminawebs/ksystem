<?php
// Recibimos los datos del formulario
$nombre = isset($_POST['nombre']) ? $_POST['nombre'] : '';
$email = isset($_POST['email']) ? $_POST['email'] : '';
$telefono = isset($_POST['telefono']) ? $_POST['telefono'] : '';  // Aseguramos que se reciba el teléfono
$fecha = isset($_POST['fecha']) ? $_POST['fecha'] : '';
$hora = isset($_POST['hora']) ? $_POST['hora'] : '';

// Codificamos los datos para que puedan ser enviados en un enlace
$mensaje = urlencode("Nuevo agendamiento:\n\nNombre: $nombre\nCorreo: $email\nTeléfono: $telefono\nFecha: $fecha\nHora: $hora");

// Número de WhatsApp (aquí puedes poner tu número de WhatsApp o el número del servicio)
$whatsapp_number = "+18475589222";  // Cambia esto por tu número

// Enlace de WhatsApp
$url = "https://wa.me/$whatsapp_number?text=$mensaje";

// Redirigir a WhatsApp con el mensaje
header("Location: $url");
exit();
?>
