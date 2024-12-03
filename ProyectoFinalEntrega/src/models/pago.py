from database.config import get_connection
from datetime import datetime

class Pago:
    @staticmethod
    def registrar_pago(id_usuario, monto):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = """INSERT INTO Pagos 
                      (id_usuario, fecha_pago, monto) 
                      VALUES (%s, %s, %s)"""
            values = (id_usuario, datetime.now().date(), monto)
            
            cursor.execute(query, values)
            connection.commit()
            print("Pago registrado exitosamente")
            
        except Exception as e:
            print(f"Error al registrar pago: {e}")
        finally:
            if connection:
                connection.close()

    @staticmethod
    def obtener_morosos():
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            
            query = """
                SELECT u.*, DATEDIFF(CURDATE(), u.fecha_registro)/30 as meses_antiguedad
                FROM Usuarios u
                LEFT JOIN Pagos p ON u.id_usuario = p.id_usuario
                GROUP BY u.id_usuario
                HAVING COUNT(p.id_pago) < DATEDIFF(CURDATE(), u.fecha_registro)/30
            """
            
            cursor.execute(query)
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error al obtener morosos: {e}")
            return []
        finally:
            if connection:
                connection.close()

    @staticmethod
    def modificar_cuota(id_usuario, nueva_cuota):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "UPDATE Usuarios SET cuota_mensual = %s WHERE id_usuario = %s"
            cursor.execute(query, (nueva_cuota, id_usuario))
            connection.commit()
            
            print("Cuota actualizada exitosamente")
            
        except Exception as e:
            print(f"Error al modificar cuota: {e}")
        finally:
            if connection:
                connection.close()