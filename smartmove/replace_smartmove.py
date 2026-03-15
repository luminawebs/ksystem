import os

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"d:\13 Key System\00site\smartmove"

# Common replacements
common_replacements = [
    ('images/logo-03.svg', 'images/logo_smart_move.png'),
    ('images/logo_vital_motion.png', 'images/logo_smart_move.png'),
    ('VMT - Vital Motion Training | OWN your movement. OWN your life.', 'Smart Move Solutions LLC | Moving Service'),
    ('VMT - Servicios | Entrenamiento Personal y Coaching en Kenosha', 'Smart Move Solutions LLC | Servicios de Mudanza'),
    ('VMT - Services | Personal Training and Coaching in Kenosha', 'Smart Move Solutions LLC | Moving Services'),
    ('Entrenamiento personal, coaching de imagen y marca personal. Fortalece tu cuerpo, mente y confianza.', 'We offer reliable moving services with skilled professionals, ensuring a seamless transition.'),
    ('Entrenamiento personal, coaching, imagen personal, marca personal, fitness, movimiento funcional, Kenosha', 'Moving service, complete moving service, delivery, reorders, packing, organizing'),
    ('Personal training, image coaching, and personal branding in Kenosha. Strengthen your body, mind, and confidence with our specialized services.', 'We offer reliable moving services with skilled professionals, ensuring a seamless transition.'),
    ('VMT, Vital Motion Training, personal training, personal coaching, personal image, personal brand, fitness, Kenosha, functional movement', 'Moving service, complete moving service, delivery, reorders, packing, organizing'),
    ('OWN YOUR MOVEMENT', 'SMART MOVE'),
    ('OWN YOUR LIFE', 'SOLUTIONS LLC'),
    ('HAZ TUYO EL MOVIMIENTO', 'SMART MOVE'),
    ('HAZ TUYA LA VIDA', 'SOLUTIONS LLC'),
    ('12623411927', '12624847309'),
    ('vitalmotiontrainingk@gmail.com', 'smartmovesolutionsllc@gmail.com'),
    ('+12623411927', '+12624847309'),
    ('WhatsApp', 'WhatsApp / Call: 262-484-7309 / 813-460-8601'),
    ('images/sobre-nosotros01.jpg', 'images/carrierteam_smart_move.jpg'),
    ('images/sobre-nosotros02.jpg', 'images/carrier_smart_move.jpg'),
    ('images/pbranding.jpg', 'images/services_smartmove.jpg'),
    ('images/coachingn.jpg', 'images/services_smartmove.jpg'),
    ('images/coachingl.jpg', 'images/carrier_smart_move.jpg'),
    ('images/coachingp.jpg', 'images/carrierteam_smart_move.jpg'),
    ('VMT - Entrenamiento personal, coaching de imagen y marca personal en Kenosha. Fortalece tu cuerpo, mente y confianza con nuestros servicios especializados.', 'Ofrecemos servicios de mudanza confiables con profesionales capacitados, asegurando una transición sin problemas.'),
]

# Spanish replacements
es_replacements = common_replacements + [
    ('¿QUÉ ES<br> VMT?', 'NUESTROS<br> SERVICIOS'),
    ('MARCA<br> PERSONAL', 'MUDANZA<br> COMPLETA'),
    ('COACHING<br> PERSONAL', 'ENTREGAS &<br> PEDIDOS'),
    ('COACHING<br> NUTRICIONAL', 'EMPAQUE &<br> ORGANIZACIÓN'),
    ('COACHING<br> LABORAL', 'OFERTAS<br> ESPECIALES'),
    ('<h2>QUÉ ES VMT</h2>', '<h2>NUESTROS SERVICIOS</h2>'),
    ('<h2>MARCA PERSONAL</h2>', '<h2>MUDANZA COMPLETA</h2>'),
    ('<h2> COACHING PERSONAL </h2>', '<h2> ENTREGAS & PEDIDOS </h2>'),
    ('<h2>NUTRITION COACHING</h2>', '<h2>EMPAQUE Y ORGANIZACIÓN</h2>'),
    ('<h2>COACHING LABORAL</h2>', '<h2>OFERTAS ESPECIALES</h2>'),
    ('<h3>SOBRE NOSOTROS</h3>', '<h3>NUESTROS SERVICIOS</h3>'),
    ('<h3>PROPIETARIOS</h3>', '<h3>NUESTRO EQUIPO</h3>'),
    ('<h3>LA EXPERIENCIA VMT</h3>', '<h3>POR QUÉ ELEGIRNOS</h3>'),
    ('>Vital Motion Training<', '>Smart Move Solutions LLC<'),
    ('>Firma de servicios personales que ofrece una experiencia integral de coaching para ayudar a las personas a mejorar su calidad de vida a través del movimiento físico y la reinvención de su imagen personal. VMT ofrece lo siguiente:<', '>Ofrecemos servicios de mudanza confiables con profesionales capacitados, asegurando una transición sin problemas.<'),
    ('>Misión<', '>Nuestra Misión<'),
    ('Contenido faltante', '[Servicio Placeholder - Más información pronto]'),
]

# English replacements
en_replacements = common_replacements + [
    ('WHAT IS<br> VMT?', 'OUR<br> SERVICES'),
    ('PERSONAL<br> BRAND', 'COMPLETE<br> MOVING'),
    ('PERSONAL<br> COACHING', 'DELIVERY &<br> REORDERS'),
    ('NUTRITION<br> COACHING', 'PACKING &<br> ORGANIZING'),
    ('CAREER<br> COACHING', 'SPECIAL<br> OFFERS'),
    ('<h2>WHAT IS VMT</h2>', '<h2>OUR SERVICES</h2>'),
    ('<h2>PERSONAL BRANDING</h2>', '<h2>COMPLETE MOVING SERVICE</h2>'),
    ('<h2>PERSONAL COACHING </h2>', '<h2>DELIVERY & REORDERS</h2>'),
    ('<h2>NUTRITION COACHING</h2>', '<h2>PACKING & ORGANIZING</h2>'),
    ('<h2>JOB COACHING</h2>', '<h2>SPECIAL OFFERS</h2>'),
    ('<h3>ABOUT US</h3>', '<h3>OUR SERVICES</h3>'),
    ('<h3>OWNERS</h3>', '<h3>OUR TEAM</h3>'),
    ('<h3>THE VMT EXPERIENCE</h3>', '<h3>WHY CHOOSE US</h3>'),
    ('>Vital Motion Training<', '>Smart Move Solutions LLC<'),
    ('>Personal services firm offering a comprehensive coaching experience to help individuals improve their quality of life through physical movement and re-imagining their personal image. VMT offers the following:<', '>We offer reliable moving services with skilled professionals, ensuring a seamless transition.<'),
    ('Missing content', '[Service Placeholder - More info coming soon]'),
]

replace_in_file(os.path.join(base_dir, 'index.html'), common_replacements)
replace_in_file(os.path.join(base_dir, 'e-menu.html'), es_replacements)
replace_in_file(os.path.join(base_dir, 'e-menuenglish.html'), en_replacements)

print("Replacement complete.")
