# empurrando pelo terminal vscode, em vez do cmf


class Nodo:
    def __init__(self, dado = 0, proximo= None):
        self.dado = dado  
        self.proximo = None

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)



class fila:
    def __init__(self):
        self.inicio = None 
        self.fim = None  
        
    def head(self):
        return "[" + str(self.inicio) +"]"
        
    def inserirInicio(self, dado):
        novo_nodo = Nodo(dado)
        if self.head():
            self.inicio = novo_nodo 
        else:
            self.fim.proximo = novo_nodo  
            self.fim = novo_nodo  
        
    def remover(self):
        if self.head():
            print("fila vazia")
            return None
        
        removido = self.inicio.dado  # Armazena o dado do primeiro elemento
        self.inicio = self.inicio.proximo  # O novo primeiro elemento é o próximo da fila
        if self.inicio is None:
            self.fim = None  # Se a fila ficou vazia, atualiza o ponteiro do fim
        
    
    def buscar(self, valor):
        corrente = self.inicio
        posicao = 0
        while corrente is not None:
            if corrente.dado == valor:
                return posicao  # Retorna a posição na fila
            corrente = corrente.proximo
            posicao += 1
        return -1  # Valor não encontrado
    
    def inverter(self):
        if self.head():
            print("fila vazia")
            
            
            
        # Usando uma pilha para inverter a fila
        pilha = []
        while not self.head():
            pilha.append(self.remover())  # Removemos e empilhamos cada elemento
        
        # Reinsere os elementos na fila na ordem inversa
        while pilha:
            self.inserirInicio(pilha.pop())
            


# -------------------------------------------------------
            
    def adicionar_processo(self, processo):
        self.inserirInicio(processo)  # Adiciona o processo no final da fila
        
    def matar_processo_maior_espera(self):
        if self.head():
            print("A fila de processos está vazia!")
            return
        
        atual = self.inicio





        anterior = None





        maior_espera = atual.dado["wait"]





        nodo_maior_espera = atual





        anterior_maior_espera = None
        





        while atual is not None:





            if atual.dado["wait"] > maior_espera:





                maior_espera = atual.dado["wait"]





                nodo_maior_espera = atual





                anterior_maior_espera = anterior





            anterior = atual





            atual = atual.proximo
        





        # Remover o nodo com maior espera





        if nodo_maior_espera == self.inicio:





            self.inicio = self.inicio.proximo  # Se for o primeiro, remove da frente





        else:





            anterior_maior_espera.proximo = nodo_maior_espera.proximo  # Remove do meio ou fim
        





        print(f"Processo com maior espera {nodo_maior_espera.dado['id']} removido.")
        





    def executar_processo(self):





        processo_removido = self.remover()





        if processo_removido is not None:





            print(f"Processo {processo_removido['id']} executado.")
            





    def imprimir_processos(self):





        atual = self.inicio





        while atual is not None:





            print(f"Processo ID: {atual.dado['id']}, Prioridade: {atual.dado['priorety']}, Espera: {atual.dado['wait']}")





            atual = atual.proximo







# Exemplo de uso das funcionalidades






fila = fila()






# Adicionar processos





processo1 = {"id": 101, "name": "Processo A", "priorety": 4, "wait": 10}





processo2 = {"id": 102, "name": "Processo B", "priorety": 2, "wait": 30}





processo3 = {"id": 103, "name": "Processo C", "priorety": 1, "wait": 50}






fila.adicionar_processo(processo1)





fila.adicionar_processo(processo2)





fila.adicionar_processo(processo3)






# Imprimir processos





fila.imprimir_processos()






# Matar processo com maior espera





fila.matar_processo_maior_espera()






# Executar o primeiro processo





fila.executar_processo()






# Imprimir a fila restante





fila.imprimir_processos()








