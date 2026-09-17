lista_categorias = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']

lista_diccionarios = []
contador = 1
for i in lista_categorias:
    lista_diccionarios.append({'Clave':contador, 'Categoría': i}) #agregar un diccionario por cada vuelta
    contador+=1

print(lista_diccionarios)

for diccionario in lista_diccionarios:
    print(f'{diccionario['Clave']} - {diccionario['Categoría']}')

seleccion = input('Seleccione una opción')

for diccionario in lista_diccionarios:
    if diccionario['Clave']== int(seleccion):
        print(f'La opción seleccionada es {diccionario['Categoría']}')