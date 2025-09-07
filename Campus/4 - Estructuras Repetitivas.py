# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#for i in range(101):
#    print (f"{i}\n")


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

#digitios = len(num)
#num = (input("Ingrese un número entero: "))
#print(f"El número ingresado tiene {digitios} digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.
#num1 = int(input("Ingrese el primer número: "))
#num2 = int(input("Ingrese el segundo número: "))
#suma=0
#if num1>num2:
#    num1, num2=num2,num1
#    for i in range(num1+1,num2):
#        suma+=i
#elif num1<num2:
#    
#    for i in range(num1+1,num2):
#        suma+=i
#print(f"La suma es: {suma}")
#
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario
# ingrese un 0.

#suma = 0
#while True:
#    num = int(input("Ingrese un número entero (0 para finalizar): "))
#    if num == 0:
#        break
#    suma += num
#print(f"La suma total es: {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
#
#import random
#num_rand = random.randint(0,9)
#intentos=0
#while True:
#    juego = int(input("Ingrese el número que crea correcto: "))
#    intentos+=1
#    if juego == num_rand:
#        print("\nIngresó el número correcto!")
#        print(f"Le tomó {intentos} intentos.")
#        break
#

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

#for i in range(101):
#    if i % 2 == 0:
#        print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.
#num_usuario = int(input("Ingrese un número entero positivo: "))
#suma=0
#for i in range (0,num_usuario+1):
#    suma+=i
#print(f"La suma de todos los números anteriores al ingresado es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, 
# cuántos son negativos y cuántos son positivos.
# (Nota: para probar el programa puedes usar una cantidad menor, 
# pero debe estar preparado para procesar 100 números con un solo cambio).
#pares=0
#impares=0
#positivo=0
#negativo=0
#nulo=0
#for i in range(100):
#    numero=int(input(f"Ingrese el {i+1}º número: "))
#    if numero % 2 == 0:
#        pares+=1
#    else:
#        impares+=1
#    if numero>0:
#        positivo+=1
#    elif numero<0:
#        negativo+=1
#    elif numero == 0:
#        nulo+=1
#print(f"De los números ingresados: {pares} son pares, {impares} son impares, {positivo} son positivos, {negativo} son negativos y {nulo} son nulos (equivalen a cero)")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego 
# calcule la media de esos valores.
# (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).
#suma=0
#media=0
#for i in range(100):
#    num = int(input(f"Ingrese el {i+1}º num: "))
#    suma+= num
#media=suma/100
#print(f"La media de los números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado
# por el usuario.
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num=input("Ingrese un número entero: ")
long=len(num)

for i in range(long,0,-1):
    print(f"{num[i-1]}", end="")
