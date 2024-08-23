inventario = [{"nombre": "McFlurry", "precio": 2.50, "stock": 10}]

def menu_principal():
    """
    Muestra el menú principal.
    """
    while True:
        print("\nMenú Principal")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente otra vez.")

def agregar_producto():
    """
    Agrega un nuevo producto al inventario o actualiza el stock de un producto existente.
    """
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    # Buscar si el producto ya existe
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            producto["stock"] += cantidad
            print(f"Cantidad del producto {nombre} actualizada. Nuevo stock: {producto['stock']}.")
            return
    
    # Si el producto no existe, agregarlo al inventario
    producto = {"nombre": nombre, "precio": precio, "stock": cantidad}
    inventario.append(producto)
    print(f"Producto {nombre} agregado al inventario con stock: {cantidad}.")

def mostrar_inventario():
    """
    Muestra todos los productos del inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\nInventario:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['stock']}")

def vender_producto():
    """
    Vende un producto, actualiza el inventario y muestra el total de la venta.
    """
    nombre = input("Ingrese el nombre del producto que desea vender: ")
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            cantidad = int(input(f"¿Cuántas unidades de {nombre} desea vender?: "))
            if cantidad <= producto["stock"]:
                producto["stock"] -= cantidad
                total = cantidad * producto["precio"]
                print(f"Venta realizada. Total: ${total:.2f}")
                
                if producto["stock"] == 0:
                    print(f"El producto {nombre} se ha agotado.")
                
                return
            else:
                print("No hay suficiente stock en inventario.")
                return
    print("Producto no encontrado en el inventario.")

menu_principal()