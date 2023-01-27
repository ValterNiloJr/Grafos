import random as rd 
import datetime

def inicia_Grafo(name, timer):
    arquivo = open(name,'r')
    largura = open('Busca em largura.txt','w')
    profundidade = open('Busca em profundidade.txt','w')
    rota_custo = open('Resultado Custo-Rota.txt', 'w')

    x = []
    for linha in arquivo:
        linha = linha.strip()
        X = linha.split(' ')
        x.append(X)
    arquivo.close()

    nVertices = x[0][0]
    x.pop(0)
    
    g = Grafo(int(nVertices))

    for linha in x:
        g.adiciona_aresta_matriz(int(linha[0]),int(linha[1]),float(linha[2]))
        g.adiciona_aresta_lista(int(linha[1]),float(linha[2]),int(linha[0]))
        g.adiciona_aresta_lista(int(linha[0]),float(linha[2]),int(linha[1]))
        g.adiciona_aresta_lista1(int(linha[1]),float(linha[2]),int(linha[0]))
        g.adiciona_aresta_lista1(int(linha[0]),float(linha[2]),int(linha[1]))


    g.mostra_matriz()
    print("")
    g.mostra_lista()
    g.info_Grafo()
    g.busca_Largura(0, largura)
    g.busca_Profundidade(0, profundidade)
    g.conexos()

    g.construtivo()
    g.refinamento(rota_custo, timer)

    largura.close()
    profundidade.close()
    rota_custo.close()

