n=eval(input("Introduceti un numar: "))
s=0
for i in range(1,n):
    if ((i%3==0)and(i%5==0)):
        s+=i
print("suma este:", s)