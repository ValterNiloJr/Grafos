from collections import defaultdict

def inicia_Grafo(arquivo):    
    g = Grafo()
    pontos = []
    grafo = []

    x = []

    for linha in arquivo:
        X = linha.split(' ')
        x.append(X)

    for linha in x:
        pontos = []
        pontos.append(linha[0])
        for i in range(len(linha)-1):
            pontos.append(linha[i+1])
        pontos.pop(1)
        grafo.append(pontos)

    for linha in grafo:
        for vertice in linha:
            if linha[0] != vertice:
                g.conectar(linha[0], vertice)

    if g.verificar_ciclos(grafo[0][0]):
        print('\nHoje tem!')
    else:
        print('\n... que ama ninguem.')

class Grafo():
    def __init__(self):
        self._data = defaultdict(list)

    def conectar(self, nodo_origem, nodo_destino):
        self._data[nodo_origem].append(nodo_destino)

    def vizinhos(self, nodo):
        return self._data[nodo]

    def verificar_ciclos(self, nodo_inicial):
        nodos_visitados = set()
        nodos_restantes = [nodo_inicial]

        while nodos_restantes:
            nodo_atual = nodos_restantes.pop()
            nodos_restantes = []
            nodos_visitados.add(nodo_atual)

            for vizinho in self.vizinhos(nodo_atual):
                if vizinho in nodos_visitados:
                    return True

                nodos_restantes.append(vizinho)

        return False 

num = int(input())
n = 0
grafo = []
while n < num:
    grafo.append(input())
    n = n + 1

inicia_Grafo(grafo)