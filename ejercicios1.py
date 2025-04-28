clientes = ["juan perez","ana gonzalez", "luis rodriguez","Damian Suarez"]

with open('clientes.txt', 'w') as archivo:
    for cliente in clientes:
        archivo.write(cliente + '\n')

#leer un archivo y mostrar datos
with open('clientes.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip()) #strip quita el salto de línea

