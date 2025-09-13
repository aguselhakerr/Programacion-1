# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.
lista=[]
for i in range(1,101):
    if i %4 == 0:
        lista.append(i)
print (lista)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!
lista1=["no", "sé", "qué", "poner", "acá"]
print(f"Lista completa: {lista1}")
print(f"indexing positivo lista1[3]: {lista1[3]}")
print(f"indexing negativo lista1[-2]: {lista1[-2]}")

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista
# resultante por pantalla.
lista_vacia=[]
lista_vacia.append("My")
lista_vacia.append("Name")
lista_vacia.append("Is")
#for i in range(3):
#    lista_vacia.append("Hi")
#    lista_vacia.append("My name is..")
#lista_vacia.append("Slim Shady")
print (lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras 
# “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar 
# cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]

print(f"\nIndexin positivo: ")
animales[1]="loro"
animales[3]="oso"
print(animales)

print(f"\nIndexing negativo: ")
animales[-3]="loro"
animales[-1]="oso"
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros= [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
print(f"El programa remueve el número más grande")

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.
lista_numeros=[]
for i in range(10,31,5):
    lista_numeros.append(i)
print(f"{lista_numeros[0]},{lista_numeros[1]}")


#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1]="TMAP"
autos[2]="NOLSALP"
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.
dobles=[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1]="tallarines"
#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
#d) Imprimir la lista resultante por pantalla
print(compras)


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidada=[]
#● Posición lista_anidada[0]: 15
lista_anidada=[15]
#● Posición lista_anidada[1]: True
lista_anidada=[[15],[True]]
#● Posición lista_anidada[2][0]: 25.5
lista_anidada=[[15],[True],[25.5]]
#● Posición lista_anidada[2][1]: 57.9
lista_anidada[2].append(57.9)
#● Posición lista_anidada[2][2]: 30.6
lista_anidada[2].append(30.6)
#● Posición lista_anidada[3]: False
lista_anidada.append([False])
#Imprimir la lista resultante por pantalla.
print(lista_anidada)