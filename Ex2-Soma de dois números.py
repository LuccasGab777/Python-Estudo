#Crie um programa que soma dois números informado pelo úsuario


print("Informe dois valores para somar")
soma1 = float (input ("Primeiro valor:"))
soma2 = float (input ("Segundo valor:"))
somaTotal = soma1+soma2
print('A soma entre',soma1,' e ',soma2,' é: ',somaTotal)

#Eu usei 'float' para declarar o número informado pelo usuario como um número decimal
#Pois se eu não usar 'float' ou 'int', o valor informado pelo usuario irá se juntar
#Número informado pelo usuario sem declarar 'float' ou 'int'. ex: 2+2=22
#Número informado pelo usuario usando 'float' ou 'int'. ex: 2+2=4
