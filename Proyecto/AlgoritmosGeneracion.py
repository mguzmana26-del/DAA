import random
import math
from Grafo import Grafo

class AlgoritmosGeneracion:
    def grafoMalla(m, n, dirigido=False): # Listo
        """
        Genera grafo de malla
        :param m: número de columnas (> 1)
        :param n: número de filas (> 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        g = Grafo()
        print("n*m es: ", n*m)
        for i in range(n*m):
            g.addNodo(i)
        for i in range(n):
            for j in range(m):
                nodo = i*m + j
                if j < m-1:
                    v = i*m + (j+1)
                    g.addEdge(str(nodo)+'--'+str(v), nodo, v)
                if i < n-1:
                    v = (i+1)*m + j
                    g.addEdge(str(nodo)+'--'+str(v), nodo, v)
        return g
        
    def grafoErdosRenyi(n, m, dirigido=False): # Listo
        """
        Genera grafo aleatorio con el modelo Erdos-Renyi
        :param n: número de nodos (> 0)
        :param m: número de aristas (>= n-1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        edges = set()
        g = Grafo()
        for i in range(n):
            g.addNodo(i)
        #for j in range(m):
        while len(edges) < m:
            n0 = random.randint(0, n-1)
            n1 = random.randint(0, n-1)
            if(n1 != n0):
                edge = tuple(sorted((n0, n1)))
                if edge not in edges: 
                    edges.add(edge)
                    g.addEdge(str(n0)+'--'+str(n1), str(n0), str(n1))
        return g

    def grafoGilbert(n, p, dirigido=False): # Listo
        """
        Genera grafo aleatorio con el modelo Gilbert
        :param n: número de nodos (> 0)
        :param p: probabilidad de crear una arista (0, 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        g = Grafo()
        for i in range(n):
            g.addNodo(i)
            for j in range(i+1, n):
                prob = random.random()
                if(prob < p and i != j):
                    g.addEdge(str(i)+'--'+str(j), str(i), str(j))

        return g

    def grafoGeografico(n, r, dirigido=False): #Listo
        """
        Genera grafo aleatorio con el modelo geográfico simple
        :param n: número de nodos (> 0)
        :param r: distancia máxima para crear un nodo (0, 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        #aristas = filas(columnas-1)+columnas(filas-1)
        g = Grafo()
        x_cord = []
        y_cord = []
        for i in range(n):
            g.addNodo(i)
            x = random.random()
            y = random.random()
            x_cord.append(x)
            y_cord.append(y)
        
        for i in range(n):
            for j in range(i+1, n):
                if i!= j:
                    d = math.sqrt((x_cord[i]-x_cord[j])**2+(y_cord[i]-y_cord[j])**2)
                    if d < r:
                        g.addEdge(str(i)+'--'+str(j), str(i), str(j))
                
        return g

    def grafoBarabasiAlbert(n, d, dirigido=False): # Listo
        """
        Genera grafo aleatorio con el modelo Barabasi-Albert
        :param n: número de nodos (> 0)
        :param d: grado máximo esperado por cada nodo (> 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """ 
        conexiones = []
        g = Grafo()
        for i in range(d):
            g.addNodo(i)
        
        for i in range(d):
            for j in range(i+1, d):
                g.addEdge(str(i)+'--'+str(j), str(i), str(j))
                conexiones.append(i)
                conexiones.append(j)
        listita = []
        for i in range(d, n):
            g.addNodo(i)
            #for j in range(d):
            while(len(listita) < d):
                nodo = random.choice(conexiones)
                if(nodo not in listita and nodo != i):
                    listita.append(nodo)
                    g.addEdge(str(i)+'--'+str(nodo), str(i), str(nodo))
                    conexiones.append(i)
                    conexiones.append(nodo)
            listita = []
        return g

    def grafoDorogovtsevMendes(n, dirigido=False): # Listo
        """
        Genera grafo aleatorio con el modelo Barabasi-Albert
        :param n: número de nodos (≥ 3)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        g = Grafo()
        for i in range(0, 2):
            g.addNodo(i)
        g.addEdge("0--1", str(0), str(1))
        g.addEdge("1--2", str(1), str(2))
        g.addEdge("2--0", str(2), str(0))

        for i in range(3, n):
            g.addNodo(i)
            a = g.getRandomArista()
            n0 = a.n0.dato
            n1 = a.n1.dato
            g.addEdge(str(i)+'--'+str(n0), str(i), str(n0))
            g.addEdge(str(i)+'--'+str(n1), str(i), str(n1))

        return g