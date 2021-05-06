
def NumeroPrimo (n):
    np=0  # contador para não primo
   
    a=0   
    for a in range (1,n+1):
        res= n % a
        if res == 0:
            np += 1
            print(res)
    
    if np > 2 :
        print('')
        print(n,' não é Primo!')
    else:
        print('')
        print(n,' é Primo!')

n=int(input('Digite um número inteiro:'))

NumeroPrimo (n)
     
     
    
        
