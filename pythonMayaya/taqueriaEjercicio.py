
dictionary={"Baja Taco": 4.00,
"Burrito": 7.50,
"Bow1": 8.50,
"Nachos": 11.00,
"Quesadilla": 8.50,
"Super Burrito": 8.50,
"Super Quesadilla": 9.50,
"Taco": 3.00,
"Tortilla Salad": 8.00
}

print("Bienvenidos a Mayaya's Taqueria")
print("Menú disponible: ")
print(dictionary)

def taqueria():
    total_cuenta=0.0

    while True:
        try:
            producto=input("Ingrese un producto: \nDe lo contrario, \nsi desea terminar ejecute CTRL+Z ").strip()
        except EOFError:
            print("El total de su cuenta es: ")
            print(total_cuenta)
            break

        producto=producto.title()

        if producto in dictionary:
            total_cuenta+=dictionary[producto]
            print(f"Subtotal: ${total_cuenta:.2f}")
        else:
            print("Producto no disponible en nuestro menú")


if __name__=="__main__":
    taqueria()





     
