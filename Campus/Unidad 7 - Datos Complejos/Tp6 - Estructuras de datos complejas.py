#1) ) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(f"1)")
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800
print(f"\n2)")
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
print(f"\n3)")
frutas = precios_frutas.keys()
print(frutas)


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# •
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# •
# Luego, pedí un nombre y mostrale el número asociado, si existe.
print(f"\n4)")
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del usuario: ")
    numero = input("Ingrese el número del usuario: ")
    contactos[nombre]=numero

buscar = input("Ingrese el nombre a buscar: ")
if buscar in contactos:
    print(f"El número de {buscar} es: {contactos[buscar]}")
else:
    print("No se encontró el contacto.")


# # 5) Solicita al usuario una frase e imprime:
# # Las palabras únicas (usando un set).
# # Un diccionario con la cantidad de veces que aparece cada palabra.
print("\n5)")
frase = input("Ingrese una frase")

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras_unicas:", palabras_unicas)
print("Recuento:", recuento)


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
print("\n6)")

alumnos={}

for i in range(3):
    nombre = input("Ingrese un nombre: ")
    notas= []
    for j in range(3):
        num = float(input(f"Ingrese la {j} nota: "))
        notas.append(num)
        alumnos[nombre] = tuple(notas)
    print(alumnos)

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# •
# Mostrá los que aprobaron ambos parciales.
# •
# Mostrá los que aprobaron solo uno de los dos.
# •
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
print("\n7)")#10
nombres = ("Juan","Matías","Facundo","Thiago","Tomás","Agustín","Enzo","Gabriel","Emiliano","Pedro")
lista1 = (8,6,9,7,4,8,2,5,7,3)
lista2 = (1,3,6,7,8,2,6,8,3,2)

print("Resultados del primer parcial: ", end="")
for i in range(0,len(lista1)):
    if lista1[i] >=6:
        print(f"{lista1[i]}(Aprobado)", end=" - ")
        continue
    print(f"{lista1[i]}(Desaprobado)", end=" - ")

print("\n\nResultados del Segundo Parcial: ", end="")
for i in range(0,len(lista2)):
    if lista2[i] >=6:
        print(f"{lista2[i]}(Aprobado)", end=" - ")
        continue
    print(f"{lista2[i]}(Desaprobado)", end=" - ")

print("\n\nQuienes aprobaron ambos: ")
for i in range(0,len(lista1)):
    if lista1[i] >=6 and lista2[i] >=6:
        print(f"{nombres[i]} Aprobó ambos con {lista1[i]} y {lista2[i]}")
        
print("\nQuienes aprobaron al menos uno: ")
for i in range(0,len(lista1)):
    if not (lista1[i] >=6 and lista2[i] >=6):
        print(f"{nombres[i]} Aprobó alguno de los dos con {lista1[i]} y {lista2[i]}")
        
print("\nTodos los estudiantes que aprobaron al menos un parcial: ")
for i in range(0,len(lista1)):
    if lista1[i] >=6 or lista2[i] >=6:
        print(f"{nombres[i]} con {lista1[i]} y {lista2[i]}")
        
        

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# •
# Consultar el stock de un producto ingresado.
# •
# Agregar unidades al stock si el producto ya existe.
# •
# Agregar un nuevo producto si no existe.
print("\n8)")
productos = {}
cant = int(input("Cuantos productos quiere ingresar: "))
for i in range(cant):
    nombre = input(f"Ingrese el nombre del {i+1}º producto: ")
    stock = int(input(f"Ingrese el stock de {nombre}: "))
    productos[nombre]=stock


print("Los productos disponibles son:")
print(productos.keys())

entrada = input("Consultar el stock de un producto: ")
if entrada in productos:
    print(f"{entrada}: {productos[entrada]}")
else:
    print("Ingrese un producto válido.")

consulta = input("Ingrese el producto al que quiera modificar su stock: ")
if consulta in productos:
    agregar = int(input(f"Ingrese el nuevo stock de {consulta}: "))
    productos[consulta]=agregar
else:
    print("Ingrese un producto válido.")
print(productos)

nuevo = input("Agregar un nuevo producto: ")
if nuevo in productos:
    print("El producto ya se encuentra en stock")
else:
    productos[nuevo]=0
print(productos)


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora
print("\n9)")
agenda = {}
dia_hora = input("Ingrese el día y la hora separada por comas: ")
dia,hora = dia_hora.split(",")
evento = input(f"Ingrese el evento que sucederá el {dia} a las {hora}: ")
agenda[dia,hora]=evento
print(agenda)

actividad = input("Ingrese el día y hora (separados por coma) que quiera consultar: ")
consulta_dia,consulta_hora=actividad.split(",")
if agenda[consulta_dia,consulta_hora]:
    print(f"El {consulta_dia} a las {consulta_hora} tiene el evento: {evento}")
else:
    print("LOL")
    
    
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# •
# Las capitales sean las claves.
# •
# Los países sean los valores.
print("\n10)")
paises={}
invertido={}
cantidad = int(input("Ingrese la cantidad de países a agregar (al menos 2): "))
if cantidad >=2:
    for i in range(cantidad):
        pais= input(f"Ingrese el {i+1}º país: ")
        capital= input(f"Ingrese la capital de {i+1}: ")
        paises[pais]=capital
        invertido[capital]=pais
    print(f"Original: {paises}")
    print(f"Invertido: {invertido}")
else:
    print("Cantidad incorrecta")