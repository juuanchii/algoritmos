from grafo import Graph


grafo = Graph(dirigido=False)

# Definimos los vertices
ambientes = ['cocina', 'cochera', 'quincho', 'baño1', 'baño2', 'habitacion1', 'habitacion2', 'sala de estar', 'terraza', 'patio']

for ambiente in ambientes:
    grafo.insert_vertice(ambiente)

# grafo.show_graph()

# Agregamos al menos 3 aristas a cada vertice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros.
grafo.insert_arista('cocina', 'cochera', 10)
grafo.insert_arista('cocina', 'quincho', 15)
grafo.insert_arista('cocina', 'baño1', 5)
grafo.insert_arista('cochera', 'quincho', 12)
grafo.insert_arista('cochera', 'baño1', 8)
grafo.insert_arista('cochera', 'baño2', 10)
grafo.insert_arista('quincho', 'baño1', 3)
grafo.insert_arista('quincho', 'baño2', 7)
grafo.insert_arista('quincho', 'habitacion1', 4)
grafo.insert_arista('quincho', 'habitacion2', 6)
grafo.insert_arista('baño1', 'habitacion1', 2)
grafo.insert_arista('baño1', 'habitacion2', 5)
grafo.insert_arista('baño2', 'habitacion1', 1)
grafo.insert_arista('baño2', 'habitacion2', 4)
grafo.insert_arista('habitacion1', 'cocina', 10)
grafo.insert_arista('habitacion2', 'sala de estar', 8)
grafo.insert_arista('sala de estar', 'terraza', 15)
grafo.insert_arista('sala de estar', 'patio', 12)
grafo.insert_arista('terraza', 'patio', 7)

# grafo.show_graph()

# Obtener el arbol de expancion minimo
arbol_expansion_min = grafo.kruskal('cocina')

# Mostrar el arbol de expancion minimo
def mostrar_arbol_expansion(arbol):
    for arista in arbol[0].split(';'):
        origen, destino, peso = arista.split('-')
        print(f"origen: {origen} -> destino: {destino} -> metros: {peso}")

mostrar_arbol_expansion(arbol_expansion_min)

# determine cuantos metros de cables se necesitan para conectar todos los ambientes.
def suma_aristas_arbol_exp(arbol_expansion_min):
    peso_total = 0
    for arista in arbol_expansion_min[0].split(';'):
        origen, destino, peso = arista.split('-')
        peso_total += int(peso)
    return peso_total
print("--------------------------------")
print(f'Los metros de cables necesarios para conectar todos los ambientes son: {suma_aristas_arbol_exp(arbol_expansion_min)}')

#determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
camino_minimo = grafo.dijkstra("habitacion1")

def mostrar_camino_dijkstra_minimo(camino_minimo):
    destino = 'sala de estar'
    peso_total = None
    camino_completo = []
    while camino_minimo.size() > 0:
        value = camino_minimo.pop()
        if value[1][0] == destino:
            if peso_total is None:
                peso_total = value[0]
            camino_completo.append(value[1][0])
            destino = value[1][2]
    camino_completo.reverse()
    print("--------------------------------")
    print(f'El camino mas corto desde la habitacion 1 hasta la sala de estar es: {'-'.join(camino_completo)} con un costo de {peso_total}')

mostrar_camino_dijkstra_minimo(camino_minimo)