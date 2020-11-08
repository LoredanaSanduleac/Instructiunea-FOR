#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele pare, pentru intervalul de la 1 la n (n-este citit de la tastatură).
n=eval(input("Introduceti un numar: "))
c=0
for i in range(2,n,2):
    c+=2
    print(i)
