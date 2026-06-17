coloniaA= 4
coloniaB= 10
dias=0
while coloniaB>=coloniaA:
     coloniaA+= float(0.03 * coloniaA)
     coloniaB+=float(0.015 * coloniaB)
     dias+=1

print(f"A colônia A levou {dias} dias para superar a colônia B")
