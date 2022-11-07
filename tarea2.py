import requests

opcion = int(input('opcion: '))

if opcion == 1:
    generacion = input('generacion: ')
    peticion1 = requests.get(f"https://pokeapi.co/api/v2/generation/{generacion}")
    datos1 = peticion1.json()
    lista_de_pokemon = [pokemon["name"] for pokemon in datos1["pokemon_species"]]
    for i in lista_de_pokemon:
        peticion2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}?limit=1323&offset=0")
        datos2 = peticion2.json()
        pokemon = i
        habilidad = [habilidad["ability"]["name"] for habilidad in datos2["abilities"]]
        url = [url["ability"]["url"] for url in datos2["abilities"]]
        print('====================================')
        print('Pokemon:   ', pokemon)
        print('Habilidad: ', habilidad)
        print('Url:       ', url)

if opcion == 2:
    peticion1 = requests.get(f"https://pokeapi.co/api/v2/pokemon-form?limit=1323&offset=0")
    datos1 = peticion1.json()
    lista_de_forma = [forma["name"] for forma in datos1["results"]]
    print(f'escoja una forma de pokemon: {lista_de_forma}')
    forma = input('Ingrese forma: ')
    peticion2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{forma}")
    datos2 = peticion2.json()
    lista_de_form = [pokemon["name"] for pokemon in datos2["forms"]]
    for i in lista_de_form:
        habilidad = [habilidad["ability"]["name"] for habilidad in datos2["abilities"]]
        url = [url["ability"]["url"] for url in datos2["abilities"]]
        print('====================================')
        print('Pokemon:   ', i)
        print('Habilidad: ', habilidad)
        print('Url:       ', url)

if opcion == 3:
    peticion1 = requests.get(f"https://pokeapi.co/api/v2/ability?limit=327&offset=0")
    datos1 = peticion1.json()
    lista_de_forma = [forma["name"] for forma in datos1["results"]]
    print(f'escoja una abulidad de pokemon: {lista_de_forma}')
    habilidad_ingresado = input('Ingrese abilidad: ')
    peticion2 = requests.get(f"https://pokeapi.co/api/v2/ability/{habilidad_ingresado}?limit=1323&offset=0")
    datos2 = peticion2.json()
    lista_de_pokemon = [forma["pokemon"]["name"] for forma in datos2["pokemon"]]
    for i in lista_de_pokemon:
        peticion3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}?limit=1323&offset=0")
        datos3 = peticion3.json()
        pokemon = i
        habilidad = [habilidad["ability"]["name"] for habilidad in datos3["abilities"]]
        url = [habilidad["ability"]["url"] for habilidad in datos3["abilities"]]
        for e in habilidad:
            if habilidad_ingresado == e:
                print('pokemon:',i)
                print('habilidad: ', habilidad)
                print('url: ', url)

if opcion == 4:
    peticion1 = requests.get(f"https://pokeapi.co/api/v2/pokemon-habitat?limit=9&offset=0")
    datos1 = peticion1.json()
    lista_de_forma = [forma["name"] for forma in datos1["results"]]
    print(f'escoja una habitat de pokemon: {lista_de_forma}')
    habitat_ingresado = input('Ingrese abilidad: ')
    peticion2 = requests.get(f"https://pokeapi.co/api/v2/pokemon-habitat/{habitat_ingresado}?limit=1323&offset=0")
    datos2 = peticion2.json()
    lista_de_pokemon = [forma["name"] for forma in datos2["pokemon_species"]]
    for i in lista_de_pokemon:
        peticion3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}?limit=1323&offset=0")
        datos3 = peticion3.json()
        pokemon = i
        habilidad = [habilidad["ability"]["name"] for habilidad in datos3["abilities"]]
        url = [url["ability"]["url"] for url in datos3["abilities"]]
        print('====================================')
        print('Pokemon:   ', pokemon)
        print('Habilidad: ', habilidad)
        print('Url:       ', url)

if opcion == 5:
    peticion1 = requests.get(f"https://pokeapi.co/api/v2/type?limit=20&offset=0")
    datos1 = peticion1.json()
    lista_de_forma = [forma["name"] for forma in datos1["results"]]
    print(f'escoja un tipo de pokemon: {lista_de_forma}')
    tipo_ingresado = input('Ingrese tipo: ')
    peticion2 = requests.get(f"https://pokeapi.co/api/v2/type/{tipo_ingresado}?limit=1323&offset=0")
    datos2 = peticion2.json()
    lista_de_pokemon = [forma["pokemon"]["name"] for forma in datos2["pokemon"]]
    for i in lista_de_pokemon:
        peticion3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}?limit=1323&offset=0")
        datos3 = peticion3.json()
        pokemon = i
        habilidad = [habilidad["ability"]["name"] for habilidad in datos3["abilities"]]
        url = [url["ability"]["url"] for url in datos3["abilities"]]
        print('====================================')
        print('Pokemon:   ', pokemon)
        print('Habilidad: ', habilidad)
        print('Url:       ', url)



