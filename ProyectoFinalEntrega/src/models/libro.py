from database.config import get_connection

class Libro:
    @staticmethod
    def agregar_libro(titulo, autor, año_publicacion, isbn):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = """INSERT INTO Libros 
                      (titulo, autor, año_publicacion, isbn, disponible) 
                      VALUES (%s, %s, %s, %s, TRUE)"""
            values = (titulo, autor, año_publicacion, isbn)
            
            cursor.execute(query, values)
            connection.commit()
            print("Libro agregado exitosamente")
            
        except Exception as e:
            print(f"Error al agregar libro: {e}")
        finally:
            if connection:
                connection.close()

    @staticmethod
    def buscar_libros(criterio, valor):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            
            query = f"SELECT * FROM Libros WHERE {criterio} LIKE %s"
            cursor.execute(query, (f"%{valor}%",))
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error al buscar libros: {e}")
            return []
        finally:
            if connection:
                connection.close()

    @staticmethod
    def actualizar_libro(id_libro, campo, valor):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = f"UPDATE Libros SET {campo} = %s WHERE id_libro = %s"
            cursor.execute(query, (valor, id_libro))
            connection.commit()
            
            print("Libro actualizado exitosamente")
            
        except Exception as e:
            print(f"Error al actualizar libro: {e}")
        finally:
            if connection:
                connection.close()

    @staticmethod
    def eliminar_libro(id_libro):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM Libros WHERE id_libro = %s"
            cursor.execute(query, (id_libro,))
            connection.commit()
            
            print("Libro eliminado exitosamente")
            
        except Exception as e:
            print(f"Error al eliminar libro: {e}")
        finally:
            if connection:
                connection.close()