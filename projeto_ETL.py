import csv

#Extract: Ler e extrair as informações do arquivo CSV.

arquivo =  open('users.csv')
dados = csv.reader(arquivo)

#Transform: Verificar perfil de cada cliente e oferecer opções de investimento compatíveis.

lista = list()
for dado in dados:
     if dado[4] == 'conservador':
          dado.append('Temos investimentos seguros ou de baixo risco para lhe oferecer!')
          lista.append(dado)
     elif dado[4] == 'moderado':
          dado.append('Temos investimentos seguros com menor retorno ou de risco mediano com maior retorno para lhe oferecer!')
          lista.append(dado)
     elif dado[4] == 'arrojado':
          dado.append('Temos investimentos com alta rentabilidade e renda variavel para lhe oferecer!')
          lista.append(dado)
     else:
          dado.append('mensagem')
          lista.append(dado)

#Load: Criar um novo arquivo com uma mensagem para cada cliente.

novo_arquivo =  open('resultado.csv', 'w', newline='')
mensagem = csv.writer(novo_arquivo, delimiter=',')
mensagem.writerows(lista)

arquivo.close()
novo_arquivo.close()
