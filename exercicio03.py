import random #importei o método ramdom

list = [] #lista onde será armazenada os nomes dos doadores

def doador(nome: str, doacao: float): #função que adiciona os nomes usando coeficiente de 10
     list.extend(((nome + ' ') * int(doacao // 10)).split())
#estendi a lista para receber nomes e multipliquei pelo coeficiente de 10

def sorteio():
     random.shuffle(list) #embaralha lista
     print(list)
     ganhador = random.choice(list) #sorteia ganhador
     print('O vencedor é {}'.format(ganhador))


dado = int(input('Gostaria de doar?  0 - Não   1 - sim : '))

while dado != 0 and dado != 1: #caso a opção seja divergente de 1 ou 0
    print('Opção inválida')
    dado = int(input('Inserir dados? 0 - Não     1 - Sim : '))

while dado == 1: #esse laço inicia o algorítimo
    nome1 = input('Qual seu nome? ')
    doacao1 = float(input('Quanto gostaria de doar? '))

    while doacao1 < 10: #caso o valor da doação seja menor que 10
        print('Valor inválido, R$10,00 é o valor mínimo')
        doacao1 = float(input('Quanto gostaria de doar? '))

    doador(nome1, doacao1) #chamada da função pra adicionar nomes na lista

    dado = int(input('Gostaria de doar?  0 - Não   1 - sim : '))

    while dado != 0 and dado != 1:  # caso a opção seja divergente de 1 ou 0
        print('Opção inválida')
        dado = int(input('Inserir dados? 0 - Não     1 - Sim : '))


if dado == 0: #encerra o programa
    print('Programa encerrado')

sorteio() #chamada da função de sorteio