# Exercício 1: Atualização de Cadastro de Clientes (Setor de CRM) Você tem um
# dicionário com o faturamento acumulado de alguns clientes: clientes = {"Lira":
# 5000, "Alon": 3000, "Julia": 4500}. O cliente "Alon" fez uma nova compra de R$
# 1.500,00. Crie um código que:
# 1. Atualize o valor do cliente "Alon" somando o novo valor ao faturamento antigo.
# 2. Adicione um novo cliente chamado "Marcos" com um faturamento inicial de R$
# 2.000,00.
# 3. Exiba o dicionário atualizado.

print("\nExercício 1:")
clientes = {"Lira":5000, "Alon": 3000, "Julia": 4500}
nova_compra = 1500
clientes["Alon"] = nova_compra
clientes["Marcos"] = 2000
for c, p in clientes.items():
    print (f"{c}: {p:.2f}")
# print(clientes)

# --------------------------------------------------------------------------------------

# Exercício 2: Consulta de Estoque Interativa (Setor de Logística) A empresa possui o
# seguinte estoque: estoque = {"teclado": 50, "mouse": 120, "monitor": 30}.
# Crie um programa que peça para o usuário digitar o nome de um produto.
# 1. Se o produto existir no estoque, exiba a quantidade disponível.
# 2. Se o produto não existir, exiba a mensagem: "Produto não encontrado no sistema".
# Dica: Lembre-se de tratar o input para evitar erros de letras maiúsculas ou espaços.

print("\nExercício 2:")
estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
produto = input("Nome do produto: ")
produto = produto.lower().replace(" ","")
if produto in estoque:
    print(f"Quantidade: {estoque[produto]}")
else:
    print("Produto não encontrado no sistema")

# --------------------------------------------------------------------------------------

# Exercício 3: Análise de Faturamento por Região (Setor Financeiro) Dada a lista de
# faturamento por região: vendas_regiao = {"Norte": 15000, "Sul": 22000,
# "Leste": 18000, "Oeste": 25000}. Seu programa deve:
# 1. Extrair todos os valores (faturamentos) para uma lista.
# 2. Calcular e exibir o faturamento total da empresa (soma de todas as regiões).
# 3. Calcular e exibir o faturamento médio das regiões.

print("\nExercício 3:")
vendas_regiao = {"Norte": 15000, "Sul": 22000,"Leste": 18000, "Oeste": 25000}
faturamento = []
regioes = 0
for regiao, vendas in vendas_regiao.items():
    faturamento.append(vendas)
    regioes = len(regiao)
faturamento_total = sum(faturamento)
faturamento_medio = faturamento_total / regioes
print(f"Uma empresa fatura: R$ {faturamento_total:.2f}\nO faturamento médio dessa empresa por região, considerando que está em {regiao} regiões: R$ {faturamento_medio:.2f}")

# --------------------------------------------------------------------------------------

# Exercício 4: Sistema de RH – Média de Desempenho (Setor de RH) O RH armazena as
# últimas 3 notas de desempenho de cada funcionário em um dicionário: desempenho =
# {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}. O gestor
# quer saber a média da funcionária "Paula". Crie um código que:
# 1. Acesse a lista de notas da "Paula".
# 2. Calcule a média das notas (soma das notas dividida pela quantidade de notas).
# 3. Exiba o resultado: "A média de Paula foi [media]".

print("\nExercício 4:")
desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}
funcionario = "Paula" # Poderia ser um input
# funcionario = input("Digite o nome do funcionário: ")
# funcionario = funcionario.capitalize()
#Evitar erros na verificação
desempenho_funcionario = desempenho[funcionario]
media_funcionario = sum(desempenho_funcionario) / 3
print(f"A média de {funcionario} foi {media_funcionario}.")

# --------------------------------------------------------------------------------------

# Exercício 5: Limpeza de Banco de Dados (Setor de TI) O sistema de e-commerce
# descontinuou alguns produtos. Você tem o dicionário: produtos = {"celular": 1500,
# "camera": 800, "radio": 200, "fone": 100}. O item "radio" deve ser removido
# por estar obsoleto. Crie um código que:
# 1. Remova o item "radio" do dicionário usando o método .pop().
# 2. Imprima o valor do produto que foi removido para fins de log.
# 3. Verifique se o produto "celular" ainda existe no dicionário e imprima True ou False.

print("\nExercício 5:")
produtos = {"celular": 1500,"camera": 800, "radio": 200, "fone": 100}
valor_removido = produtos.pop("radio")
print(f"{valor_removido}, valor excluido com sucesso!")
checado = "celular" in produtos
print(f"Celular: {checado}")

print("")