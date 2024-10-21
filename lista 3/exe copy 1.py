def factorial (n): #  aaaaaaaaaaaaaaah por isso return é importante 
    if n == 0:
        return 1
    else:
      return  n * factorial(n-1)
    
resultado = factorial(5)
print(resultado)