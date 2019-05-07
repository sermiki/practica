
def cantidad(num):
    n=num
    cont=0
    while (num>0):
        num=num/10
        cont+=1
    print("la cantidad del numero es", cont)
        
n=int(input("escribe el numero"))
numero=cantidad(n)

