'''
1.	Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
Llamar a esta función desde el programa principal.
'''
print("---1)---")
def imprimir_hola_mundo():
    return "Hola Mundo!"

print(imprimir_hola_mundo())



'''
2.	Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
Llamar a esta función desde el programa principal solicitando el nombre al usuario.
'''
print("\n---2)---")
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre=input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

'''
3.	Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en
[residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
'''

print("\n---3)---")
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}."

nombre=input("Ingrse su nombre: ")
apellido=input("Ingrse su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su residencia: ")
print(informacion_personal(nombre,apellido,edad,residencia))

'''
4.	Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio 
como parámetro y devuelva el perímetro del círculo.
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
'''
print("\n---4)---")
import math
def calcular_area_circulo(radio):
    area=(math.pi)*math.pow((radio),2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro=2*(math.pi)*(radio)
    return perimetro


radio=float(input("Ingrese el radio del circulo: "))
print(f"Area de {radio}: {calcular_area_circulo(radio)}")
print(f"Perimetro de {radio}: {calcular_perimetro_circulo(radio)}")


'''
5.	Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de 
segundos como parámetro y devuelva la cantidad de horas correspondientes. 
Solicitar al usuario los segundos y mostrar el resultado usando esta función.
'''

print("\n---5)---")
def segundos_a_horas(segundos):
    minuto=segundos/60
    hora=minuto/60
    return hora

segundos=int(input("Ingrese los segundos que quiera pasara a horas: "))

print(segundos_a_horas(segundos))

'''
6.	Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro 
y imprima la tabla de multiplicar de ese número del 1 al 10. 
Pedir al usuario el número y llamar a la función.
'''

print("\n---6)---")
def tabla_multiplicar(numero):
    for i in range(11):
        print(f"{numero} x {i} = {numero*i}")

numero=int(input("Ingrese un número:\n"))

tabla_multiplicar(numero)

'''
7.	Crear una función llamada operaciones_basicas(a, b) que reciba dos números como 
parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y 
dividirlos. Mostrar los resultados de forma clara.
'''

print("\n---7)---")
def operaciones_basicas(a,b):
    suma = a+b
    resta = a-b
    mult = a*b
    division = a/b
    return (suma,resta,mult,division)

a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))

print(f"{a} + {b} = {operaciones_basicas(a,b)[0]}")
print(f"{a} - {b} = {operaciones_basicas(a,b)[1]}")
print(f"{a} * {b} = {operaciones_basicas(a,b)[2]}")
print(f"{a} / {b} = {operaciones_basicas(a,b)[3]}")
print(type(operaciones_basicas(a,b)))


'''
8.	Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos 
y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario 
los datos y llamar a la función para mostrar el resultado con dos decimales.
'''

print("\n---8)---")
def calcular_imc(peso, altura):
    IMC = (peso)/ (altura*altura)
    return IMC

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))

print(f"El IMC es: {calcular_imc(peso,altura):.2f}")

'''
9.	Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura 
en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura
en Celsius y mostrar el resultado usando la función.
'''

print("\n---9)---")
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius*1.8)+32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en celsius: "))
print(f"{celsius}Cº son {celsius_a_fahrenheit(celsius)}Fº.")

'''
Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado 
usando esta función-
'''

print("\n---10)---")
def calcular_promedio(a, b, c):
    sumatoria=a+b+c
    promedio=sumatoria/3
    return promedio

a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
c=float(input("Ingrese el tercer número: "))
print(f"El promedio de {a}, {b} y {c} es: {calcular_promedio(a,b,c)}")


