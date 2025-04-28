print ("hola mundo")

#condicionales
#If, elif, else
numero = 11

if numero > 10:
    print("Mayor de 10")
elif numero == 10:
    print("Igual a 10")
else:
    print("Menor a 10")

#for
for i in range(5):
    print(i)

#while
contador = 1
while contador < 5:
    print(contador)
    contador += 1

#funciones
def saludar(nombre):
    print (f"hola, {nombre}!")

saludar("Juan")

#listas
lista = [1,2,3,4,5,6,7,8,9]
lista.append(10)
print(lista[1])
print(lista)

#tuplas, son como las listas, pero inmutables
tupla = (1,2,3)
print(tupla)

#diccionarios- Son equivalentes a los objetos en javascript
persona = { "nombre": "Juan", "edad": 30}
print(persona["nombre"])

#Conjuntos - Colecciones de elementos únicos, similares a un set de javascript
conjunto = { 1,2,3,4}
conjunto.add(5)
print(conjunto)

#For
nombres = ["Juan", "Pedro","Gabriel"]
for nombre in nombres:
    print(nombre)
#For in range - range ( inicio fin paso)
#Para hacer un rango de 2 en 2
for i in range(0, 10 , 2):
    print(i)

#se puede iterar en cadenas de texto
letras = "Tortuga"
for letra in letras:
    print(letra)

#iterar sobre diccionarios
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}
for clave in persona:
    print(clave)
#iterar sobre clave valores
for clave, valor in persona.items():
    print(clave, valor)

#recorrer listas con listas adentro
matriz = [[1,2,3],[4,5,6],[7,8,9]]
for fila in matriz:
    for elemento in fila:
        print(elemento)

#se puede usar else en for
for i in range(5):
    print(i)
else:
    print("El ciclo terminó")

#listas
mi_lista = [10,20,30,40,50,60,70,80,90]
#accediendo al primer elemento
print(mi_lista[0])
#accediendo al elemento en reversa
print(mi_lista[-2])
#accediendo a un rango de la lista (similar al slice)
print(mi_lista[1:4])
#modificar un elemento
mi_lista[1] = 25
print(mi_lista)
#reemplazar un rango de elementos
mi_lista[2:4] = [35,45]
print(mi_lista)

#metodos comunes en listas
#agregar un elemento al final de la lista
mi_lista.append(100)
print(mi_lista)

mi_lista.extend([110,120])
print(mi_lista)
#insertar elemento en una posición específica
mi_lista.insert(1,15)
print(mi_lista)
#elimina la primera ocurrencia de un valor específico
mi_lista.remove(25)
print(mi_lista)
#Pop, eliminar y devolver un elemento en el índice especificado, sino por defecto es el último
eliminado= mi_lista.pop(2)
print(eliminado)
print(mi_lista)
#index, devuelve el índice de la primera ocurrencia de un valor
indice = mi_lista.index(100)
print(indice)
#count, cuenta cuántas veces aparece un valor en una lista
print(mi_lista.count(15))
#invertir el orden de una lista
mi_lista.reverse()
print(mi_lista)
mi_lista.sort()
print(mi_lista)
#imprimir tamaño de la lista
print(len(mi_lista))
#comprobación de existencia
print(45 in mi_lista)


#tuplas
mitupla = (1,2,3,4,5,6)
#desempaquetado
a,b,c,d,e,f = mitupla
print(a)
print(b)
print(c)
#desempaquetado con el operador *
a, b, c, *resto = mitupla
print(a)
print(b)
print(c)
print(*resto)


#Diccionarios
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Buenos Aires"
}
#con get es más seguro acceder a un elemento porque no da error si la clave no existe
print(mi_diccionario.get("nombre"))
print(mi_diccionario.get("edad"))
print(mi_diccionario.get("altura"))
#modificar un valor
mi_diccionario["edad"] = 31
print(mi_diccionario)
#agregar un nuevo clave valor
mi_diccionario["pais"] = "Argentina"
print(mi_diccionario)
#eliminar clave valor
del mi_diccionario["pais"]
print(mi_diccionario)
#eliminar y obtener el mismo valor
pais = mi_diccionario.pop("ciudad")
print(pais)
print(mi_diccionario)


#funciones
#args acepta multiples argumentos como tupla
def sumar_todo(*numeros):
    return sum(numeros)

print(sumar_todo(1,2,3,4,5,6,7,8,9,10))
#kwargs acepta multiples argumentos con nombre como diccionario
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave, valor)

mostrar_datos(nombre="juan", edad=30, ciudad="Buenos Aires")


#Manejo de errores
try:
    #código que puede fallar
    #numero = int(input("Ingresa un numero: "))
    resultado = numero / 10
    print(resultado)
except zeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("Tenès que ingresar un número válido")
#se puede utilizar un else al final que funciona si el codigo sale bien
#Finally se ejecuta siempre, haya o no error

try:
    with open('datos.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("No se puede abrir el archivo, creándolo...")
    with open('datos.txt', 'w') as archivo:
        archivo.write("Archivo creado automáticamente")

#resumen:
#open('archivo.txt', 'r') leer archivo
#open('archivo.txt', 'w')   escribir archivo borrando de cero
#open('archivo.txt', 'a')   agregar al final
#with open () as    cerrar automáticamente

