
from lista import show_list_list, search

entrenadores = [
    {"nombre": "Ash", "torneos_ganados": 10, "batallas_perdidas": 20, "batallas_ganadas": 100},
    {"nombre": "Misty", "torneos_ganados": 5, "batallas_perdidas": 35, "batallas_ganadas": 80},
    {"nombre": "Brock", "torneos_ganados": 8, "batallas_perdidas": 40, "batallas_ganadas": 90},
    {"nombre": "Gary", "torneos_ganados": 15, "batallas_perdidas": 5, "batallas_ganadas": 120},
    {"nombre": "May", "torneos_ganados": 12, "batallas_perdidas": 18, "batallas_ganadas": 95},
    {"nombre": "Dawn", "torneos_ganados": 7, "batallas_perdidas": 52, "batallas_ganadas": 85},

]

# Definimos los Pokémon de los primeros 12 entrenadores
pokemones = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Psyduck",
        "nivel": 64,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": "Planta",
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None,
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None,
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Tyrantrum",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
]

lista_entrenadores = []
#Meter la lista de entrenadores_pokemon dentro de la lista de pokemones_entrenadores
for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for entrenador in lista_entrenadores:
    for pokemon in pokemones:
        entrenador['sublist'].append(pokemon)

#Punto A
def cantidad_pokemones_de(entrenador):
    index_entrenador = search(entrenadores, "nombre", entrenador)
    return len(lista_entrenadores[index_entrenador]['sublist'])

#Punto B
def entrenadores_con_mas_de_x_torneos(cant_torneos):
    for entrenador in lista_entrenadores:
        if entrenador['torneos_ganados'] > cant_torneos:
            print(entrenador['nombre'])

#Punto C
def mayor_nivel_pokemon_ent_ganador():
    ganador = None;
    pokemon_mayor_nivel = None;
    for entrenador in lista_entrenadores:
        if not ganador:
            ganador = entrenador
        if entrenador['torneos_ganados'] > ganador['torneos_ganados']:
            ganador = entrenador

    for pokemon in ganador['sublist']:
        if not pokemon_mayor_nivel:
            pokemon_mayor_nivel = pokemon
        if pokemon['nivel'] > pokemon_mayor_nivel['nivel']:
            pokemon_mayor_nivel = pokemon

    print(f"* Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados: ")
    print(f"---------{pokemon_mayor_nivel['nombre']} del entrenador {ganador['nombre']}")

#Punto D
def mostrar_informacion_entrenador(nombre_entrenador):
    indexEntrenador = search(entrenadores, "nombre", nombre_entrenador)
    if indexEntrenador is not None:
        e = entrenadores[indexEntrenador]
        print(f"Informacion del entrenador {nombre_entrenador}:")
        print(f"    -Torneos ganados: {e['torneos_ganados']}")
        print(f"    -Batallas perdidas: {e['batallas_perdidas']}")
        print(f"    -Batallas ganadas: {e['batallas_ganadas']}")
        for pokemon in e['sublist']:
            print(f"        -{pokemon['nombre']}")
            print(f"            -Nivel: {pokemon['nivel']}")
            print(f"            -Tipo: {pokemon['tipo']}")
            print(f"            -Subtipo: {pokemon['subtipo']}")

#Punto E
def entrenadores_winrate_mayor_79():
    for entrenador in lista_entrenadores:
        total_batallas = entrenador['batallas_ganadas'] + entrenador['batallas_perdidas']
        winrate = (entrenador['batallas_ganadas'] * 100) / total_batallas
        if winrate > 79:
            print(entrenador['nombre'])

#Putno F
def entrenadores_con_pokemones(tipo, subtipo):
    for entrenador in lista_entrenadores:
        for pokemon in entrenador['sublist']:
            if pokemon['tipo'] == tipo and pokemon['subtipo'] == subtipo:
                print(f"---{entrenador['nombre']} con pokemon {pokemon['nombre']} de tipo {pokemon['tipo']} y {pokemon['subtipo']} ")

