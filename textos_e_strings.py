# Exercício 1: Relatório de Margem de Lucro (Setor Financeiro) Uma empresa de varejo
# precisa de um resumo rápido sobre a performance de um produto. Dado o faturamento de
# R$ 45.000,00 e o custo de R$ 23.500,00, crie um programa que calcule o lucro e a margem
# de lucro (lucro dividido pelo faturamento). Exiba uma mensagem formatada onde o lucro
# use o separador de milhar e duas casas decimais, e a margem seja exibida como uma
# porcentagem inteira.

faturamento = 45000
custo = 23500
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print ("\nExercício 1:")
print (f"O lucro foi de {lucro:,.2f}") #Para mudar formatação de textos(strings) e fazer a incorporação de váriaveis mais facilmente a resposta usar o f de format fora da string para formatar, o {} para adicionar variável, : para indicar qual é a formatação daquela variável.
print (f"A margem de lucro foi de {margem_lucro:.0%}")

# Exercício 2: Padronização de Dados de CRM (Setor de Vendas) Um vendedor cadastrou
# um cliente com os dados desorganizados no sistema: nome = " mArCoS aNtOnIo
# rOcHa " e email = " MARCOS.ROCHA@GMAIL.COM ". Para evitar duplicidade e erros
# de envio, você deve:
# 1. Remover os espaços extras no início e fim das duas variáveis.
# 2. Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo
# (formato de nome próprio).
# 3. Deixar o e-mail todo em letras minúsculas. Exiba os resultados finais no console.

nome =  " mArCoS aNtOnIo "
email ="  MARCOS.ROCHA@GMAIL.COM "

nome = nome.title()
email = email.lower()

# Para formatar strings utilizamos funções prontas do python.
# Para alterar a escrita em si:
# upper -> Todas maiúsculas.
# lower -> Todas minúsculas.
# capitalize -> Primeira letra da string maiúscula.
# title -> Primeira linha de cada palavra maiúscula.
# swapcase -> Inversão de estado(maiúsculo por minúsculo e vice-versa)

nome = nome.strip()
email = email.strip()

# isupper -> Verifica se todos os caracteres são maiúsculos
# islower -> Verifica se todos os caracteres são minúsculos
# istitle -> Verifica se a string segue o formato de título 
# strip -> Remove espaços em branco do início e do final da string
# split -> Divide a string em uma lista, útil para manipular pedaços dela

print ("\nExercício 2:")
print (f"Nome: {nome}\nEmail: {email}")

# Exercício 3: Migração de Servidor de E-mail (Setor de TI) Sua empresa mudou de nome
# e todos os funcionários que usavam o domínio @empresa.com.br agora devem usar o
# domínio @grupocorp.com. O e-mail do funcionário é andre_silva@empresa.com.br.
# Crie um código que substitua automaticamente o domínio antigo pelo novo e exiba o novo
# endereço de e-mail.



# Exercício 4: Extração de Username para Log (Setor de Segurança) Para criar um log de
# acessos, o sistema precisa extrair apenas a parte do nome do usuário de um e-mail
# corporativo (tudo o que vem antes do @). Dado o e-mail
# beatriz.oliveira@grupocorp.com, use a função .find() e o fatiamento de texto
# para extrair e exibir apenas o nome beatriz.oliveira.



# Exercício 5: Personalização de E-mail de Marketing (Setor de Marketing) O marketing
# quer enviar um e-mail de boas-vindas. O cliente forneceu o nome completo: lucas
# ferreira souza. Você deve extrair apenas o primeiro nome para usar na saudação (ex:
# "Olá, Lucas!"). O código deve:
# 1. Encontrar a posição do primeiro espaço.
# 2. Fatiar o texto para pegar apenas o primeiro nome.
# 3. Formatar o nome com a primeira letra maiúscula.
# 4. Exibir a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"



# Print para deixar esteticamente organizado no terminal
print("")