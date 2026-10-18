# SISTEMA DE GESTION DE PRODUCTOS
# Programacion Orientada a Objetos (POO)
# ==========================================

# CLASE 1: Producto
class Producto:
    # Constructor
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

     # Metodo para mostrar la informacion
    def mostrar_informacion(self):
        print(f"ID: {self.id_producto}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad disponible: {self.cantidad}")
        print("-" * 30)

    # Metodo para calcular el valor del inventario
    def calcular_valor(self):
        return self.precio * self.cantidad

    # Metodo para actualizar la cantidad
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad
            print("Cantidad actualizada correctamente.")
        else:
            print("Error: la cantidad no puede ser negativa.")

# CLASE 2: Inventario
class Inventario:
    # Constructor
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    # Metodo para agregar un producto
    def agregar_producto(self, producto):
        for existente in self.productos:
            if existente.id_producto == producto.id_producto:
                print("Error: el ID del producto ya existe.")
                return

        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado correctamente.")

    # Metodo para mostrar todos los productos
    def mostrar_productos(self):
        print(f"\nINVENTARIO DE {self.nombre_tienda.upper()}")
        print("=" * 35)

        if not self.productos:
            print("No hay productos registrados.")
            return

        for producto in self.productos:
            producto.mostrar_informacion()

    # Metodo para buscar un producto por ID
    def buscar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto

        return None

    # Metodo para calcular el valor total del inventario
    def calcular_inventario(self):
        total = 0

        for producto in self.productos:
            total += producto.calcular_valor()

        return total

# CLASE 3: Aplicacion
class Aplicacion:
    # Constructor
    def __init__(self):
        self.inventario = Inventario("Mi Tienda")

    # Metodo para ejecutar el programa
    def ejecutar(self):
        while True:
            print("\n===== GESTION DE PRODUCTOS =====")
            print("1. Registrar producto")
            print("2. Mostrar productos")
            print("3. Buscar producto")
            print("4. Actualizar cantidad")
            print("5. Mostrar valor del inventario")
            print("6. Salir")

            opcion = input("Selecciona una opcion: ")

            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.inventario.mostrar_productos()
            elif opcion == "3":
                self.consultar_producto()
            elif opcion == "4":
                self.modificar_cantidad()
            elif opcion == "5":
                total = self.inventario.calcular_inventario()
                print(f"Valor total del inventario: ${total:.2f}")
            elif opcion == "6":
                print("Gracias por utilizar el sistema.")
                break
            else:
                print("Opcion no valida. Intenta nuevamente.")

    # Metodo para registrar productos
    def registrar_producto(self):
        try:
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad disponible: "))

            if not id_producto.strip() or not nombre.strip():
                print("Error: el ID y el nombre son obligatorios.")
                return

            if precio < 0 or cantidad < 0:
                print("Error: el precio y la cantidad no pueden ser negativos.")
                return

            producto = Producto(
                id_producto, nombre, precio, cantidad
            )

            self.inventario.agregar_producto(producto)

        except ValueError:
            print("Error: introduce un precio o cantidad validos.")

    # Metodo para consultar un producto
    def consultar_producto(self):
        id_producto = input("Ingresa el ID que deseas buscar: ")
        producto = self.inventario.buscar_producto(id_producto)

        if producto:
            producto.mostrar_informacion()
        else:
            print("Producto no encontrado.")

    # Metodo para modificar existencias
    def modificar_cantidad(self):
        id_producto = input("ID del producto: ")
        producto = self.inventario.buscar_producto(id_producto)

        if producto:
            try:
                cantidad = int(input("Nueva cantidad: "))
                producto.actualizar_cantidad(cantidad)
            except ValueError:
                print("Error: introduce una cantidad entera.")
        else:
            print("Producto no encontrado.")


# CREACION DEL OBJETO PRINCIPAL
programa = Aplicacion()

# INICIO DE LA APLICACION
programa.ejecutar()
