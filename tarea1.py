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
class buscar_autores_editorial_genero():
    def buscar_aeg(self, por):
        self.por = por
        if self.por == 1:
            autor = input("buscar por autor: ")
            print('========================RESULTADO DE BUSQUEDA==========================')
            for cont, e in enumerate(libros):
                auto = tuple(e['autores'])
                for i in auto:
                    if i == autor:
                        print(f'{cont} - {e}')
            print('=======================================================================')
        if self.por == 2:
            editorial = input("buscar por editorial: ")
            print('========================RESULTADO DE BUSQUEDA==========================')
            for cont, e in enumerate(libros):
                if e['editorial'] == editorial:
                    print(f'{cont} - {e}')
            print('=======================================================================')
        if self.por == 3:
            genero = input("buscar por genero: ")
            print('========================RESULTADO DE BUSQUEDA==========================')
            for cont, e in enumerate(libros):
                if e['genero'] == genero:
                    print(f'{cont} - {e}')
            print('=======================================================================')

class buscar_numero_autores():
    def buscar_na(self, n_autor):
        self.n_autor = n_autor
        print('========================RESULTADO DE BUSQUEDA==========================')
        for cont, e in enumerate(libros):
            auto = tuple(e['autores'])
            if len(auto) == self.n_autor:
                print(f'{cont} - {e}')
        print('=======================================================================')

class actializar_libros():
    def actualizar(self, num):
        self.num = num
        id = int(input('id: '))
        titulo = input('titulo: ')
        genero = input('genero: ')
        isbn = input('isbn: ')
        editorial = input('editorial: ')
        autores = []
        numero_autores = int(input('numero de autores: '))
        for i in range(1, numero_autores + 1):
            autor = input(f'autor {i}: ')
            autores.append(autor)
        dic = libros[self.num]
        dic.update(
            {'id': id, 'titulo': titulo, 'genero': genero, 'isbn': isbn, 'editorial': editorial, 'autores': autores})
        print('=============================ACTUALIZADO==============================')
        for cont, i in enumerate(libros):
            if cont == nun:
                print(f'{cont} - actualizado - {i}')
            else:
                print(f'{cont} - {i}')
        print('=======================================================================')

class guardar_libro():
    def guardar(self):
        with open("libros.txt", "wb") as f:
            pickle.dump(libros, f)
            print('====================GUARDADO COMO libros.txt=======================')


while True:
    opcion = int(input('\nIngrese 0 para ver opciones.\nDe lo contrario ingrese una opcion: '))
    if opcion == 0:
        op = mostrar_opciones()
        op.Opciones()
    if opcion == 1:
        lel = leer_libro()
        lel.leer()
    if opcion == 2:
        mo = mostrar_libros()
        mo.mostrar(libros)
    if opcion == 3:
        id = int(input('id: '))
        titulo = input('titulo: ')
        genero = input('genero: ')
        isbn = input('isbn: ')
        editorial = input('editorial: ')
        autores = []
        numero_autores = int(input('numero de autores: '))
        for i in range(1, numero_autores + 1):
            autor = input(f'autor {i}: ')
            autores.append(autor)
        agr = agregar_libros()
        agr.agregar(id, titulo, genero, isbn, editorial, autores)
    if opcion == 4:
        titulo = input("eliminar titulo: ")
        eli = eliminar_libros()
        eli.eliminar(titulo)
    if opcion == 5:
        titulo = input("buscar titulo: ")
        bus = buscar_libros()
        bus.buscar(titulo)
    if opcion == 6:
        ord = ordenar_libros()
        ord.ordenar()
    if opcion == 7:
        print('buscar libro por:')
        print('Opción 1: Busqueda por autor')
        print('Opción 2: Busqueda por editorial')
        print('Opción 3: Busqueda por genero')
        por = int(input('Escoja la opcion a buscar: '))
        baeg = buscar_autores_editorial_genero()
        baeg.buscar_aeg(por)
    if opcion == 8:
        n_autor = int(input("Busqueda por numero de autores: "))
        bna = buscar_numero_autores()
        bna.buscar_na(n_autor)
    if opcion == 9:
        print('Seleccione el numero a actualizar')
        for cont, i in enumerate(libros):
            print(f'{cont} - {i}')
        nun = int(input('Ingrese un numero: '))
        acl = actializar_libros()
        acl.actualizar(nun)
    if opcion == 10:
        gul = guardar_libro()
        gul.guardar()
    else:
        print('GAME OVER :)')
        break
