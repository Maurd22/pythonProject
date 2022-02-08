def email(): #função para coletar nome e sobrenome
    nome = input('Digite seu nome: ')
    sNome = input('Digite seu sobrenome: ')
    ru = input('Digite seu RU: ')
    if nome.upper() and sNome.upper(): #if para deixar os caracteres minúculos para serem concatenados com email
        nome2 = nome.lower()
        sNome2 = sNome.lower()
    print('Sr(a). {} {}, seu email é {}{}{}@algoritimos.com.br'.format(nome.capitalize(), sNome.capitalize(), nome2[0], sNome2, ru))
    #usei o método capitalize() apra deixar as primeiras letras do nome e sobrenome maiúsculas
email() #Chamada da função
