# Lista de textos extraídos
textos = ['Open main menu', 'Inicio', 'Nosotros', 'Servicios', 'Compromiso Social', 'Contacto', 'REDCYCLE® es una empresa 100% mexicana con suficiente experiencia en asesoría en reciclaje y manejo de residuos\r\n de todo tipo, siendo especialistas en', 'metales', '.', 'Contáctanos', 'Conócenos', 'Bienvenidos a Redcycle', 'Atendemos\r\n las necesidades específicas de todas las partes involucradas, tanto de calidad en los productos,\r\n tramitología y permisos, logística, entre otros aspectos, realizando procesos minuciosos de licitaciones\r\n privadas para encontrar el mejor prospecto.', 'Nosotros', 'Nuestros Servicios', 'Conoce más sobre nuestros servicios', 'INTERMEDIACIÓN MERCANTIL', 'COMPRA Y VENTA DE MATERIALES', 'RECICLAJE Y TRANSPORTE', 'Inicio', 'Nosotros', 'Servicios', 'Compromiso', 'Contacto', 'Aviso de Privacidad', 'Aviso de Confidencialidad', 'Calle Eca Do Queirós 5113-int 1, Jardines Universidad, 45110 Zapopan, Jalisco.', 'compras@redcycle.com', '(33) 2688 5165', '© 2023', 'Redcycle™', '. Todos los derechos reservados.']

# Creación del diccionario para traducción
traducciones = {texto: None for texto in textos}

# Exportar a JSON
import json

with open('traducciones.json', 'w', encoding='utf8') as file:
    json.dump(traducciones, file, ensure_ascii=False, indent=4)

# Ahora traducciones.json contiene los textos con espacios para las traducciones al inglés
