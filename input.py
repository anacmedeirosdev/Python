# Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal) Uma empresa de
# serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. Como o
# valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
# 1. Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
# 2. Limpar o texto removendo o "R$" e trocando a vírgula por ponto.
# 3. Converter para número decimal (float).
# 4. Calcular o valor do imposto (15% do valor bruto).
# 5. Exibir uma mensagem formatada com f-string mostrando o valor do imposto com
# duas casas decimais.

print("\nExercício 1:")
# valor_bruto = input("Valor bruto: ")
# valor_bruto = valor_bruto.replace(".","")
# valor_bruto = valor_bruto.replace(",",".")
# valor_bruto = valor_bruto.replace("R$","")
# valor_bruto = valor_bruto.strip()
# valor_bruto = float(valor_bruto)

#De forma mais simplificada
valor_bruto = input("Valor bruto: ")
valor_bruto = float(valor_bruto.replace(".","").replace(",",".").replace("R$","").strip())
imposto = valor_bruto * 0.15
print (f"Imposto: {imposto:.2f}")



# --------------------------------------------------------------------------------------

# Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH) Ao cadastrar um novo
# funcionário, o RH precisa extrair o primeiro nome para criar um crachá e padronizar o
# e-mail. Crie um programa que:
# 1. Peça o nome completo do colaborador.
# 2. Peça o e-mail pessoal do colaborador.
# 3. Extraia o primeiro nome (deixe-o com a primeira letra maiúscula).
# 4. Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas).
# 5. Exiba a mensagem: "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail
# padronizado]".

print("\nExercício 2:")
print("----Preencha os seguintes dados.----")
nome_completo = input("Nome completo: ")
email_pessoal = input("Email pessoal: ")
nomes = nome_completo.lower().split()
primeiro_nome = nomes[0].capitalize()
email_padronizado = email_pessoal.strip().lower().replace(" ","")
print(f"Cadastro concluído: {primeiro_nome}.\nE-mail de acesso: {email_padronizado}.")

# --------------------------------------------------------------------------------------

# Exercício 3: Análise de Metas de Vendas (Setor Comercial) Um gerente quer comparar o
# desempenho de duas filiais. O programa deve:
# 1. Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário pode digitar
# números decimais).
# 2. Calcular o faturamento total das duas lojas.
# 3. Calcular a média de faturamento entre elas.
# 4. Exibir uma única mensagem formatada informando o total e a média, utilizando o
# separador de milhar e duas casas decimais.

print ("\nExercício 3:")
faturamento_a = float(input("Faturamento da Loja A: "))
faturamento_b = float(input("Faturamento da Loja B: "))
faturamento_total = faturamento_a + faturamento_b
faturamento_medio = faturamento_total / 2

print(f"O faturamento total foi {faturamento_total:.2f} e o faturamento médio entre as lojas foi {faturamento_medio:.2f}")

print("")