from grafo import Graph
from heap import HeapMin
from pila import Stack

grafo = Graph(dirigido=False)

grafo.insert_vertice("Luke Skywalker")
grafo.insert_vertice("Leia Organa")
grafo.insert_vertice("Han Solo")
grafo.insert_vertice("Darth Vader")
grafo.insert_vertice("Emperor Palpatine")
grafo.insert_vertice("Chewbacca")
grafo.insert_vertice("Yoda")
grafo.insert_vertice("Rey")
grafo.insert_vertice("Kylo Ren")
grafo.insert_vertice("Boba Fett")
grafo.insert_vertice("C3PO")
grafo.insert_vertice("BB8")

grafo.insert_arista("Luke Skywalker", "Leia Organa", 3)
grafo.insert_arista("Luke Skywalker", "Han Solo", 3)
grafo.insert_arista("Leia Organa", "Han Solo", 3)
grafo.insert_arista("Leia Organa", "Darth Vader", 2)
grafo.insert_arista("Han Solo", "Chewbacca", 4)
grafo.insert_arista("Darth Vader", "Emperor Palpatine", 3)
grafo.insert_arista("Chewbacca", "Yoda", 1)
grafo.insert_arista("Yoda", "Luke Skywalker", 2)
grafo.insert_arista("Rey", "Luke Skywalker", 3)
grafo.insert_arista("Rey", "Kylo Ren", 3)
grafo.insert_arista("Boba Fett", "Han Solo", 3)
grafo.insert_arista("Kylo Ren", "Darth Vader", 2)
grafo.insert_arista("C3PO", "Yoda", 1)
grafo.insert_arista("BB8", "Rey", 1)

arbol_expansion_min = grafo.kruskal("BB-8")
print()
def mostrar_arbol_expansion(arbol):    
    for arista in arbol[0].split(';'):
        origen, destino, peso = arista.split('-')
        print(f"origen: {origen} -> destino: {destino} -> metros: {peso}")

mostrar_arbol_expansion(arbol_expansion_min)

def contiene_a(arbol, key):
    for arista in arbol[0].split(';'):
        origen, destino, peso = arista.split('-')
        if origen == key or destino == key:
            return True
    return False

print()
yoda = "Yoda"
print()
if contiene_a(arbol_expansion_min, yoda):
    print(f"{yoda} está en el árbol de expansión mínima")

print()
max_peso, max_vertices = grafo.get_max_arista()
print(f"El vértice con el peso máximo es {max_vertices} con un peso de {max_peso}")