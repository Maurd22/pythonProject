dado = int(input('Inserir dados? 0 - Não     1 - Sim : ')) #pedindo a confirmação
while dado != 0 and dado != 1: #caso a opção seja divergente de 1 ou 0
    print('Opção inválida')
    dado = int(input('Inserir dados? 0 - Não     1 - Sim : '))

while dado == 1: #opção para rodar o código
   nome = input('Nome do aluno: ')
   nota = float(input('Nota final: '))

   while nota > 10 or nota < 0: #caso a nota seja maior ou menor que 10
      print('Nota inválida')
      nota = float(input('Nota final: '))

   if nota == 0 or nota <= 2.9: #parametros das notas
     print('O aluno {} tirou nota {} e se enquadra no conceito E.'.format(nome, nota))
   elif nota == 3 or nota <= 4.9:
     print('O aluno {} tirou nota {} e se enquadra no conceito D.'.format(nome, nota))
   elif nota == 5 or nota <= 6.9:
     print('O aluno {} tirou nota {} e se enquadra no conceito C.'.format(nome, nota))
   elif nota == 7 or nota <= 8.9:
     print('O aluno {} tirou nota {} e se enquadra no conceito B.'.format(nome, nota))
   elif nota == 9 or nota <= 10:
     print('O aluno {} tirou nota {} e se enquadra no conceito A.'.format(nome, nota))

   dado = int(input('Inserir dados? 0 - Não     1 - Sim : '))

   while dado != 0 and dado != 1: #caso a opção seja divergente de 1 ou 0
       print('Opção inválida')
       dado = int(input('Inserir dados? 0 - Não     1 - Sim : '))



if dado == 0: #encerra o programa
    print('Programa encerrado.')







