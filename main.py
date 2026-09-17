import requests as consulta

categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
print('Categorías: ', categorias.json())
lista_categorias = categorias.json()
print('Último dato de lista categorías: ', lista_categorias[-1])
lista_categorias = categorias.json()
lista_categorias_dic = []
contador = 1
for i in lista_categorias:
    lista_categorias_dic.append({'Clave':contador, 'Categoría': i}) #agregar un diccionario por cada vuelta
    contador+=1

for diccionario in lista_categorias_dic:
    print(f'{diccionario['Clave']} - {diccionario['Categoría']}')

seleccion = input('Seleccione una opción ')
categoria_seleccionada = None

for diccionario in lista_categorias_dic:
    if diccionario['Clave'] == int(seleccion):
        categoria_seleccionada = diccionario['Categoría']
        #print(f'La opción seleccionada es {diccionario['Categoría']}')


response = consulta.get(f'https://api.chucknorris.io/jokes/random?category={categoria_seleccionada}')

#print('Código HTTP de respuesta: ', response.status_code)
#print('Cabecera: ', response.headers['content-type'])
#print('Encoding: ', response.encoding)
#print('Respuesta en string: ', response.text)
print('Respuesta en JSON', response.json())

#Ejemplo para acceder a un valor del JSON
print(response.json()['value'])