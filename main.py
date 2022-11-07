import pickle

libros = []

class mostrar_opciones():
    def Opciones(self):
        print('================================LISTA DE OPCIONES======================')
        print('Opción 1: Leer archivo de disco duro (.txt o csv).')
        print('Opción 2: Listar libros.')
        print('Opción 3: Agregar libro.')
        print('Opción 4: Eliminar libro.')
        print('Opción 5: Buscar libro por ISBN o por título.')
        print('Opción 6: Ordenar libros por título.')
        print('Opción 7: Buscar libros por autor, editorial o género.')
        print('Opción 8: Buscar libros por número de autores.')
        print('Opción 9: Editar o actualizar datos de un libro.')
        print('Opción 10: Guardar libros en archivo de disco duro (.txt o csv).')
        print('Opción 11: Salir :)')
        print('=======================================================================')

class leer_libro():
    def leer(self):
        with open("libros.txt", "rb") as f:
            agregar = pickle.load(f)
            for i in agregar:
                libros.append(i)
            print('======================LISTANDO LIBROS AGREGADOS=======================')
            for cont, i in enumerate(libros):
                print(f'{cont} - {i}')
            print('=======================================================================')




