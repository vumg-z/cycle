
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

# Reemplaza 'your_website_url' con la URL de tu página web.
url = 'http://127.0.0.1:5501/contacto.html'

# Realiza una petición GET para obtener el contenido de la página.
response = requests.get(url)

# Verifica que la petición fue exitosa.
if response.ok:
    # Crea un objeto BeautifulSoup para analizar el HTML obtenido.
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encuentra todos los elementos que contengan texto.
    text_elements = soup.find_all(string=True)
    
    # Filtra el texto y elimina aquellos que sean espacios en blanco o no relevantes.
    visible_texts = filter(tag_visible, text_elements)
    visible_texts = [text.strip() for text in visible_texts if text.strip()]

    # Convierte el texto a una lista.
    visible_texts = list(visible_texts)
    
    # Aquí puedes hacer lo que necesites con los textos, como guardarlos en un JSON.
    print(visible_texts)
else:
    print("Error al obtener la página")
