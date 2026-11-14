
# SISTEMA DE GESTION DE PRODUCTOS
# PROGRAMACION ORIENTADA A OBJETOS (POO)
# ACTIVIDAD FORMATIVA 3: IMPLEMENTACION DE HERENCIA
# ==========================================


# CLASE 1: Producto (CLASE PADRE)
class Producto:

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


# CLASE 1.1: ProductoElectronico (CLASE DERIVADA)
class ProductoElectronico(Producto):

    def __init__(self, id_producto, nombre, precio,
                 cantidad, garantia):

        # Reutilizamos el constructor de Producto
        super().__init__(id_producto, nombre, precio, cantidad)

        # Atributo propio de la clase derivada
        self.garantia = garantia

    # Metodo propio de ProductoElectronico
    def mostrar_garantia(self):
        print(f"Garantia: {self.garantia} meses")

    # Sobrescritura del metodo de la clase padre
    def mostrar_informacion(self):
        super().mostrar_informacion()
        self.mostrar_garantia()


# CLASE 2: Inventario (CLASE PADRE)
class Inventario:

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


# CLASE 2.1: InventarioElectronico (CLASE DERIVADA)
class InventarioElectronico(Inventario):

    def __init__(self, nombre_tienda, departamento):

        # Reutilizamos el constructor de Inventario
        super().__init__(nombre_tienda)

        # Atributo propio de la clase derivada
        self.departamento = departamento

    # Metodo propio de InventarioElectronico
    def mostrar_departamento(self):
        print(f"Departamento: {self.departamento}")

    # Sobrescritura del metodo mostrar_productos
    def mostrar_productos(self):
        print("\n===== INVENTARIO ESPECIALIZADO =====")

        # Reutilizamos el metodo de la clase padre
        super().mostrar_productos()

        self.mostrar_departamento()


# CLASE 3: Aplicacion
class Aplicacion:

    def __init__(self):
        # Utilizamos la clase derivada InventarioElectronico
        self.inventario = InventarioElectronico(
            "Mi Tienda", "Electronica"
        )

    # Metodo para ejecutar el programa
    def ejecutar(self):

        while True:

            print("\n===== GESTION DE PRODUCTOS =====")
            print("1. Registrar producto electronico")
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

    # Metodo para registrar productos electronicos
    def registrar_producto(self):

        try:
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad disponible: "))
            garantia = int(input("Garantia en meses: "))

            if not id_producto.strip() or not nombre.strip():
                print("Error: el ID y el nombre son obligatorios.")
                return

            if precio < 0 or cantidad < 0 or garantia < 0:
                print("Error: no se permiten valores negativos.")
                return

            # Creamos un objeto de la clase derivada
            producto = ProductoElectronico(
                id_producto,
                nombre,
                precio,
                cantidad,
                garantia
            )

            # Utilizamos el metodo heredado de Inventario
            self.inventario.agregar_producto(producto)

        except ValueError:
            print("Error: introduce valores numericos validos.")

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
