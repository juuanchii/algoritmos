from colaST import Queue

cola_star_wars = Queue()

cola_star_wars.arrive("Luke Skywalker", "Tatooine")
cola_star_wars.arrive("Leia Organa", "Alderaan")
cola_star_wars.arrive("Jar Jar Binks", "Naboo")
cola_star_wars.arrive("Darth Vader", "Tatooine")
cola_star_wars.arrive("Yoda", "Dagobah")
cola_star_wars.arrive("Wicket Warrick", "Endor")
cola_star_wars.arrive("Han Solo", "Corellia")

def show_elements():
    print("Personajes en la cola:")
    for i in range(cola_star_wars.size()):
        print(cola_star_wars.on_front()["nombre"])
        cola_star_wars.move_to_end()

"""Mostrar los personajes del planeta Alderaan, Endor y Tatooine"""
print()
for i in range(cola_star_wars.size()):
    personaje = cola_star_wars.on_front()
    if personaje["planeta"] in ["Alderaan", "Endor", "Tatooine"]:
        print(personaje["nombre"], "--> Planeta: ", personaje["planeta"])
    cola_star_wars.move_to_end()

"""Mostrar los planetas de Luke Skywalker y Han Solo"""
def show_planet(name):
    for i in range(cola_star_wars.size()):
        personaje = cola_star_wars.on_front()
        if personaje["nombre"] == name:
            print(personaje["nombre"], "--> Planeta: ", personaje["planeta"])
        cola_star_wars.move_to_end()

print()
print("Planetas de Luke Skywalker y Han Solo:")
show_planet("Luke Skywalker")
show_planet("Han Solo")

"""Insertar un nuevo personaje antes del maestro Yoda"""
nuevo_personaje = {"nombre": "Obi-Wan Kenobi", "planeta": "Dagobah"}
for i in range(cola_star_wars.size()):
    if personaje["nombre"] == "Yoda":
        cola_star_wars.arrive(nuevo_personaje["nombre"], nuevo_personaje["planeta"])
        break
    personaje = cola_star_wars.on_front()

print()
show_elements()

"""Eliminar el personaje despues de Jar Jar Binks"""
for i in range(cola_star_wars.size()):
    personaje = cola_star_wars.on_front()
    if personaje["nombre"] == "Jar Jar Binks":
        cola_star_wars.move_to_end()
        cola_star_wars.attention()
    cola_star_wars.move_to_end()


print()
show_elements()