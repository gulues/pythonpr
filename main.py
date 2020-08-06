import sympy.ntheory as nt 
###############################
###############################
def countPrimes(primo,anterior):
    count=0
    nt
    prime=int(primo)
    for i in range(anterior, prime):
        if (nt.isprime(i)):
            count=count+1
    return count

if __name__ == "__main__":
    file = open('.\merssene.txt')
    lista = file.readline().split(",")
    itemAnterior=1
    for l in lista:
        print(l + ": " + str(countPrimes(l,itemAnterior)))
        itemAnterior=int(l) 