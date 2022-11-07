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


class mostrar_libros():
    def mostrar(self, fi):
        self.f = fi
        print('===========================LISTANDO LIBROS=============================')
        for cont, i in enumerate(self.f):
            print(f'{cont} - {i}')
        print('=======================================================================')

class agregar_libros():
    def agregar(self, id, titulo, genero, isbn, editorial, autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autores = autores
        libro = {}
        libro['id'] = self.id
        libro['titulo'] = self.titulo
        libro['genero'] = self.genero
        libro['isbn'] = self.isbn
        libro['editorial'] = self.editorial
        libro['autores'] = self.autores
        libros.append(libro)
        print('=================================AGREGADO==============================')

class eliminar_libros():
    def eliminar(self, titulo):
        self.titulo = titulo
        for e in libros:
            if e["titulo"] == self.titulo:
                libros.remove(e)
        print('================================ELIMINADO=============================')

class buscar_libros():
    def buscar(self, valor):
        self.valor = valor
        print('========================RESULTADO DE BUSQUEDA==========================')
        for e in libros:
            if e["titulo"] == self.valor or e["isbn"] == self.valor:
                print(e)
        print('=======================================================================')

class ordenar_libros():
    def ordenar(self):
        ordenado = sorted(libros, key=lambda k: k['titulo'])
        print('========================LISTA ORDENADA==========================')
        for cont, i in enumerate(ordenado):
            print(f'{cont} - {i}')
        print('=======================================================================')




