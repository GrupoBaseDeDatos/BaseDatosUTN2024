from models.usuario import Usuario
from models.libro import Libro
from models.prestamo import Prestamo
from models.pago import Pago

def test_sistema():
    print("\n=== Prueba de búsqueda de usuarios ===")
    usuarios = Usuario.buscar_usuarios("nombre", "Ana")
    print("Usuarios con nombre 'Ana':", usuarios)

    print("\n=== Prueba de búsqueda de libros ===")
    libros = Libro.buscar_libros("autor", "García")
    print("Libros de García Márquez:", libros)

    print("\n=== Prueba de cálculo de multa ===")
    multa = Prestamo.calcular_multa(1)
    print(f"Multa del préstamo 1: ${multa}")

    print("\n=== Prueba de reporte de morosos ===")
    morosos = Pago.obtener_morosos()
    print("Morosos encontrados:", morosos)

if __name__ == "__main__":
    test_sistema()
