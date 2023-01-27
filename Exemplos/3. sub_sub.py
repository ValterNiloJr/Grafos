from collections import defaultdict

def inicia_Grafo(arquivo1, arquivo2):    
    g = Grafo()
    pontos = []
    grafo = []

    x = []
    y = []

    for linha in arquivo1:
        X = linha.split(' ')
        x.append(X)

    for linha in arquivo2:
        Y = linha.split(' ')
        y.append(Y)

    grafo = x
    sub_grafo = y

    g = Grafo()
    pontos = []
    check_sum = []
    flag = True


    for i in range(len(grafo)):
        grafo[i].pop(1)
    for i in range(len(sub_grafo)):
        sub_grafo[i].pop(1)

    for linha in grafo:
        for vertice in linha:
            if linha[0] != vertice:
                g.conectar(linha[0], vertice)
    for linha in sub_grafo:
        check_sum.append(linha[0])
        for vertice in linha:
            if linha[0] != vertice:
                g.conectar_sub(linha[0], vertice)

    if sub_grafo == []:
        print('\nSub-sub!')
    elif (g.verificar_sub(grafo[0][0], sub_grafo[0][0], check_sum)):
        print('\nSub-sub!')
    else:
        print('\nUe? Ue? Ue?')



class Grafo():
    def __init__(self):
        self._data = defaultdict(list)
        self._data_sub = defaultdict(list)

    def conectar(self, nodo_origem, nodo_destino):
        self._data[nodo_origem].append(nodo_destino)

    def conectar_sub(self, nodo_origem_sub, nodo_destino_sub):
        self._data_sub[nodo_origem_sub].append(nodo_destino_sub)

    def vizinhos(self, nodo):
        return self._data[nodo]

    def vizinhos_sub(self, nodo_sub):
        return self._data_sub[nodo_sub]

    def verificar_sub(self, nodo_inicial, nodo_inicial_sub, check_sum):
        nodos_visitados = set()
        nodos_visitados_sub = set()
        nodos_restantes = [nodo_inicial]
        nodos_restantes_sub = [nodo_inicial_sub]
        check = []
        count = 0
        while nodos_restantes_sub:
            nodo_atual_sub = nodos_restantes_sub.pop()
            nodo_atual = nodo_atual_sub
            nodos_restantes = []
            #nodos_restantes_sub = []
            nodos_visitados.add(nodo_atual)
            nodos_visitados_sub.add(nodo_atual_sub)

            for vizinho in self.vizinhos(nodo_atual):
                if (self.vizinhos_sub(nodo_atual_sub) != []):
                    for vizinho_sub in self.vizinhos_sub(nodo_atual_sub):
                        if (vizinho in vizinho_sub) and (nodo_atual_sub not in check):
                            print('atual: ', nodo_atual_sub)
                            check.append(nodo_atual_sub)
                        
                        nodos_restantes_sub.append(vizinho_sub)
                else:
                    if (nodo_atual_sub not in check):
                        check.append(nodo_atual_sub)

                nodos_restantes.append(vizinho)

            check.sort()
            print(check_sum)
            print(check)
            if (check == check_sum):
                return True
            if (count == len(self._data_sub)):
                    return False
            count += 1

num = int(input())
n = 0
grafo = []
sub_grafo = []
while n < num:
    grafo.append(input())
    n = n + 1

space = input()

num = int(input())
n = 0
while n < num:
    sub_grafo.append(input())
    n = n + 1

inicia_Grafo(grafo, sub_grafo)