gastos=[2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

produtos_acima_de_3000=0
quantidade_de_produtos=len(gastos)


for i in gastos:
   if i>3000:
       produtos_acima_de_3000+=1


porcentagem= produtos_acima_de_3000*100
resultado_final= (porcentagem * quantidade_de_produtos)/100

print(f"A porcentagem é: {resultado_final}%")
print(f"Tem {produtos_acima_de_3000} produtos acima de 3000 reais\n")




