#Crie um programa para mostrar qual é o de
# caractere que o usuario está informando

valor = input('Digite um valor: ')

print("O valor é: ", type(valor))
print('O valor digitado é númerico ?',valor.isnumeric())
print("O valor é alphabetico ?", valor.isalpha())
