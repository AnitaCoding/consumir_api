import requests as consulta

categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
print('Categorías: ', categorias.json())
lista_categorias = categorias.json()
print('Último dato de lista categorías: ', lista_categorias[-1])

response = consulta.get('https://api.chucknorris.io/jokes/random?category=animal')

print('Código HTTP de respuesta: ', response.status_code)
print('Cabecera: ', response.headers['content-type'])
print('Encoding: ', response.encoding)
print('Respuesta en string: ', response.text)
print('Respuesta en JSON', response.json())