class nodolista:
    def __init__(self,dado = 0, proximo_nodo= None):
        self.dado = dado
        self.proximo = proximo_nodo
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class listaEncadeada:
    def __init__(self):
        self.cabeca = None
    def __repr__(self):
        return "[" + str(self.cabeca) +"]"

    def isere_no_inicio(self, novo_dado):
        novo_nodo = nodolista(novo_dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo

    def mostrar_cabeca (self):
        return  "[" + str(self.cabeca.dado) +"]"

    def busca(self, valor):
        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        return corrente
    
    def remove(self, valor):
        corrente = self.cabeca
        ponteiroAterior = None
        
        while corrente and corrente.dado != valor:
            ponteiroAterior = corrente
            corrente = corrente.proximo
        
        ponteiroAterior.proximo = corrente.proximo
        print("agr foi kkk")
        
    def removeDuplicada(self):
        corrente = self.cabeca
        
        while corrente and corrente.proximo:
            if corrente.dado == corrente.proximo.dado:
                corrente.proximo = corrente.proximo.proximo
            else: 
                corrente = corrente.proximo
                
                
    def teste(self):
        corrente = self.cabeca
        
        print(corrente)
        print(corrente.dado)
        print(corrente.proximo)
        print(corrente.proximo.dado)
        print(corrente.proximo.proximo)
        





l = listaEncadeada()
l.isere_no_inicio(4)
l.isere_no_inicio(5)
l.isere_no_inicio(5)
l.isere_no_inicio(6)
l.isere_no_inicio(7)
# print(l)


print(l.teste())


# print(l)
# print(l.mostrar_cabeca())
