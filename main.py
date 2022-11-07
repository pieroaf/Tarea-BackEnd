libros = []

while True:
    opcion = int(input('que opcion: '))
    if opcion == 1:
        print('falta')
    if opcion == 2:
        for cont, i in enumerate(libros):
            print(f'{cont} - {i}')
    if opcion == 3:
        id = int(input('id: '))
        titulo = input('titulo: ')
        autores = []
        numero_autores = int(input('numero de autores: '))
        for i in range(1, numero_autores + 1):
            autor = input(f'autor {i}: ')
            autores.append(autor)
        libro = {}
        libro['id'] = id
        libro['titulo'] = titulo
        libro['autores'] = autores
        libros.append(libro)
    if opcion == 4:
        titulo = input("eliminar titulo: ")
        for e in libros:
            if e["titulo"] == titulo:
                libros.remove(e)
    if opcion == 5:
        titulo = input("buscar titulo: ")
        for e in libros:
            if e["titulo"] == titulo:
                print(libros)
    if opcion == 6:
        print('falta')




