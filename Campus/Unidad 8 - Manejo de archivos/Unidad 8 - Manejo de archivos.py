




# # # 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos.
# # #  Cada línea debe tener: nombre,precio,cantidad

# print("\n1)")
# with open("productos.txt","w") as archivo:
#     archivo.write("Producto: Lapicera ")
#     archivo.write("| Precio: $120.5 ")
#     archivo.write("| Cantidad: 30")
#     archivo.write("\n")
#     archivo.write("Producto: Resaltador ")
#     archivo.write("| Precio: $252 ")
#     archivo.write("| Cantidad: 12")
#     archivo.write("\n")
#     archivo.write("Producto: Regla ")
#     archivo.write("| Precio: $155 ")
#     archivo.write("| Cantidad: 20")
# print("Archivo creado!")

# # 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# # línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# # formato:
# # Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# print("\n2)\n")

# with open("productos.txt","r") as archivo:
#     for linea in archivo:
#         # print(linea.strip())
#         partes = linea.strip(",")
#         print(partes)



# # 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# # los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# # cantidad) y lo agregue al archivo sin borrar el contenido existente.

# print("\n3)\n")

# with open("productos.txt","a") as archivo:
#     nuevo_producto = input("Ingrese un nuevo producto: ")
#     archivo.write(f"\nProducto: {nuevo_producto} ")
#     nuevo_precio = input(f"Ingrese el valor de {nuevo_producto}: ")
#     archivo.write(f"| Precio: ${nuevo_precio} ")
#     nueva_cantidad = input(f"Ingrese la cantidad de {nuevo_producto}: ")
#     archivo.write(f"| Cantidad: {nueva_cantidad} ")

# print("")
# with open("productos.txt","r") as archivo:
#     for linea in archivo:
#         # print(linea.strip())
#         partes = linea.strip(",")
#         print(partes)


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

# print("\n4)\n")
# productos = []

# with open("productos.txt", "r") as archivo:
#     for linea in archivo:
#         partes = linea.strip().split('|')
        
#         nombre = partes[0].split(':')
#         nombre = nombre[1].strip()
        
#         precio = partes[1].split(':')
#         precio = precio[1].strip()
        
#         cantidad = partes[2].split(':')
#         cantidad = cantidad[1].strip()
        
#         productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
# print(type(productos))
# print(productos)

# print(nombre)

# open("archivo.txt","r", encoding="utf-8")

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

# print("\n5)\n")

# bool = False
# seleccion = input("Ingrese el producto a buscar: ")
# indice=0
# print("")
# with open("productos.txt", "r") as archivo:
#     for linea in archivo:
#         indice+=1
#         partes = linea.strip().split('|')
#         nombre = partes[0].split(':')
#         nombre = nombre[1].strip()
#         if seleccion == nombre:
#             print(productos[indice-1])
#             bool = True

# if not bool:
#     print("El producto ingresado no está disponible")



# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split('|')
        
        nombre = partes[0].split(':')
        nombre = nombre[1].strip()
print(nombre)