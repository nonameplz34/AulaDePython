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
    
    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo
        
    def remove(self):
        assert self.topo, "impossivel remover valor de pilhaa vazia"
        self.topo = self.topo.anterior
    
    def maiorElemento(self):
        corrente = self.topo
        maior = corrente.dado
        
        while corrente != None:
            if corrente.dado > maior:
                maior = corrente.dado
            corrente = corrente.anterior    
        print(maior)
    
    def inverso(self):
        corrente = self.topo
        novaPilha = Pilha()
        
        while corrente != None:
            novaPilha.insere(corrente.dado)
            corrente = corrente.anterior
        print(novaPilha)
            # 2.Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.

    def saoIguais(self, ele1, ele2):
        pilha1 = ele1.topo
        pilha2 = ele2.topo
        
        
        

        while pilha1.dado == pilha2.dado:
                pilha1.dado = pilha1.anterior.dado
                pilha2.dado = pilha2.anterior.dado
                print(f"{pilha1.dado} é igual a {pilha2.dado}")
        print("saiu")
        
        # 3. Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais. Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.  
    
    def cadeCarro(self, placa, rua):    
        # 4.
        # Armazene as placas (apenas os números) que estão estacionados numa rua sem saída estreita. (placa = nodo da pilha)
        # Dado uma placa verifique se o carro está estacionado na rua. (pilha = rua)
        # Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair. ( loop com verificador e adicionador em lista (posivelmente ivertida por conta do lifo))
        pass    
    
    def TPilha(self, vetorInteiros):
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
    
x=Pilha()

x.insere(1)
x.insere(5)
x.insere(3)

print(x)

y=Pilha()

y.insere(1)
y.insere(5)
y.insere(3)

print(y)
y.saoIguais(x, y)

