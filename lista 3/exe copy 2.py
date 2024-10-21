# 2) Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci. Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89... 






def fibanachiiii (n): 
    if n == 0:
        return 0
    elif n == 1:        
        return 1
    else:
        calculo = fibanachiiii(n-1) +  fibanachiiii(n-2)
        return calculo 
    
    
    
resultado = fibanachiiii(12)
print(resultado)