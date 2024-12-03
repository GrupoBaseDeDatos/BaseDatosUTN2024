from database.config import get_connection
from datetime import datetime

class Usuario:
    @staticmethod
    def agregar_usuario(nombre, direccion, telefono, email, cuota_mensual):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = """INSERT INTO Usuarios 
                      (nombre, direccion, telefono, email, fecha_registro, cuota_mensual) 
                      VALUES (%s, %s, %s, %s, %s, %s)"""
            values = (nombre, direccion, telefono, email, datetime.now().date(), cuota_mensual)
            
            cursor.execute(query, values)
            connection.commit()
            print("Usuario agregado exitosamente")
            
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
        finally:
            if connection:
                connection.close()

    @staticmethod
    def buscar_usuarios(criterio, valor):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            
            query = f"SELECT * FROM Usuarios WHERE {criterio} LIKE %s"
            cursor.execute(query, (f"%{valor}%",))
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error al buscar usuarios: {e}")
            return []
        finally:
            if connection:
                connection.close()

    @staticmethod
    def actualizar_usuario(id_usuario, campo, valor):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = f"UPDATE Usuarios SET {campo} = %s WHERE id_usuario = %s"
            cursor.execute(query, (valor, id_usuario))
            connection.commit()
            
            print("Usuario actualizado exitosamente")
            
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
        finally:
            if connection:
                connection.close()

    @staticmethod
    def eliminar_usuario(id_usuario):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM Usuarios WHERE id_usuario = %s"
            cursor.execute(query, (id_usuario,))
            connection.commit()
            
            print("Usuario eliminado exitosamente")
            
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
        finally:
            if connection:
                connection.close()