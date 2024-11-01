from grafo import Graph

#Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo
# Crear el grafo
grafo = Graph(dirigido=False)
# de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las naturales) y tipo (natural o arquitectónica)
# Agregar los vertices (maravillas) al grafo
maravillas = [
    ('Torre Eiffel', 'Francia', 'arquitectónica'),
    ('Cataratas del Ródano', 'Francia', 'natural'),
    ('Mont Blanc', 'Francia', 'natural'),
    ('Taj Mahal', 'India', 'arquitectónica'),
    ('Río Ganges', 'India', 'natural'),
    ('Gran Muralla China', 'China', 'arquitectónica'),
    ('Opera de Sidney', 'Australia', 'arquitectónica'),
    ('Monte Uluru', 'Australia', 'natural'),
    ('Monte Everest', 'Nepal', 'natural'),
    ('Venecia', 'Italia', 'arquitectónica'),
    ('Coliseo', 'Italia', 'arquitectónica'),
    ('Monte Vesubio', 'Italia', 'natural')
]

for maravilla in maravillas:
    grafo.insert_vertice(maravilla[0], maravilla)
    
#cada vertice debe estar relacionada con las otras seis de su tipo por aristas, para lo que se debe almacenar la distancia que las separa.

grafo.insert_arista('Torre Eiffel', 'Cataratas del Ródano', 500)
grafo.insert_arista('Torre Eiffel', 'Mont Blanc', 600)
grafo.insert_arista('Cataratas del Ródano', 'Mont Blanc', 300)

grafo.insert_arista('Taj Mahal', 'Río Ganges', 600)

grafo.insert_arista('Gran Muralla China', 'Taj Mahal', 3885)
grafo.insert_arista('Gran Muralla China', 'Opera de Sidney', 8894)
grafo.insert_arista('Gran Muralla China', 'Monte Everest', 2956)

grafo.insert_arista('Opera de Sidney', 'Monte Uluru', 2884)

grafo.insert_arista('Monte Everest', 'Venecia', 6046)
grafo.insert_arista('Monte Everest', 'Coliseo', 5866)

grafo.insert_arista('Venecia', 'Coliseo', 393)
grafo.insert_arista('Venecia', 'Monte Vesubio', 600)
grafo.insert_arista('Coliseo', 'Monte Vesubio', 250)

grafo.insert_arista('Torre Eiffel', 'Taj Mahal', 6596)
grafo.insert_arista('Torre Eiffel', 'Gran Muralla China', 8103)
grafo.insert_arista('Torre Eiffel', 'Opera de Sidney', 16940)
grafo.insert_arista('Torre Eiffel', 'Monte Everest', 7156)
grafo.insert_arista('Torre Eiffel', 'Venecia', 1110)
grafo.insert_arista('Torre Eiffel', 'Coliseo', 1105)
grafo.insert_arista('Opera de Sidney', 'Venecia', 16215)
grafo.insert_arista('Opera de Sidney', 'Coliseo', 16570)


#grafo.show_graph()

#hallar el árbol de expansión mínimo de cada tipo de las maravillas;
arbol_exp_min_venecia = grafo.kruskal("Venecia")
arbol_exp_min_taj_mahal = grafo.kruskal("Taj Mahal")
arbol_exp_min_taj_eiffel = grafo.kruskal("Torre Eiffel")
arbol_exp_min_gran_muralla_china = grafo.kruskal("Gran Muralla China")
arbol_exp_min_opera_sidney = grafo.kruskal("Opera de Sidney")
arbol_exp_min_monte_everest = grafo.kruskal("Monte Everest")
#mostrar arbol de expancion minima
def mostrar_arbol_expansion(arbol):
    for arista in arbol[0].split(';'):
        origen, destino, peso = arista.split('-')
        print(f"origen: {origen} -> destino: {destino} -> distancia: {peso}Km")

print('--------------------------------')
print('Arbol de expancion minima Venecia:')
print()
mostrar_arbol_expansion(arbol_exp_min_venecia)
print('--------------------------------')
"""Un árbol de expansión mínima de un grafo es único por eso siempre va a ser igual"""
# mostrar_arbol_expansion(arbol_exp_min_taj_mahal)
# print('--------------------------------')
# mostrar_arbol_expansion(arbol_exp_min_taj_eiffel)
# print('--------------------------------')
# mostrar_arbol_expansion(arbol_exp_min_gran_muralla_china)
# print('--------------------------------')
# mostrar_arbol_expansion(arbol_exp_min_opera_sidney)
# print('--------------------------------')
# mostrar_arbol_expansion(arbol_exp_min_monte_everest)

print()
paises_arq_nat = grafo.paises_con_maravillas()
print(f"Los países con maravillas arquitectónicas y naturales son: {paises_arq_nat}")
print("--------------------------------")