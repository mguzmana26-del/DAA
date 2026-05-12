from Nodo import Nodo
from Arista import Arista
import random
import os
import subprocess

class Grafo:
    def __init__(self, dirigido):
        self.id = ""
        self.nodos   ={}
        self.aristas ={}
        self.dirigido = dirigido
        self.vecinos = {}
        self.path = []
        self.nodosDijkstra = {}
        self.aristasDijkstra = {}
        self.dist = {}
        self.padre = {}
        self.origen = None
        self.destino = None
    
    def addNodo(self, nombre):
        nodo = self.nodos.get(nombre)
        #print("EL nodo es: ", nodo)
        if nodo is None:
            nodo = Nodo(nombre)
            #print("EL nodo despues es: ", nodo.dato)
            self.nodos[nombre] = nodo
            #print("Nodos totales: ", self.nodos)
        #else:
        #    return
        return nodo

    def addEdge(self, nombre, nodo0, nodo1):
        arista = self.aristas.get(nombre)
        #print("La arista es: ", arista, nombre)
        #print("La arista despues es: ", arista.id)
        w = random.randint(10, 20)
        e = self.aristas.get(nombre)
        if e is None:
            #self.aristas[nombre] = arista.id
            n0 = self.addNodo(nodo0)
            n1 = self.addNodo(nodo1)
            arista = Arista(n0, n1, nombre, w)
            self.aristas[nombre] = arista
            self.vecinos.setdefault(nodo0, []).append((nodo1, w))
            
            if self.dirigido == False:
                self.vecinos.setdefault(nodo1, []).append((nodo0, w))
        #print("Arista totales: ", self.aristas)
        return arista
    
    # Crea el archivo con el nombre 'grafo.gv'
    def getGraph(self, filename):
        with open(filename, "w") as file:
            file.write("graph G {\n")
            connector = "--"

            for arista in self.aristas.values():
                n0 = arista.n0.dato
                n1 = arista.n1.dato
                file.write(f"    {n0} {connector} {n1};\n")

            file.write("}\n")
    
    def getArista(self, name):
        return self.aristas.get(name)
    
    def getAristas(self):
        return self.aristas
    
    def getRandomArista(self):
        return random.choice(list(self.aristas.values()))
    
    def getRandomNodo(self):
        return random.choice(list(self.nodos.keys()))
    #----------------------------------------------------
    # Algoritmos de busqueda
    # ---------------------------------------------------
    def getVecinos(self, nodo):
        return self.vecinos.get(nodo, [])

    def BFS(self, s):
        visited = set([s])
        queue = [s]
        edges_written = set()
        while queue:
            node = queue.pop(0)
            for vecino in self.getVecinos(node):
                if vecino not in visited:
                    visited.add(vecino)
                    queue.append(vecino)
                    edge = tuple(sorted((node, vecino)))
                    if edge not in edges_written:
                        nombre = str(edge[0])+'--'+str(edge[1])
                        nodo0 = edge[0]
                        nodo1 = edge[1]
                        edges_written.add(edge)
                        e = self.aristasBFS.get(nombre)
                        if e is None:
                            n0 = self.addNodo(nodo0)
                            n1 = self.addNodo(nodo1)
                            arista = Arista(n0, n1, nombre)
                            self.aristasBFS[nombre] = arista
                            self.vecinosBFS.setdefault(nodo0, []).append(nodo1)
                            self.vecinosBFS.setdefault(nodo1, []).append(nodo0)
        self.getGraphSearch("BFS.gv", self.aristasBFS)
        return edges_written

    def DFS_R(self, s):
        self.visitedDSF_R.add(s)
        self.path.append(s)
        for v in self.getVecinos(s):
            if v is None:
                return
            #if v not in self.path:
            if v not in self.visitedDSF_R:
                self.visitedDSF_R.add(v)
                node = self.path[-1]
                edge = tuple(sorted((node, v)))
                if edge not in self.edges_written_DFS_R:
                        nombre = str(edge[0])+'--'+str(edge[1])
                        nodo0 = edge[0]
                        nodo1 = edge[1]
                        self.edges_written_DFS_R.add(edge)
                        e = self.aristasDFS_R.get(nombre)
                        if e is None:
                            #n0 = self.nodos.get(nodo0)
                            #n1 = self.nodos.get(nodo1)
                            n0 = self.addNodo(nodo0)
                            n1 = self.addNodo(nodo1)
                            arista = Arista(n0, n1, nombre)
                            self.aristasDFS_R[nombre] = arista
                            self.vecinosDFS_R.setdefault(nodo0, []).append(nodo1)
                            self.vecinosDFS_R.setdefault(nodo1, []).append(nodo0)
                            self.DFS_R(v)
        return self.getGraphSearch('DFS_R.gv', self.aristasDFS_R)

    def DFS_I(self, s):
        visited = set()
        stack = [(s, None)]
        edges_written = set()
        while stack:
            node, parent = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if parent is not None:
                edge = tuple(sorted((node, parent)))
                if edge not in edges_written:
                    nombre = str(edge[0]) + '--' + str(edge[1])
                    nodo0, nodo1 = edge
                    edges_written.add(edge)
                    n0 = self.addNodo(nodo0)
                    n1 = self.addNodo(nodo1)
                    arista = Arista(n0, n1, nombre)
                    self.aristasDFS_I[nombre] = arista
                    self.vecinosDFS_I.setdefault(nodo0, []).append(nodo1)
                    self.vecinosDFS_I.setdefault(nodo1, []).append(nodo0)

            for vecino in self.getVecinos(node):
                if vecino not in visited:
                    stack.append((vecino, node))
        self.getGraphSearch("DFS_I.gv", self.aristasDFS_I)
        return edges_written
    
    def getGraphSearch(self, filename="path.gv", aristas=[]):
        with open(filename, "w") as file:
            file.write("graph{\n")
            for arista in aristas.values():
                n0 = arista.n0.dato
                n1 = arista.n1.dato
                file.write(f'    {n0} -- {n1};\n')

            file.write("}\n")
    
    #----------------------------------------------------
    # Algoritmo de Dijkstra
    # ---------------------------------------------------
    def camino_mas_corto(self, origen, destino):
        self.origen = origen
        self.destino = destino
        camino = []
        actual = destino
        while actual != origen:
            p = self.padre[actual]
            if p is None:
                return []
            camino.append((p, actual))
            actual = p
        camino.reverse()
        return camino
    
    def Dijkstra(self, s):
        visitado = {}
        for nodo in self.nodos:
            self.dist[nodo] = float('inf')
            self.padre[nodo] = None
            visitado[nodo] = False
        self.dist[s] = 0
        while True:
            actual = None
            menor_dist = float('inf')
            for nodo in self.nodos:
                if not visitado[nodo]:
                    if self.dist[nodo] < menor_dist:
                        menor_dist = self.dist[nodo]
                        actual = nodo
            if actual is None:
                break
            visitado[actual] = True
            for vecino, peso in self.getVecinos(actual):
                #print("ACTUAL:", actual)
                #print("VECINOS:", self.getVecinos(actual))
                nueva_dist = self.dist[actual] + peso
                if nueva_dist < self.dist[vecino]:
                    self.dist[vecino] = nueva_dist
                    self.padre[vecino] = actual
        #print("DIST:", self.dist[24])
        #print("PADRE 24:", self.padre[24])
        #print("PADRES:", self.padre)
  
    def getDijkstra(self, filename, camino):
        with open(filename, "w") as file:
            if self.dirigido:
                file.write("digraph G {\n")
                arrow = "->"
            else:
                file.write("graph G {\n")
                arrow = "--"

            file.write('layout=neato;\n')
            file.write('overlap=false;\n')
            file.write('splines=true;\n')
            file.write('node [shape=circle];\n')
            camino_set = set()

            for u, v in camino:
                camino_set.add((u, v))
                camino_set.add((v, u))

            nodos_camino = set()

            for u, v in camino:
                nodos_camino.add(u)
                nodos_camino.add(v)
            for nodo in self.nodos:
                distancia = self.dist.get(nodo, float('inf'))
                if nodo == self.origen:
                    fill = "green"
                elif nodo == self.destino:
                    fill = "red"
                elif nodo in nodos_camino:
                    fill = "gold"
                elif distancia == float('inf'):
                    fill = "lightgray"
                else:
                    fill = "lightblue"

                if nodo in nodos_camino:
                    etiqueta = f"{nodo}\\nDist:{distancia}"
                else:
                    etiqueta = f"{nodo}"

                file.write(
                    f'"{nodo}" '
                    f'[label="{etiqueta}", '
                    f'style=filled, '
                    f'fillcolor={fill}, '
                    f'fontsize=18, '
                    f'width=1.2, '
                    f'height=1.2];\n'
                )

            for arista in self.aristas.values():
                n0 = arista.n0.dato
                n1 = arista.n1.dato
                peso = arista.weight
                color = "black"
                ancho = 1
                # Camino mínimo
                if (n0, n1) in camino_set:
                    color = "red"
                    ancho = 3
                if color == "red":
                    etiqueta = f"{peso} / total:{self.dist[n1]}"
                else:
                    etiqueta = f"{peso}"
                file.write(
                    f'"{n0}" {arrow} "{n1}" '
                    f'[label="{etiqueta}", '
                    f'color={color}, '
                    f'style=solid, '
                    f'penwidth={ancho}, '
                    f'fontsize=14];\n'
                )

            if self.destino is not None:
                costo_total = self.dist.get(self.destino, float('inf'))
                file.write(
                    f'label="Costo total mínimo: {costo_total}";\n'
                )
                file.write('labelloc="t";\n')
                file.write('fontsize=20;\n')
            file.write("}\n")

        nombre_png = filename.replace(".gv", ".png")
        subprocess.run([
            "dot",
            "-Tpng",
            filename,
            "-o",
            nombre_png
        ])
        #print(f"Imagen generada: {nombre_png}")