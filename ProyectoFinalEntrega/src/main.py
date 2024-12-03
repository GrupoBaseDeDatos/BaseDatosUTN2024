from models.usuario import Usuario
from models.libro import Libro
from models.prestamo import Prestamo
from models.pago import Pago

def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===")
    print("1. Gestión de Usuarios")
    print("2. Gestión de Libros")
    print("3. Gestión de Préstamos")
    print("4. Búsqueda y Filtrado")
    print("5. Reporte de Morosos")
    print("6. Modificación de Cuota")
    print("0. Salir")

def menu_usuarios():
    while True:
        print("\n=== GESTIÓN DE USUARIOS ===")
        print("1. Agregar usuario")
        print("2. Ver usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("0. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            cuota = float(input("Cuota mensual: "))
            Usuario.agregar_usuario(nombre, direccion, telefono, email, cuota)
        
        elif opcion == "2":
            criterio = input("Seleccionar por (nombre/email): ") #buscamos por nombre o email
            valor = input("Valor a buscar: ") #con valor hace referencia al nombre o email
            usuarios = Usuario.buscar_usuarios(criterio, valor)
            for usuario in usuarios:
                print(usuario)
        
        elif opcion == "0":
            break

def menu_libros():
    while True:
        print("\n=== GESTIÓN DE LIBROS ===")
        print("1. Agregar libro")
        print("2. Ver libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("0. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            año = int(input("Año de publicación: "))
            isbn = input("ISBN: ")
            Libro.agregar_libro(titulo, autor, año, isbn)
        
        elif opcion == "2":
            criterio = input("Buscar por (titulo/autor): ")
            valor = input("Valor a buscar: ")
            libros = Libro.buscar_libros(criterio, valor)
            for libro in libros:
                print(libro)
        
        elif opcion == "0":
            break

def menu_prestamos():
    while True:
        print("\n=== GESTIÓN DE PRÉSTAMOS ===")
        print("1. Registrar préstamo")
        print("2. Calcular multa")
        print("0. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            id_usuario = int(input("ID de usuario: "))
            id_libro = int(input("ID de libro: "))
            Prestamo.registrar_prestamo(id_usuario, id_libro)
        
        elif opcion == "2":
            id_prestamo = int(input("ID de préstamo: "))
            multa = Prestamo.calcular_multa(id_prestamo)
            print(f"La multa es de: ${multa}")
        
        elif opcion == "0":
            break

def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            menu_usuarios()
        
        elif opcion == "2":
            menu_libros()
        
        elif opcion == "3":
            menu_prestamos()
        
        elif opcion == "4":
            print("\n=== BÚSQUEDA Y FILTRADO ===")
            tipo = input("Buscar (usuarios/libros): ")
            criterio = input("Criterio de búsqueda: ")
            valor = input("Valor a buscar: ")
            
            if tipo == "usuarios":
                resultados = Usuario.buscar_usuarios(criterio, valor)
            else:
                resultados = Libro.buscar_libros(criterio, valor)
                
            for resultado in resultados:
                print(resultado)
        
        elif opcion == "5":
            print("\n=== REPORTE DE MOROSOS ===")
            morosos = Pago.obtener_morosos()
            if morosos:
                total_meses = sum(moroso['meses_antiguedad'] for moroso in morosos)
                promedio = total_meses / len(morosos)
                print(f"Promedio de meses de antigüedad de morosos: {promedio:.2f}")
                for moroso in morosos:
                    print(moroso)
            else:
                print("No hay morosos registrados")
        
        elif opcion == "6":
            print("\n=== MODIFICACIÓN DE CUOTA ===")
            id_usuario = int(input("ID de usuario: "))
            nueva_cuota = float(input("Nueva cuota mensual: "))
            Pago.modificar_cuota(id_usuario, nueva_cuota)
        
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema!")
            break

if __name__ == "__main__":
    menu_principal()