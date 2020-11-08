#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru intervalul de la a la b (a și b se citesc de la tastatură).
a=eval(input("Introduceti un numar: "))
b=eval(input("Introduceti un numar: "))
c=1
for i in range(a,b,2):
    c+=2
    print(i)
