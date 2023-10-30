# Código que calcula la nota acomulada del semestre

lista=[50,50,45,48,0,0]
porcentaje=[0.05,0.1,0.2,0.06,0.06,0.03]
notafinal=0

for i in range(len(lista)):
    nota= lista[i]*porcentaje[i]
    notafinal=notafinal+nota
print ('Nota acomulada =',notafinal)
