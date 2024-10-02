super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad.",
    "villano": False
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men.",
    "villano": False
  },
  {
    "nombre": "Doctor Straje",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad.",
    "villano": False
  },
  {
    "nombre": "Joker",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Archienemigo de Batman, un genio del crimen con un sentido del humor retorcido.",
    "villano": True
  },
  {
    "nombre": "Thanos",
    "año_aparicion": 1973,
    "casa_comic": "Marvel Comics",
    "biografia": "Titán loco que busca la aniquilación de la mitad del universo usando las Gemas del Infinito.",
    "villano": True
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Estudiante que, tras ser mordido por una araña radiactiva, obtiene poderes sobrehumanos y protege Nueva York como Spider-Man.",
    "villano": False
  },
  {
    "nombre": "Lex Luthor",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Magnate multimillonario y brillante científico, enemigo acérrimo de Superman.",
    "villano": True
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "Bruce Wayne, un multimillonario que lucha contra el crimen en Gotham City usando su intelecto, habilidades marciales y tecnología avanzada.",
    "villano": False
  },
  {
    "nombre": "Captain America",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "Steve Rogers fue transformado en el súper soldado Captain America para luchar contra las fuerzas del mal durante la Segunda Guerra Mundial. Con su escudo indestructible y su inquebrantable sentido del deber, se convirtió en un símbolo de justicia y libertad.",
    "villano": False
  },
  {
    "nombre": "Magneto",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante maestro del magnetismo, defensor de la supremacía mutante y líder de los mutantes rebeldes.",
    "villano": True
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa guerrera de las Amazonas, defensora de la paz y la justicia en el mundo humano.",
    "villano": False
  },
  {
    "nombre": "Venom",
    "año_aparicion": 1984,
    "casa_comic": "Marvel Comics",
    "biografia": "Un simbionte alienígena que se fusiona con Eddie Brock, formando un antihéroe con habilidades similares a Spider-Man.",
    "villano": True
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "El hombre más rápido del mundo, usando su supervelocidad para combatir el crimen y proteger Central City.",
    "villano": False
  },
  {
    "nombre": "Green Goblin",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Norman Osborn, un industrial y científico loco que utiliza la tecnología para convertirse en el enemigo más peligroso de Spider-Man.",
    "villano": True
  },
  {
    "nombre": "Black Panther",
    "año_aparicion": 1966,
    "casa_comic": "Marvel Comics",
    "biografia": "T'Challa, rey de Wakanda, defensor de su nación y portador de poderes sobrehumanos otorgados por la hierba corazón.",
    "villano": False
  },
  {
    "nombre": "Harley Quinn",
    "año_aparicion": 1992,
    "casa_comic": "DC Comics",
    "biografia": "Ex psiquiatra del Asilo Arkham convertida en la compañera y cómplice del Joker.",
    "villano": True
  }
]

from tp_arbol import BinaryTree

tree_heroes = BinaryTree()

for personaje in super_heroes:
    tree_heroes.insert_node(personaje["nombre"], personaje)



""" Ordena los heroes en orden alfabético"""
print('------------------------------------------------')
print(' Lista de villanos ordenados alfabéticamente: ')
tree_heroes.inorden_villanos()
print('------------------------------------------------')


""" Mostrar heroes que empiecen con 'c'"""
print(' Lista de heroes que empiezan con "C": ')
tree_heroes.inorden_heroes_startswith('C')
print('------------------------------------------------')


""" Contar cuántos heroes hay en el arbol"""
print(' Cantidad de heroes dentro del arbol: ')
cantidad_de_heroes = tree_heroes.count_heroes()
print(cantidad_de_heroes)
print('------------------------------------------------')

""" Buscar por proximidada a Doctor Strange"""
tree_heroes.proximity_search('Doctor')

value_to_delete = 'Doctor Straje'
delete_value, extra_info = tree_heroes.delete_node_with_values(value_to_delete)
print('eliminado', delete_value, extra_info)
new_name = 'Doctor Strange'
extra_info['nombre'] = new_name
tree_heroes.insert_node(new_name, extra_info)
print()
print('Heroe corregido: ', new_name)
pos = tree_heroes.search('Doctor Strange')
if pos:
    print('encontrado', pos.other_value)

print()
tree_heroes.proximity_search('La')
print('------------------------------------------------')

""" Mostrar heroes de manera descentes"""
print(' Heroes de manera descendente: ')
tree_heroes.postorden_heroes()
print('------------------------------------------------')

""" Agregar un nuevo heroe en un arbol y los villanos en el otro """
tree_heroes_heroes = BinaryTree()
tree_heroes_villanos = BinaryTree()

for personaje in super_heroes:
    if personaje["villano"]:
        tree_heroes_villanos.insert_node(personaje["nombre"], personaje["villano"])
    else:
        tree_heroes_heroes.insert_node(personaje["nombre"], personaje["villano"])


""" Mostrar cantidad de nodos en los arboles de heroes y villanos"""
print(' cantidad de nodos en el arbol tree_heroes_heroes: ')
print(tree_heroes_heroes.count())
print('------------------------------------------------')

print(' cantidad de nodos en el arbol tree_heroes_villanos: ')
print(tree_heroes_villanos.count())
print('------------------------------------------------')

""" Barrido en orden alfabetico de los arboles"""
print(' HEROES: ')
tree_heroes_heroes.inorden()
print('------------------------------------------------')

print(' VILLANOS: ')
tree_heroes_villanos.inorden()
print('------------------------------------------------')