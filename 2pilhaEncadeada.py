class Nodo:
    def __init__(self,dado = 0, nodo_anterior = None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)
    
class Pilha:
    def __init__(self):
        self.topo = None
    def __repr__(self):
        return "[" + str(self.topo) +"]" 
    
    def insere(self, novo_dado): #✅ funcionando
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo
        
    def remove(self): #✅ funcionando
        assert self.topo, "impossivel remover valor de pilhaa vazia"
        self.topo = self.topo.anterior
    
    def maiorElemento(self): #✅ funcionando
        corrente = self.topo
        maior = corrente.dado
        
        while corrente != None:
            if corrente.dado > maior:
                maior = corrente.dado
            corrente = corrente.anterior    
        print(maior)
    
    def inverso(self): #✅ funcionando
        # 2.Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.
        corrente = self.topo
        novaPilha = Pilha()
        
        while corrente != None:
            novaPilha.insere(corrente.dado)
            corrente = corrente.anterior
        print(novaPilha)
        
    def saoIguais(self, ele1, ele2): #🛑 terminado, não esta funcionado
        ### 3. Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais. Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.  
            ele1 = Nodo(ele1)
            ele2 = Nodo(ele2)

        # --------------- tive uma dificuldade com o ele1.dado e ele1 sozinho , no caso ele1 é o ponteiro e ele1.ddo e int ?
        # -------------tava chando o ele1 de pilha em vez de nodo
            while ele2 is not None and ele1 is not None:
                
                if ele1.dado != ele2.dado:
                    print("são diferentes :(")
                ele1 = ele1.anterior
                ele2 = ele2.anterior
        
            if  ele2 is not None and ele1 is not None:
                print( "as pilhas são iguais :)")
    
    # -------------------------------------create new class,( fix code fisrt)-------------------------------------------------------
    
    def TPilha(self, vetorInteiros): #❔ trabalhando atualmente
        # 5. Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos. Para cada um deles, como segue: 
        # Se o número for par, insira-o na pilha; 
        # Se o número lido for ímpar, retire um número da pilha; 
        # Ao final, esvazie a pilha imprimindo os elementos.

        pass 
    
    def TPilha(self, N, P):
        # 6. Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um: 
        # se positivo, inserir na pilha P; 
        # se negativo, inserir na pilha N; 
        # se zero, retirar um elemento de cada pilha.
        pass 
    
# -------------------------------------create new class,( fix code fisrt)-------------------------------------------------------

    def wherreCar(self, rua, placa):  #✅ funcionando
        # 4.
        # Armazene as placas (apenas os números) que estão estacionados numa rua sem saída estreita. 
        # Dado uma placa verifique se o carro está estacionado na rua. 
        # Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair. verificador e adicionador em lista 
        
        # codigo anterior🔽
            # # rua = self.topo
            #     rua = Nodo(rua)
            #     # ⬆ isso me confunde um pouco, não estou entendo como usar
            #     counter = 0
                
            #     while rua.dado is not None and placa != rua.dado:
            #         rua.dado = rua.anterior.dado
            #         counter += 1

        rua = self.topo
        # rua = Nodo(rua)
        # ⬆ isso me confunde um pouco, não estou entendo como usar
        counter = 0
        while rua is not None and placa != rua.dado:
            rua = rua.anterior
            counter += 1
    
        if rua.dado != placa:
            print("essa placa nã esta nessa rua")
        else: 
            print(f"vão precisar sair {counter} carros para esse sair")
                    
        

    

x=Pilha()
x.insere(1)
x.insere(5)
x.insere(3)
x.insere(7) 

y=Pilha()
y.insere(1)
y.insere(5)
y.insere(3)
y.insere(7)



# x.saoIguais(y , x)
x.wherreCar(x, 3)
# print(x)
# x.inverso()
# --------------- x ja é uma pilha bobinho jkkkkjkjkjk
# --------------- como faço para aparecer os hits da ide quando for colocar os parametros?, no vs code 

