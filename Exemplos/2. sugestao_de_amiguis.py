from collections import defaultdict

def inicia_Grafo(arquivo):    
    g = Grafo()
    pontos = []
    grafo = []

    x = []

    for linha in arquivo:
        linha = linha.strip()
        X = linha.split(' ')
        x.append(X)
    
    g = Grafo()
    pontos = []
    grafo = []

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

    amiguis = grafo[0]
    out = loop(g.verificar_amiguis(grafo[1][0], amiguis))

def loop(output):
    output.sort()
    for amiguis in output:
        print(amiguis)

class Grafo():
    def __init__(self):
        self._data = defaultdict(list)

    def conectar(self, nodo_origem, nodo_destino):
        self._data[nodo_origem].append(nodo_destino)

    def vizinhos(self, nodo):
        return self._data[nodo]

    def verificar_amiguis(self, nodo_inicial, amiguis):
        nodos_visitados = set()
        nodos_restantes = [nodo_inicial]
        novo = []
        count = 0
        while nodos_restantes:
            nodo_atual = nodos_restantes.pop()
            nodos_restantes = []
            nodos_visitados.add(nodo_atual)
            for vizinho in self.vizinhos(nodo_atual):
                for amigo in amiguis:
                    if ((vizinho not in amiguis)):
                        novo.append(vizinho)
                nodos_restantes.append(vizinho)

            if (count >= len(self._data)):
                if (novo == []):
                    novo.append('Cacildis! Cade elis?')
                else:
                    novo.pop()
                out = list(set(novo))
                return out
            count+=1

num = int(input())
n = 0
grafo = []
while n < num:
    grafo.append(input())
    n = n + 1

inicia_Grafo(grafo)