from database.config import get_connection
from datetime import datetime, timedelta

class Prestamo:
    @staticmethod
    def registrar_prestamo(id_usuario, id_libro):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            # Verificar disponibilidad del libro
            cursor.execute("SELECT disponible FROM Libros WHERE id_libro = %s", (id_libro,))
            disponible = cursor.fetchone()[0]
            
            if not disponible:
                print("El libro no está disponible")
                return
            
            # Registrar préstamo
            query = """INSERT INTO Prestamos 
                      (id_usuario, id_libro, fecha_prestamo) 
                      VALUES (%s, %s, %s)"""
            values = (id_usuario, id_libro, datetime.now().date())
            
            cursor.execute(query, values)
            
            # Actualizar disponibilidad del libro
            cursor.execute("UPDATE Libros SET disponible = FALSE WHERE id_libro = %s", (id_libro,))
            
            connection.commit()
            print("Préstamo registrado exitosamente")
            
        except Exception as e:
            print(f"Error al registrar préstamo: {e}")
        finally:
            if connection:
                connection.close()

    @staticmethod
    def calcular_multa(id_prestamo):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            # Obtener información del préstamo y cuota mensual
            query = """
                SELECT p.fecha_prestamo, p.fecha_devolucion, u.cuota_mensual 
                FROM Prestamos p 
                JOIN Usuarios u ON p.id_usuario = u.id_usuario 
                WHERE p.id_prestamo = %s
            """
            cursor.execute(query, (id_prestamo,))
            prestamo = cursor.fetchone()
            
            if not prestamo:
                print("Préstamo no encontrado")
                return 0
                
            fecha_prestamo, fecha_devolucion, cuota_mensual = prestamo
            
            if not fecha_devolucion:
                dias_retraso = (datetime.now().date() - fecha_prestamo).days
            else:
                dias_retraso = (fecha_devolucion - fecha_prestamo).days
            
            if dias_retraso <= 0:
                return 0
                
            multa = (cuota_mensual * 0.03) * dias_retraso
            return round(multa, 2)
            
        except Exception as e:
            print(f"Error al calcular multa: {e}")
            return 0
        finally:
            if connection:
                connection.close()