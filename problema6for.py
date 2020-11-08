#Să se calculeze sumele: 	s1=1+2+3+…+n
#			s2=1*2+2*3+3*4+…+(n-1)*n
#			s3=1+1*2+1*2*3+…+1*2*3*…*n
#			s4=12+22+32+…+n2
#			s5=1/2+2/3+3/4+…+n/(n+1)
#			s6=1+2+22+23+24+…+2n
#			Notă: Pentru fiecare sumă n – se va citi de la tastatură.
n=eval(input("Introduceti un numar: "))
s1=0
for i in range(1,(n+1)):
    s1+=i
print("suma1 este:", s1)
n=eval(input("Introduceti un numar: "))
s2=0
for i in range(1,n):
    s2+=(i-1)*i
print("suma2 este:", s2)
n=eval(input("Introduceti un numar: "))
s3 = 1
factorial = 1
for i in range(2, n):
    factorial *= n
    s3 += factorial
print("suma3 este:", s3)
n=eval(input("Introduceti un numar: "))
s4=0
for i in range(1, ((n * 10) + 1)):
    if (i % 10 == 0):
        s4 += (i + 2)
print("suma4 este:", s4)
n=eval(input("Introduceti un numar: "))
s5=0
for i in range(1,n):
    s5=i/(i+1)
print("suma5 este:", s5)
n=eval(input("Introduceti un numar: "))
s6=0
for i in range(1,n):
    s6+=(20+n)
print("suma6 este:", s6)