#Punto G
def promedio_nivel_pokemones_de(entrenador):
    index_entrenador = search(entrenadores, "nombre", entrenador)
    total_nivel = 0
    for pokemon in lista_entrenadores[index_entrenador]['sublist']:
        total_nivel += pokemon['nivel']
    print(f"El promedio de nivel de los pokemones del entrenador {entrenador} es {total_nivel / len(lista_entrenadores[index_entrenador]['sublist'])}")

#Pungo H
def cuantos_entrenadores_tienen_a(pokemon):
    contador = 0
    for entrenador in lista_entrenadores:
        for pokemon_entrenador in entrenador['sublist']:
            if pokemon_entrenador['nombre'] == pokemon:
                contador += 1
    print(f"La cantidad de entrenadores que tienen a {pokemon} es de {contador}")

#Punto I
def pokemones_repetidos_de(entrenador):
    nombre_pokemons = []
    pokemons_repetidos = []

    index_entrenador = search(entrenadores, "nombre", entrenador)

    for pokemon in lista_entrenadores[index_entrenador]['sublist']:
        nombre_pokemons.append(pokemon['nombre'])

    for nombre in nombre_pokemons:
        contador = nombre_pokemons.count(nombre)
        if contador > 1 and search(pokemons_repetidos, 'nombre', nombre) == None:
            pokemons_repetidos.append({'nombre': nombre, 'contador': contador})
            print(f"{entrenador} tiene repetido a {nombre} {contador} veces")

#Punto J 
"""Todavia no esta termindado"""
def buscar_entrenador_y_pokemon(entrenador, pokemon):
    indexEntrenador = search(entrenadores, "nombre", entrenador)
    indexPokemon = search(lista_entrenadores[indexEntrenador]['sublist'], "nombre", pokemon)
    return indexEntrenador, indexPokemon

pokemons_TTW = []
for entrenador in entrenadores:
    indexPokemonTy = search(entrenador['sublist'], "nombre", "Tyrantrum")
    indexPokemonTe = search(entrenador['sublist'], "nombre", "Terrakion")
    indexPokemonWi = search(entrenador['sublist'], "nombre", "Wingull")
    if indexPokemonWi != -1 or indexPokemonTe != -1 or indexPokemonTe != -1:
        print(f"El entrenador {entrenador['nombre']} t")

#Punto K
def mostrar_entrenador_y_pokemon(entrenador, pokemon):
    indexEntrenador = search(entrenadores, "nombre", entrenador)
    indexPokemon = search(lista_entrenadores[indexEntrenador]['sublist'], "nombre", pokemon)
    if indexEntrenador is not None and indexPokemon is not None:
        e = entrenadores[indexEntrenador]
        p = e['sublist'][indexPokemon]
        print(f"Informacion del entrenador {e['nombre']}:")
        print(f"    -Torneos ganados: {e['torneos_ganados']}")
        print(f"    -Batallas perdidas: {e['batallas_perdidas']}")
        print(f"    -Batallas ganadas: {e['batallas_ganadas']}")

        print(f"Informacion del pokemon {p['nombre']}:")
        print(f"        -{p['nombre']}")
        print(f"            -Nivel: {p['nivel']}")
        print(f"            -Tipo: {p['tipo']}")
        print(f"            -Subtipo: {p['subtipo']}")

#show_list_list("entrenador", "pokemones", lista_entrenadores)
#print(cantidad_pokemones_de("Ash"))
#entrenadores_con_mas_de_x_torneos(8)
#mayor_nivel_pokemon_ent_ganador()
#mostrar_informacion_entrenador("Ash")
#entrenadores_winrate_mayor_79()
#entrenadores_con_pokemones("Fuego", "Planta")
print()
#entrenadores_con_pokemones("Agua", "Volador")
#promedio_nivel_pokemones_de("Ash")
#cuantos_entrenadores_tienen_a("Onix")
#mostrar_entrenador_y_pokemon("Ash", "Vulpix")
#pokemones_repetidos_de("Ash")

  
#buscar_pokemon(pokemon)