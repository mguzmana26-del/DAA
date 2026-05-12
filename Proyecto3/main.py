from AlgoritmosGeneracion import AlgoritmosGeneracion
#Malla con 100 nodos
isDirected = True
# Malla con 50 nodos no dirigido
#p1  = AlgoritmosGeneracion.grafoMalla(7, 8) # 56
#p1.getGraph('Malla_50.gv')
#while(True):
#    s1 = p1.getRandomNodo()
#    s2 = p1.getRandomNodo()
#    p1.Dijkstra(s1)
#    camino = p1.camino_mas_corto(s1, s2)
#    print("Camino 1 es: ", camino)
#    p1.getDijkstra("malla_50_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Malla con 200 nodos dirigido
#p2  = AlgoritmosGeneracion.grafoMalla(15, 14, isDirected) # 210
#p2.getGraph('Malla_200.gv')
#while(True):
#    s1 = p2.getRandomNodo()
#    s2 = p2.getRandomNodo()
#    p2.Dijkstra(s1)
#    camino = p2.camino_mas_corto(s1, s2)
#    print("Camino 2 es: ", camino)
#    p2.getDijkstra("malla_200_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Erdos Renyi con 50 nodos
#p3  = AlgoritmosGeneracion.grafoErdosRenyi(50, 50)
#p3.getGraph('ErdosRenyi_50.gv')
#while(True):
#    s1 = p3.getRandomNodo()
#    s2 = p3.getRandomNodo()
#    p3.Dijkstra(s1)
#    camino = p3.camino_mas_corto(s1, s2)
#    print("Camino 3 es: ", camino)
#    p3.getDijkstra("erdosRenyi_50_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Erdos Renyi con 200 nodos
#p4  = AlgoritmosGeneracion.grafoErdosRenyi(200, 200) # 100
#p4.getGraph('ErdosRenyi_200.gv')
#while(True):
#    s1 = p4.getRandomNodo()
#    s2 = p4.getRandomNodo()
#    p4.Dijkstra(s1)
#    camino = p4.camino_mas_corto(s1, s2)
#    print("Camino 4 es: ", camino)
#    p4.getDijkstra("erdosRenji_200_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Gilbert con 50 nodos
#p5  = AlgoritmosGeneracion.grafoGilbert(50, 0.3, isDirected) # 100
#p5.getGraph('Gilbert_50.gv')
#while(True):
#    s1 = p5.getRandomNodo()
#    s2 = p5.getRandomNodo()
#    p5.Dijkstra(s1)
#    camino = p5.camino_mas_corto(s1, s2)
#    print("Camino 5 es: ", camino)
#    p5.getDijkstra("Gilbert_50_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Gilbert con 200 nodos
#p6  = AlgoritmosGeneracion.grafoGilbert(200, 0.3) # 100
#p6.getGraph('Gilbert_200.gv')
#while(True):
#    s1 = p6.getRandomNodo()
#    s2 = p6.getRandomNodo()
#    p6.Dijkstra(s1)
#    camino = p6.camino_mas_corto(s1, s2)
#    print("Camino 6 es: ", camino)
#    p6.getDijkstra("Gilbert_200_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Geografico con 50 nodos
p7  = AlgoritmosGeneracion.grafoGeografico(50, 0.4) # 100
p7.getGraph('Geografico_50.gv')
while(True):
    s1 = p7.getRandomNodo()
    s2 = p7.getRandomNodo()
    p7.Dijkstra(s1)
    print('s1 y s2 es: ', s1, s2)
    camino = p7.camino_mas_corto(s1, s2)
    print("Camino 7 es: ", camino)
    p7.getDijkstra("geografico_50_dijkstra.gv", camino)
    if s1 != s2:
        break

# Geografico con 200 nodos
#p8  = AlgoritmosGeneracion.grafoGeografico(200, 0.7) # 100
#p8.getGraph('Geografico_200.gv')
#while(True):
#    s1 = p8.getRandomNodo()
#    s2 = p8.getRandomNodo()
#    print('s1 y s2 es: ', s1, s2)
#    p8.Dijkstra(s1)
#    camino = p8.camino_mas_corto(s1, s2)
#    print("Camino 8 es: ", camino)
#    p8.getDijkstra("Geografico_200_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Barabasi Albert con 50 nodos
#p9  = AlgoritmosGeneracion.grafoBarabasiAlbert(50, 3) # 100
#p9.getGraph('BarabasiAlbert_50.gv')
#while(True):
#    s1 = p9.getRandomNodo()
#    s2 = p9.getRandomNodo()
#    print('s1 y s2 es: ', s1, s2)
#    p9.Dijkstra(s1)
#    camino = p9.camino_mas_corto(s1, s2)
#    print("Camino 9 es: ", camino)
#    p9.getDijkstra("BarabasiAlbert_50_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Barabasi Albert con 200 nodos
#p10  = AlgoritmosGeneracion.grafoBarabasiAlbert(200, 4) # 200
#p10.getGraph('BarabasiAlbert_200.gv')
#while(True):
#    s1 = p10.getRandomNodo()
#    s2 = p10.getRandomNodo()
#    p10.Dijkstra(s1)
#    camino = p10.camino_mas_corto(s1, s2)
#    print("Camino 10 es: ", camino)
#    p10.getDijkstra("BarabasiAlbert_200_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Dorogovtsev Mendes con 500 nodos
#p11  = AlgoritmosGeneracion.grafoDorogovtsevMendes(50) # 50
#p11.getGraph('DorogovtsevMendes_50.gv')
#while(True):
#    s1 = p11.getRandomNodo()
#    s2 = p11.getRandomNodo()
#    p11.Dijkstra(s1)
#    camino = p11.camino_mas_corto(s1, s2)
#    print("Camino 11 es: ", camino)
#    p11.getDijkstra("DorogovtsevMendes_50_dijkstra.gv", camino)
#    if s1 != s2:
#        break

# Dorogovtsev Mendes con 200 nodos
#p12  = AlgoritmosGeneracion.grafoDorogovtsevMendes(200) # 200
#p12.getGraph('DorogovtsevMendes_200.gv')
#while(True):
#    s1 = p12.getRandomNodo()
#    s2 = p12.getRandomNodo()
#    p12.Dijkstra(s1)
#    camino = p12.camino_mas_corto(s1, s2)
#    print("Camino 12 es: ", camino)
#    p12.getDijkstra("DorogovtsevMendes_200_dijkstra.gv", camino)
#    if s1 != s2:
#        break