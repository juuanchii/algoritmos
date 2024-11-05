pokemons = [
    {"nombre": "Pikachu", "numero": 25, "tipo": ["Eléctrico"]},
    {"nombre": "Charmander", "numero": 4, "tipo": ["Fuego"]},
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Planta", "Veneno"]},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["Agua"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["Eléctrico"]},
    {"nombre": "Vaporeon", "numero": 134, "tipo": ["Agua"]},
    {"nombre": "Flareon", "numero": 136, "tipo": ["Fuego"]},
    {"nombre": "Chikorita", "numero": 152, "tipo": ["Planta"]},
    {"nombre": "Torchic", "numero": 255, "tipo": ["Fuego"]},
    {"nombre": "Mudkip", "numero": 258, "tipo": ["Agua"]},
    {"nombre": "Treecko", "numero": 252, "tipo": ["Planta"]},
    {"nombre": "Magnemite", "numero": 81, "tipo": ["Eléctrico", "Acero"]},
    {"nombre": "Electabuzz", "numero": 125, "tipo": ["Eléctrico"]},
    {"nombre": "Poliwag", "numero": 60, "tipo": ["Agua"]},
    {"nombre": "Litten", "numero": 725, "tipo": ["Fuego"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["Roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": ["Roca", "Dragón"]}
]


from arbol_avl import BinaryTree

tree_by_nombre = BinaryTree()
tree_by_numero = BinaryTree()
tree_by_tipo = BinaryTree()

for pokemon in pokemons:
    tree_by_nombre.insert_node(pokemon["nombre"], pokemon)
    tree_by_numero.insert_node(pokemon["numero"], pokemon)
    tree_by_tipo.insert_node(pokemon["tipo"][0], pokemon)

print()
"""Hago una busqueda por proximidad con los caracteres 'Bul' y despues busco con exactitud con el numero de pokemon que me devuelve la busqueda por proximidad"""
tree_by_nombre.proximity_search_pokemons("Bul")
datos_pokemon_1 = tree_by_numero.search(1)
print(f"Datos del pokemon con numero 1: {datos_pokemon_1.other_value}")

print()
print("Pokemones ordenados segun su tipo:")
print()
tree_by_nombre.inorden_por_tipo("Fuego")
print()
tree_by_nombre.inorden_por_tipo("Agua")
print()
tree_by_nombre.inorden_por_tipo("Planta")
print()
tree_by_nombre.inorden_por_tipo("Eléctrico")

"""Listado pokemones por nombre de manera ascendente"""
print()
print("Listado pokemones por nombre de manera ascendente")
tree_by_nombre.inorden_data_pokemons()
print()
"""Listado pokemones por numero de manera ascendente"""
print("--------------------------------")
print("Listado pokemones por numero de manera ascendente")
tree_by_numero.inorden_data_pokemons()

"""Listado pokemones por nivel por nombre"""
print()
print("--------------------------------")
print("Listado pokemones por nivel por nombre")
tree_by_nombre.by_level()
print()


"""Busco un pokemon por nombre y muestro sus datos"""
print("Busco un pokemon por nombre y muestro sus datos")

buscados = ['Jolteon', 'Lycanroc', 'Tyrantrum']
for pokemon in buscados:
    jolteon = tree_by_nombre.search(pokemon)

    if jolteon is not None:
        print("--------------------------------")
        print(f"        Numero: {jolteon.other_value['numero']}")
        print(f"        Nombre: {jolteon.other_value['nombre']}")
        print(f"        Tipo: {jolteon.other_value['tipo']}")
    else:
        print()
        print(f"No se encontro el pokemon {pokemon}")

print("--------------------------------")
print(f"Cantidad de pokemones de tripo electrico {tree_by_tipo.contar_tipo("Eléctrico")}")
print("--------------------------------")
print(f"Cantidad de pokemones de tripo Acero {tree_by_tipo.contar_tipo("Acero")}")