class Grafo:


    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo_matriz = [[0]*self.vertices for i in range(self.vertices)]
        self.grafo_lista = [[] for i in range(self.vertices)]
        self.grafo_lista_vizinhos = [[] for i in range(self.vertices)]

    def adiciona_aresta_matriz(self, u, v, w):
        # estou pensando em grafos direcionados simples
        self.grafo_matriz[u-1][v] = w 
        self.grafo_matriz[v-1][u] = w

    def adiciona_aresta_lista(self, u, v, w):
        # estamos pensando em grafo direcionado sem peso nas arestas
        self.grafo_lista[u-1].append(w)
        self.grafo_lista[u-1].append(v)

    def adiciona_aresta_lista1(self, u, v, w):
        # estamos pensando em grafo direcionado sem peso nas arestas
        self.grafo_lista_vizinhos[u-1].append(w)

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        print("M = ")
        for i in range(self.vertices):
            print(self.grafo_matriz[i-1])

    def mostra_lista(self):
        self.l = []
        self.lv = []
        fl = []
        aux = []
        n = 0
        for i in range(self.vertices):
            for j in self.grafo_lista[i-1]:
                aux.append(j)
            a = []
            b = []
            if(len(aux) >= 4):
                n = (len(aux) / 2)
            for k in range (len(aux)):
                if (n > k):
                    a.append(aux[k])
                elif(n <= k):
                    b.append(aux[k])
                
            self.l.append([a]+[b])
            aux=[]
        print("L = ",self.l)

        for i in range(self.vertices):
            for j in self.grafo_lista_vizinhos[i-1]:
                fl.append(j)
            a = []
            b = []
            for k in range (len(fl)):
                a.append(fl[k])     
            self.lv.append(a)
            fl=[]
        

    def info_Grafo(self):
        print('')
        nd = []
        aux = []
        count = []
        n = len(self.grafo_matriz)
        maior_Grau = 0
        grau_Medio = 0
        menor_Grau = 10000000
        indice_maior = -1
        indice_menor = 0
        
        self.grafo_matriz = self.grafo_matriz[-1:] + self.grafo_matriz[:-1]

        for j in (self.grafo_matriz):
            grau = (len(j)) - j.count(0)
            if (grau > maior_Grau):
                maior_Grau = grau
                indice_maior += 1
            if(grau < menor_Grau):
                menor_Grau = grau
                indice_menor += 1
            nd.append(grau)
        
        for i in nd:
            aux.append(i)
        
        grau_Medio = (maior_Grau + menor_Grau) / 2
        print("Maior Grau: ",maior_Grau,"- vertice: ", indice_maior)
        print("Menor Grau: ",menor_Grau,"- vertice: ", indice_menor, "\n")
        print("Grau medio: ", grau_Medio,"\n")
        print("Frequencia relativa: ")

        for i in range(max(nd)):
            count = aux.count(i+1)
            print("Grau", i+1,":",(count/n))

    def busca_Largura(self, vertice_fonte, largura):
        largura.write('#vertice:nivel')
        print('\nbusca em Largura')
        print('Vertice:Nivel')
        grafo = self.lv
        nivel = 0
        count = 0
        n_arestas = 0
        nt_arestas = len(grafo[vertice_fonte])
        visitados, fila = set(), [vertice_fonte]
        while fila:
            vertice = fila.pop(0)
            if ((n_arestas == nt_arestas) or count ==1):
                nt_arestas = len(fila)
                nivel += 1

            if vertice not in visitados:
                visitados.add(vertice)
                fila.extend(grafo[vertice])
                largura.write('\n'+(str(vertice)+':'+(str(nivel))))
                print(vertice,':', nivel)
                n_arestas += 1

            count+=1
        count = 0

    def busca_Profundidade(self, vertice, profundidade):
        profundidade.write('#vertice:nivel')
        print('\nbusca em Profundidade')
        print("Vertices:Nivel")
        
        
        grafo = self.lv
        visitados = set()
        nivel = 0
        
        def dfs_recursiva(self, vertice, nivel, profundidade):
            visitados.add(vertice)
            profundidade.write('\n'+(str(vertice))+':'+(str(nivel)))
            print(vertice,":", nivel)

            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    nivel+=1
                    dfs_recursiva(grafo, vizinho, nivel, profundidade)
            
        
        dfs_recursiva(grafo, vertice, nivel, profundidade)
    
    def conexos(self):
        print('')
        c = self.lv
        k = 0
        self.vertice = []
        conexos = []
        for i in range (len(c)):
            self.vertice.append(i)
        fila = len(self.vertice)
        def busca_Profundidade_conexos(vertice):
            grafo = self.lv 
            visitados = set()
            nivel = 0
            
            def dfs_recursiva_conexos(self, vertice, nivel):
                visitados.add(vertice)
                #print(vertice)
                for vizinho in grafo[vertice]:
                    if vizinho not in visitados:
                        nivel+=1
                        dfs_recursiva_conexos(grafo, vizinho, nivel)

            visitados.add(vertice)
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    nivel+=1
                    dfs_recursiva_conexos(grafo, vertice, nivel)
            return visitados

        aux_conexos = self.vertice.copy()
        count = 0
        while fila > 0:
            aux = []
            aux.extend(busca_Profundidade_conexos(self.vertice[k]))
            if k == count:
                for i in range(len(aux)):
                    aux_conexos.remove(aux[i])
            fila -= len(aux)
            conexos.append(aux)
            if (fila != 0):
                k = aux_conexos[0]
            count += 1
        print('Componentes conexas: ', len(conexos))
        for i in range(len(conexos)):
            print(len(conexos[i]),'- Vertices')
        
                
    def construtivo(self):
        print('')
        grafo = self.grafo_lista[-1:] + self.grafo_lista[:-1]
        vertice = self.vertice
        self.rota = []
        self.aux_rota = []
        for i in zip(vertice, grafo):
            self.aux_rota.append(i)
            
        self.aux_rota = (rd.sample(self.aux_rota, len(self.aux_rota)))
        print('Rota inicial Aleatória:')

        for i in range(len(self.aux_rota)):
            self.rota.append(self.aux_rota[i][0])
        self.rota.append(self.rota[0])
        print(self.rota)
        print('')
        

    def refinamento(self, rota_custo, timer):

        QTI = 1024  # Quantidade de Individuos a serem criados
        TC1 = 0.15  # Taxa de cruzamento nas gerações de 15%
        TM1 = 0.58  # Taxa de mutação nas gerações de 58%

        # Calcula o custo total da rota
        def custos(rota, aux):
            c = []
            for i in range(len(rota)-1):
                for j in range(len(rota)-1):
                    if (rota[i] == aux[j][0]):
                        if (rota[i+1] in aux[j][1]):
                            n_pos = aux[j][1].index(rota[i+1])
                            c.append(aux[j][1][n_pos+1])
            return c

        # Calcula as notas de cada individuo, que é inversamente proporcional ao custo, ou seja, quando menor ao custo, maior a nota
        def avaliacao(c):
            if(c != 0):
                n = ( 1 / c )
            else:
                n = 0
            return n*100

        def cruzamento(selecionado, taxa):

                populacao = selecionado

                for i in range(len(selecionado)):
                        # Um ponto é escolhido para fazer a troca
                        ponto = rd.randint(1, QTI)
                        pais = rd.sample(selecionado, 2)  # Dois pais sao escolhidos

                        # Taxa da probabilidade de cruzamento
                        if (rd.random() <= taxa):
                        # O material genético dos pais e misturado a cada novo individuo
                                populacao[i][:ponto] = pais[0][:ponto]
                                populacao[i][ponto:] = pais[1][ponto:]
                return populacao

        def mutacao(crossover, taxa):
            if rd.random() <= taxa:

                for i in crossover:
                    index_1 = rd.randrange(len(i))
                    index_2 = rd.randrange(len(i))
                    while(index_2==index_1 and i[index_1] != i[index_2]):
                        index_2 = rd.randrange(len(i))

                temp = i[index_1]
                i[index_1] = i[index_2]
                i[index_2] = temp

            return crossover 

        SampleTime = datetime.datetime.now()
        self.rota.pop()
        rota = self.rota
        populacao = []      # Matriz de custos de posição a posição do conjunto de cidades

        contGeracao = 0
        controleNovaGeracao = True
        nmax = 0
        cont = 0
        naux = 0
        length = 0
        
        # 1ª população
        for i in range(QTI):
            populacao.append(rd.sample(rota, len(rota)))
            populacao[i].append(populacao[i][0])

        while (controleNovaGeracao):
            
            apt = []    # Aptidão do individuo
            nota = []       # Avaliação das notas dadas a cada individuo pela distancia a percorrer
            cTotal = []         # Custo de cada individuo da população
            selecionado = []        # Lista dos selecionados 
            sProporcional = []          # Lista da seleção proporcional

            time = []

            for k in range(len(populacao)):
                cTotal.append(custos(populacao[k], self.aux_rota))

            # Faz a avaliação concatenando as somas das notas em relação a distância
            for i in range (len(cTotal)):
                nota.insert(i, avaliacao(sum(cTotal[i])))

            # Seleção proporcional
            for i in range (len(nota)):
                apt.append(nota[i] / (sum(nota)))
                sProporcional.append(apt[i] * len(nota))
                for j in range(int(sProporcional[i])):
                    selecionado.insert(i, populacao[i])

            index = len(populacao) -  len(selecionado)

            # Seleção roleta
            if(len(selecionado) < len(populacao)):
                    roleta = []
                    for i in range (index):
                        roleta.append(rd.sample(populacao, len(populacao)))
                        selecionado.append(roleta[i][0])
            
            #Cruzamento
            plCruzamento = cruzamento(selecionado, TC1)

            #Mutação
            plMutacao = mutacao(plCruzamento, TM1)  

            # Seleção da maior nota, para apresentação do melhor indivíduo
            if(nmax < max(nota)):
                length = int(format(nota.index(max(nota))))
                bst = populacao[length]
                custo = sum(cTotal[length])
                nmax = max(nota)

            lastSampleTime = datetime.datetime.now() - SampleTime 

            print("Geração:", contGeracao, '|-| Tempo:', lastSampleTime)
  
            #Critério de parada por gerações
            if(nmax == naux):
                cont += 1
            else:
                cont = 0
            naux = nmax

            # Se passarem 10 gerações sem alteração, ele para
            if(cont > 10):		
                print("\n \---------------\o/---------------/\n")
                print("O melhor individuo:", bst, "\nCusto:", '{:.1f}'.format(custo))
                rota_custo.write(str('{:.1f}'.format(custo))+'\n'+str(bst))
                controleNovaGeracao = False
                

            #Faz com que os selecionados sejam a próxima geração
            populacao = plMutacao

            if(int(timer) < 10):
                time = '0:00:0' + str(timer)
            else:
                time = '0:00:' + str(timer)

            # Critério de parada por tempo
            # Se passar do tempo estipulado para a execução do programa, ele para
            if(str(lastSampleTime) > time):
                print("\n \---------------\o/---------------/\n")
                print("O melhor individuo:", bst, "\nCusto:", '{:.1f}'.format(custo), '\nTimeOut')
                
                break
            else:
                contGeracao += 1

name = input('Digite o nome do arquivo: ')
time = input('Digite o tempo limite (s): ')

inicia_Grafo(name, time)