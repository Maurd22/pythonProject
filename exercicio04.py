from operator import itemgetter

list = [] #lista
itens = dict() #dicionário

def registerProduct(): #função para colocar os itens do dicionário dentro da lista usando método append()
    list.append(itens.copy())

dado = int(input('Gostaria de cadastrar um produto?  0 - Não   1 - sim : ')) #inicia o programa

while dado != 1 and dado != 0: #caso o dado seja diferente de 1 ou 0
    print('Opção invalida!')
    dado = int(input('Gostaria de cadastrar um produto?  0 - Não   1 - sim : '))

while dado == 1: #caso o dado seja 1
    itens['codigo'] = int(input('Digite o código do produto: ')) #1º item do dicionário

    if itens['codigo'] == 0: #encerra o programa caso o código do produto seja 0
        print('Código 0! o programa será encerrado.')
        break

    itens['estoque'] = int(input('Digite o estoque: ')) #2º item do dicionário
    itens['minimo'] = int(input('Mínimo necessário: ')) #3º item do dicionário

    registerProduct() #chamada da função

    dado = int(input('Gostaria de cadastrar um produto?  0 - Não   1 - sim : '))

    while dado != 1 and dado != 0: #caso o dado seja diferente de 1 ou 0
        print('Opção invalida!')
        dado = int(input('Gostaria de cadastrar um produto?  0 - Não   1 - sim : '))

ordenedList = sorted(list, key=itemgetter('codigo')) #variável para oerdenar a lista de forma crescente
                                                     #usando o valor do código do produto

for product in ordenedList: #laço de repetição para imprimir a lista ordenada
    print(product)








if dado == 0:
    print('Programa encerrado.')


