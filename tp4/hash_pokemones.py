from lista import show_list_list

pokemons = [
    {   
        "numero": 25,
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "numero": 25,
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "numero": 6,
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "numero": 3,
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "numero": 121,
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "numero": 54,
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "numero": 130,
        "nombre": "Gyarados",
        "nivel": 36,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "numero": 95,
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "numero": 74,
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "numero": 37,
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "numero": 9,
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "numero": 197,
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "numero": 34,
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "numero": 74,
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "numero": 142,
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    }
]

""" Ejercicio A, B y C"""
def hash_tipo(pokemon):
    return pokemon['tipo']

def hash_numero(pokemon):
    return pokemon['numero']%10

def hash_nivel(pokemon):
    return pokemon['nivel']%10

tabla_por_tipo = {}
tabla_por_numeros = {}
tabla_por_nivel = {}

for pokemon in pokemons:
    clave = hash_tipo(pokemon)
    if clave not in tabla_por_tipo:
        tabla_por_tipo[clave] = []
    tabla_por_tipo[clave].append(pokemon)

    clave = hash_numero(pokemon)
    if clave not in tabla_por_numeros:
        tabla_por_numeros[clave] = []
    tabla_por_numeros[clave].append(pokemon)

    clave = hash_nivel(pokemon)
    if clave not in tabla_por_nivel:
        tabla_por_nivel[clave] = []
    tabla_por_nivel[clave].append(pokemon)

def mostrar_pokemones(lista_hash, title):
    print('----------------------------------------------------------------')
    print(title)
    print("")
    for index, pokemon in enumerate(lista_hash):
        p = pokemon
        print(f"{index+1}) Informacion del pokemon {p['nombre']}:")
        print(f"            -Numero: {p['numero']}")
        print(f"            -Nivel: {p['nivel']}")
        print(f"            -Tipo: {p['tipo']}")
        print(f"            -Subtipo: {p['subtipo']}")
        print('----------------------------------------------------------------')

""" Ejercicio D"""
def cargar_pokemon(numero, nombre, nivel, tipo, subtipo):
    pokemon = { "numero": numero,
                "nombre": nombre,
                "nivel": nivel,
                "tipo": tipo,
                "subtipo": subtipo}
    
    pokemons.append(pokemon)
    
    clave = hash_tipo(pokemon)
    if clave not in tabla_por_tipo:
        tabla_por_tipo[clave] = []
    tabla_por_tipo[clave].append(pokemon)

    clave = hash_numero(pokemon)
    if clave not in tabla_por_numeros:
        tabla_por_numeros[clave] = []
    tabla_por_numeros[clave].append(pokemon)

    clave = hash_nivel(pokemon)
    if clave not in tabla_por_nivel:
        tabla_por_nivel[clave] = []
    tabla_por_nivel[clave].append(pokemon)

cargar_pokemon(9, "Blastoise", 45, "Agua", None)


""" Ejercicio E"""
def pokemones_terminan_en(numero):
    terminan_en = tabla_por_numeros.get(numero)
    if terminan_en is not None:
        mostrar_pokemones(terminan_en, f'Pokemones que terminan en {numero}')

# pokemones_terminan_en(3)
# pokemones_terminan_en(7)
# pokemones_terminan_en(9)


""" Ejercicio F"""
def pokemones_nivel_multiplo(multiplo):
    for nivel in tabla_por_nivel:
        if (nivel%multiplo == 0):
            mostrar_pokemones(tabla_por_nivel[nivel], f'Pokemones con nivel multiplo de {multiplo}')
            
# pokemones_nivel_multiplo(5)
# pokemones_nivel_multiplo(2)
# pokemones_nivel_multiplo(10)

""" Ejercicio G"""        
def pokemones_de_tipo(tipo):
    if tipo in tabla_por_tipo:
        mostrar_pokemones(tabla_por_tipo[tipo], f'Pokemones de tipo {tipo}')
    else:
        print(f'No hay pokemones de tipo {tipo}')


# pokemones_de_tipo('Fuego')
# pokemones_de_tipo('Acero')
# pokemones_de_tipo('Eléctrico')
# pokemones_de_tipo('Hielo')


