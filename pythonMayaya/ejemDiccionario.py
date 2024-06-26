dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
gustosMayaya = {
    "comida": "hamburguesa",
    "color": "morado", 
    "mascota": "perro",
    "bebida":"coca cola",
    "helado":"arequipe"}
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
print(gustosMayaya)
gustosMayaya['color']='azul'

#Para llamar cualquiera de los valores del diccionario:
print ("El color favorito de Mayaya es: ")
print (gustosMayaya["color"])



#AGREGAR NUEVAS CLAVES AL DICCIONARIO:

#1. Para agregar un par nuevo al diccionario
gustosMayaya["almuerzo"]="arroz con pollo"
print(gustosMayaya)

#2. Para insertar un elemento al diccionario con el método "update()"
gustosMayaya.update({"ropa":"vestido"})
print (gustosMayaya)

#ELIMINAR UNA CLAVE:


#Nota: al eliminar la clave también se removerá el valor asociado. 
#Los valores no pueden existir sin sus claves.
#Esto se logra con la instrucción "del".

#1. Para eliminar CUALQUIER clave del diccionario
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

del dictionary['perro']
print(dictionary)

#2. Para eliminar el último elemento del diccionario
#Se emplea el método "popitem()"
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
dictionary.popitem()
print(dictionary)





