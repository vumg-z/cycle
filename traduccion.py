# Lista de textos extraídos
textos = [
    'Open main menu',
    'Inicio',
    'Nosotros',
    'Servicios',
    'Compromiso Social',
    'Contacto',
    'NOSOTROS',
    'Atendemos las necesidades específicas de todas las partes involucradas, tanto de calidad en los productos, tramitología y permisos, logística, entáctanos',
    'Conócenos',
    'Bienvenidos a Redcycle',
    'Atetre otros aspectos, realizando procesos minuciosos de licitaciones privadas para encontrar el mejor prospecto.',
    'Nuestros clientes y proveedores son compañías nacionales e internacionales, quienes se desempeñan en prácjor prospecto.',
    'Nosotros',
    'Nuestros Servicios',
    'Coticamente todas las ramas de la industria, confianza que nos han brindado desde el inicio de nuestras operaciones y se ha consolidado con el pasar del tiempo.',
    'INFRAESTRUCTURA',
    'Nuestra oficina corporativa se encuentra en Guadalajara Jalisco,rdines Universidad, 45110 Zapopan, Jalisco.',
    'compras esto, en virtud de ser una zona centro entre el centro, occidente, bajío y norte del país, además de contar con diversos clientes y proveedores en las zonas industriales y puertos más importantes de la región.',
    'Nuestra planta se encuentra ubicada en Ciudad Juárez Chihuahua, locación que hemos concretado por el alto número de empresas ubicadas en esa región del país, así como la cercanía y logística con Estados Unidos de América, país el cual, se concentran gran número de nuestros clientes y aliados.',
    'Inicio',
    'Nosotros',
    'Servicios',
    'Compromiso',
    'Contacto',
    'Aviso de Privacidad',
    'Aviso de Confidencialidad',
    'Calle Eca Do Queirós 5113-int 1, Jardines Universidad, 45110 Zapopan, Jalisco.',
    'compras@redcycle.com',
    '(33) 2688 5165',
    '© 2023',
    'Redcycle™. Todos los derechos reservados.'
]
# Creación del diccionario para traducción
traducciones = {texto: None for texto in textos}

# Exportar a JSON
import json

with open('traducciones.json', 'w', encoding='utf8') as file:
    json.dump(traducciones, file, ensure_ascii=False, indent=4)

# Ahora traducciones.json contiene los textos con espacios para las traducciones al inglés
