n1=int(input("Digite um número: "))
n2=int(input("Digite um número: "))
n3=0
if n1> n2:
  n3=n1
  n1=n2
  n2=n3

for i in range(n1,n2+1):
        print(i)
