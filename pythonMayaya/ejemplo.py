# Diccionario con los nombres de los productos y sus precios
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bow1": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total_cost = 0.0
    
    while True:
        try:
            # Leer la entrada del usuario (con control D para terminar)
            line = input("Ingrese un artículo (CTRL+D para terminar): ").strip()
        except EOFError:
            break  # Si el usuario presiona CTRL+D para terminar, se sale del bucle
        
        # Convertir la entrada a título para manejar variaciones de mayúsculas/minúsculas
        line = line.title()
        
        # Verificar si el artículo está en el menú
        if line in menu:
            total_cost += menu[line]
            print(f"Costo total hasta ahora: ${total_cost:.2f}")
        else:
            print("Artículo no válido, por favor ingrese uno del menú.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
