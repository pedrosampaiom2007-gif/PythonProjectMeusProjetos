def media(notas:list):
   """Esta função analisa uma lista e remove o maior e menor valor dela e após isso calcula a média das notas restantes, excelente para analisar notas de provas de manobra"""
   a=max(notas)
   b=min(notas)

   notas.remove(a)
   notas.remove(b)

   media_calc=sum(notas)/len(notas)

   return media_calc

lista=[]

for nota in range(0,5):
    while True:
     info=int(input("Digite as próximas 5 notas do competidor de 0 a 10: \n"))

     if info >= 0 and info <= 10:

         lista.append(info)
         break
     else:
         print("Digite uma nota de 0 a 10!")


print("-"*30)
nota_final=(media(lista))

print(f"A nota final da manobra foi {nota_final:.2f}")







