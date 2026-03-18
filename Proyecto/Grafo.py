from Nodo import Nodo
from Arista import Arista
import random

class Grafo:
    def __init__(self):
        self.id = ""
        self.nodos   ={}
        self.aristas ={}

    def nombreNodo(i, j):
        return 
    
    def nombreArista ():
        return
    
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
        e = self.aristas.get(nombre)
        if e is None:
            #self.aristas[nombre] = arista.id
            n0 = self.addNodo(nodo0)
            n1 = self.addNodo(nodo1)
            arista = Arista(n0, n1, nombre)
            self.aristas[nombre] = arista
        #print("Arista totales: ", self.aristas)
        return arista
    
    # Crea el archivo con el nombre 'grafo.gv'
    def getGraph(self):
        with open('grafo.gv', "w") as file:
            file.write("graph G {\n")
            connector = "--"

            for arista in self.aristas.values():
                n0 = arista.n0.dato
                n1 = arista.n1.dato
                file.write(f"    {n0} {connector} {n1};\n")

            file.write("}\n")
    
    # Crea el archivo con el nombre del valor que contiene la variable filename
    def getGraph2(self, filename):        
        with open(filename+'.gv', "w") as file:
            file.write("graph G {\n")
            connector = "--"

            for arista in self.aristas.values():
                n0 = arista.n0.dato
                n1 = arista.n1.dato
                file.write(f"    {n0} {connector} {n1};\n")

            file.write("}\n")
    
    def getNodos(self):
        return self.nodos

    def getArista(self, name):
        return self.aristas.get(name)
    
    def getAristas(self):
        return self.aristas
    
    def getAristas(self):
        return self.aristas
    
    def getRandomArista(self):
        return random.choice(list(self.aristas.values()))