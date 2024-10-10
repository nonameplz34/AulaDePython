class nodolista:
    def __init__(self ,dado = 0, proximo_nodo= None): #change, self.proximo = proximo_nodo  to private later
        self.dado = dado
        self.proximo = proximo_nodo
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class listaEncadeada:

    def __init__(self):
        self.cabeca = None

    def __repr__(self):

        return "[" + str(self.cabeca) +"]"

    def addOnTheStart(self, novo_dado):
        novo_nodo = nodolista(novo_dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo

    def showHead (self): #change to getter later
        return  "[" + str(self.cabeca.dado) +"]"

    def search(self, valor): #change to getter later

        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        return corrente
    
    def remove(self, valor): #change to setter later
    


        corrente = self.cabeca
        ponteiroAterior = None

        while corrente and corrente.dado != valor:



            ponteiroAterior = corrente



            corrente = corrente.proximo
        




        ponteiroAterior.proximo = corrente.proximo



        print("agr foi kkk")
        
    def removeDuplicate(self):




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
l.addOnTheStart(4)
l.addOnTheStart(5)
l.addOnTheStart(5)
l.addOnTheStart(6)
l.addOnTheStart(7)

print(l)

print(l.showHead())




