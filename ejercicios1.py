clientes = ["juan perez","ana gonzalez", "luis rodriguez","Damian Suarez"]

with open('clientes.txt', 'w') as archivo:
    for cliente in clientes:
        archivo.write(cliente + '\n')

#leer un archivo y mostrar datos
with open('clientes.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip()) #strip quita el salto de línea

#registro de movimientos contables en un archivo
movimientos = [
    "01/04/2025 - Venta - $5000",
    "02/04/2025 - Pago servicios - $15000",
    "03/04/2025 - Compra insumos - $10000",
]

with open('movimientos.txt', 'a') as archivo:
    for movimiento in movimientos:
        archivo.write(movimiento + '\n')

#POO
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hace un sonido.")

# Clase hija
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Otra clase hija
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Crear objetos
perro = Perro("Fido")
gato = Gato("Mishi")

perro.hablar()
gato.hablar()