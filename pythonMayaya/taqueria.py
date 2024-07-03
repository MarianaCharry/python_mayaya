#Mariana Charry Prada - ADSO: 2694667 - 03/07/2024

print("Bienvenidos a Mayaya's Taqueria")
print("Nuestro menú disponible: ")
print("Baja Taco: 4.00")
print("Burrito: 7.50")
print("Bow1: 8.50")
print("Nachos: 11.00")
print("Quesadilla: 8.50")
print("Super Burrito: 8.50")
print("Super Quesadilla: 9.50")
print("Taco: 3.00")
print("Tortilla Salad: 8.00")


producto=input("Ingrese el producto que desea: ")
def prodcuto_elegido(producto):
    if producto=='Baja Taco':
        message='Elegiste baja taco'
    else:
        message='Este producto no existe en nuestro menú'
        print(message)

