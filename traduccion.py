# Lista de textos extraídos
textos = [
    'Open main menu', 'Inicio', 'Nosotros', 'Servicios', 'Compromiso Social', 
    'Contacto', 'CONTACTO', 'Contáctanos', '(+52) 332688 5165', 'Ventas', 
    'compras@redcycle.com', 'Inicio', 'Nosotros', 'Servicios', 'Compromiso', 
    'Contacto', 'Aviso de Privacidad', 'Aviso de Confidención minuciosa de productos, peso y embalaje, parcialidad', 
    'Calle Eca Do Queirós 5113-int 1, Jardines Universidad, 45110 Zapopan, Jalisco.', 
    'compras@redcycle.com', '(33) 2688 5165', '© 2023', 'Redcycle™', '.', 
    'Todos los derechos reservados.'
]



# Creación del diccionario para traducción
traducciones = {texto: None for texto in textos}

# Exportar a JSON
import json

with open('traducciones.json', 'w', encoding='utf8') as file:
    json.dump(traducciones, file, ensure_ascii=False, indent=4)

# Ahora traducciones.json contiene los textos con espacios para las traducciones al inglés
