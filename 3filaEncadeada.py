
# para agilizar o processo de envio dessa lista, pq sei q corrigir isso da trabalho e foi erro meu apagar esse ultimo arquivo de fila estou utilizando o chatgbt

# me lembro do meu codigo , fiz umas leves alteraçoes nesse (colocar no padrão q ja estudamos), irei comentar somente onde a resposta esta melhor, igual ou onde eu não entender oq o codigo esta fazendo 

# nunca mais dou shift delete em algum arquivo 😂😂😂😂😂😂😂 

class Nodo: #igual ao meu
    def __init__(self, dado = 0, proximo= None):
        self.dado = dado  
        self.proximo = None

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class fila:
    def __init__(self): #igual ao meu
        self.inicio = None 
        self.fim = None  
        
    def head(self): #igual ao meu
        return "[" + str(self.inicio) +"]"
        
    def inserirInicio(self, dado): #igual ao meu
        novo_nodo = Nodo(dado)
        if self.head():
            self.inicio = novo_nodo 
        else:
            self.fim.proximo = novo_nodo  
            self.fim = novo_nodo  
        
    def remover(self): #melhor que o meu, so não tinha pensado em colocar somente self.head para verificar com if
        if self.head():
            print("fila vazia")
            return None
        self.inicio = self.inicio.proximo  
        if self.inicio is None:
            self.fim = None 
        
    def buscar(self, valor): #igual ao meu, so coloquei o if fora e print ao inves de return
        corrente = self.inicio
        posicao = 0
        while corrente is not None:
            if corrente.dado == valor:
                return posicao  
            corrente = corrente.proximo
            posicao += 1
        
    def inverter(self): #não entendi, como não uso mais bild tim essa solução ficou muito diferente da minha, não sabia q dava para fazer isso com append, so reutilizei a função "busca" pra criar uma correte e atribuir a uma nova pilha 
        if self.head():
            print("fila vazia")
            
        pilha = []
        while not self.head():
            pilha.append(self.remover())  # Removemos e empilhamos cada elemento
        
        # Reinsere os elementos na fila na ordem inversa
        while pilha:
            self.inserirInicio(pilha.pop())
            
# -------------------------------------------------------
# ------------------------foram esses que fiquei mais travados-------------------------------
            
    def adicionar_processo(self, processo): #igual ao meu
        self.inserirInicio(processo) 
        
    def matar_processo_maior_espera(self): # melhor que o meu, tentei fazer com dicionarios, me compliquei com a biblioteca pandas, não entendi algumas coisas
        
        if self.head():
            print("A fila de processos está vazia!")
            return
        
        # dese jeito ficaria muito mais simples kkkkkkkkkkkk
        atual = self.inicio
        anterior = None
        maior_espera = atual.dado["wait"]
        nodo_maior_espera = atual
        anterior_maior_espera = None
        
        while atual is not None:
            if atual.dado["wait"] > maior_espera:
                maior_espera = atual.dado["wait"]
                nodo_maior_espera = atual
                
                # isso é necessaraio ?
                anterior_maior_espera = anterior
                
                #isso entendi mais ou menos, os nomes me confundem um pouco 
            anterior = atual
            atual = atual.proximo
        
        
        # isso é so para printar depois de achar, so os nomes q estão me confundido um pouco
        if nodo_maior_espera == self.inicio:
            self.inicio = self.inicio.proximo 
            
        else:
            anterior_maior_espera.proximo = nodo_maior_espera.proximo 
        print(f"Processo com maior espera {nodo_maior_espera.dado['id']} removido.")
        
        
    def executar_processo(self): #melhor que o meu, mas entendi o codigo
        processo_removido = self.remover()
        if processo_removido is not None:
            print(f"Processo {processo_removido['id']} executado.")
            
    def imprimir_processos(self): #melhor que o meu, mas entendi o codigo
        atual = self.inicio
        while atual is not None:
            print(f"Processo ID: {atual.dado['id']}, Prioridade: {atual.dado['priorety']}, Espera: {atual.dado['wait']}")
            atual = atual.proximo



fila = fila()

processo1 = {"id": 101, "name": "Processo A", "priorety": 4, "wait": 10}
processo2 = {"id": 102, "name": "Processo B", "priorety": 2, "wait": 30}
processo3 = {"id": 103, "name": "Processo C", "priorety": 1, "wait": 50}


fila.adicionar_processo(processo1)
fila.adicionar_processo(processo2)
fila.adicionar_processo(processo3)

fila.imprimir_processos()

fila.matar_processo_maior_espera()

fila.executar_processo()

fila.imprimir_processos()



