cola_personajes_mcu = ([
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre": "Thor Odinson", "superheroe": "Thor", "genero": "M"},
    {"nombre": "Bruce Banner", "superheroe": "Hulk", "genero": "M"},
    {"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre": "T'Challa", "superheroe": "Black Panther", "genero": "M"},
    {"nombre": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
    {"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
    {"nombre": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"}
])

from colaMCU import Queue

cola_mcu = Queue()

for personaje in cola_personajes_mcu:
    cola_mcu.arrive(personaje)

def show_elements():
    print("Personajes en la cola:")
    for i in range(cola_mcu.size()):
        print(cola_mcu.on_front())
        cola_mcu.move_to_end()

show_elements()

"""Mostrar nombre del superheroe Capitana Marvel"""
print()
for i in range(cola_mcu.size()):
    personaje = cola_mcu.on_front()
    if personaje["superheroe"] == "Capitana Marvel" :
        print("Nombre de la Capitana Marvel, ", personaje["nombre"])
    cola_mcu.move_to_end()

"""Mostrar los personajes del planeta Alderaan, Endor y Tatooine"""
print()
print("Personajes del genero Femenino:")
for i in range(cola_mcu.size()):
    personaje = cola_mcu.on_front()
    if personaje["genero"] in "F":
        print(personaje["superheroe"], "--> Nombre: ", personaje["nombre"])
    cola_mcu.move_to_end()

"""Mostrar los personajes del planeta Alderaan, Endor y Tatooine"""
print()
print("Personajes del genero Masculino:")
for i in range(cola_mcu.size()):
    personaje = cola_mcu.on_front()
    if personaje["genero"] in "M":
        print(personaje["superheroe"], "--> Nombre: ", personaje["nombre"])
    cola_mcu.move_to_end()

"""Mostrar nombre del superheroe Capitana Marvel"""
print()
for i in range(cola_mcu.size()):
    personaje = cola_mcu.on_front()
    if personaje["nombre"] == "Scott Lang" :
        print("Nombre de superheroe de Scott Lang, ", personaje["superheroe"])
    cola_mcu.move_to_end()

"""mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S"""
print()
print("Personajes Que su nombre empieza con S:")
for i in range(cola_mcu.size()):
    personaje = cola_mcu.on_front()
    if personaje["nombre"].startswith("S"):
        print("Superheroe: ", personaje["superheroe"], "--> ", personaje["nombre"])
    cola_mcu.move_to_end()

"""determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes."""
print()
for i in range(cola_mcu.size()):
    personaje = cola_mcu.on_front()
    if personaje["nombre"] == "Carol Danvers" :
        carolDanvers = personaje
    cola_mcu.move_to_end()

if carolDanvers is not None:
    print("Carol Danvers se encuentra en la cola. Su superheroe es: ", personaje["superheroe"])
else:
    print("Carol Danvers no se encuentra en la cola.")