def bfs (arbol = {}):
    ##Inicializar la lista de nodos por visitar con el primer nodo en la lista
    por_visitar = []
    por_visitar.append(str(list(arbol.keys())[0]))

    ##Lista de nodos visitafos
    bfs = []

    for elemento in por_visitar:
        if elemento not in bfs:
            bfs.append(elemento)
        ##Verificar que el nodo existe en el arbol antes de intentar visitarlo
        if elemento in arbol:
            for hijo in arbol[elemento]:
                if hijo not in por_visitar:
                    por_visitar.append(hijo)
    return bfs


arbol = {"A":["B","C","D","E"],"B":["A","C","G"],"C":["A","D"], "D":["A","C","E","H"],"E":["A","D","F"], "F":["E","H","G","I"], "G":["B","H"],"H":["D","F"],"I":["F"]}
#print(arbol)
orden_bfs = bfs(arbol)
print(orden_bfs)