def main():

 print('SDM, Seu dinheiro em boas mãos\n')

 nome = input('Cadastro\nInforme o seu nome:')

 senha = input('Informe a sua senha:')

 #fiz um laço de repetição usando while
 # coloquei aspas no '1234' para declarar que ele é uma string
 while senha != '1234':
   senha = input ('Senha invalida, por favor digite novamente:')

 #se a senha digitada pelo usuario for igual a "1234" saí do laço de repetição
 print('Seja bem vindo(a) {}'.format(nome))

 saldo = 0.0 # O uso do  0.0, indica que é um número decimal float
 extrato = [] # O uso dos [] é para atribuir uma lista vazia
 escolha = "" # O uso das aspas vazias indica que é uma String sem vazia


 while True:
    escolha = menu()

    if escolha == '1':
      verSaldo(saldo,nome)
    elif escolha == '2':
      saldo,extrato = verDeposito(saldo,extrato,nome)#"o saldo,extrato = a 'função' é usado pois tem lista
    elif escolha == '3':
      saldo,extrato = sacar(saldo,extrato,nome)
    elif escolha == '4':
      verExtrato(extrato,nome)
    elif escolha == '5':
      sair(nome)
      break
    else:
      print("Opção invalida")

def menu():
  print('Escolha uma opção')
  print('1 -> Ver Saldo')
  print('2 -> Depositar')
  print('3 -> Sacar')
  print('4 -> Extrato')
  print('5 -> Sair')
  return input("")




def verSaldo(saldo,nome):
   print('Seu saldo atual é: {:.2f}'.format(saldo))
   #A expressão {:.2f} coloca 2 digito em um valor float. Por exemplo 10.5011 -> 10.50


def verDeposito(saldo, extrato,nome):
  deposito =float (input('Informe o valor do desposito: R$'))
  while deposito < 0: # Enquanto o deposito for menor que zero, repete a string
    deposito = float (input ('Deposito invalido, tente novamente!\nDigite o valor: R$'))

  saldo += deposito
  print(f'deposito realizado com sucesso!\nSaldo atual:{saldo:.2f}')
  extrato.append(f'Deposito: R${deposito:.2f}')
  # O f (f-string) antes das aspas simples('') é usado para colocar variavél dentro da string
  # A função append deposita um valor na lista, nesse caso estou adicionando o valor na lista extrato[]
  return saldo, extrato


def sacar(saldo,extrato,nome):
    saque = float (input('Informe o valor de saque:R$'))
    while saque < 0 or saque > saldo:
        saque = float (input('Saque invalido, por favor digite novamente!\nDigite o valor: R$'))

    saldo -= saque
    print(f'Saque realizado com sucesso!\nSaldo atual:{saldo:.2f}')
    extrato.append(f'Saque: R${saque:.2f}')
    return saldo, extrato


def verExtrato(extrato,nome):
  print('extrato')

  if extrato:
     for i in extrato:
       print (i)
  else:
   print("{},nenhuma movimentação registrada".format(nome))


def sair(nome):
    print ('{}, Volte sempre!'.format(nome))

if __name__ == '__main__':
     main()