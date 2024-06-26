def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

#numeros de ejemplos:
#a=25
#b=32
#c=5

#operaciones:
#a+b=57         a+b 57>5 (c) SI
#b+c=37         b+c 37>25 (a) SI
#c+a=30         c+a 30>32 (b) NO
#No se cumple la última condición del and por lo tanto, no se cumple toda la operación y el resultado sería "No, no puede ser un triángulo"



a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')