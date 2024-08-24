import requests
from .models import Autor

def fetch_and_save_authors():
    response = requests.get('https://openlibrary.org/authors/OL1A.json')
    data = response.json()
    
    autor, created = Autor.objects.get_or_create(
        nome = data['nome'],
        email=f'{data['key']}@openlibrary.org'
    )
    
    #Salva no Banco Externo
    autor.save(using='mysql')
    
    return autor
    