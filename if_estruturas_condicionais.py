# Exercício 1: Validação de Investimento (Setor Financeiro) Uma corretora de valores
# quer automatizar a recomendação básica de perfil. Crie um programa que peça ao usuário o
# valor que ele deseja investir.
# 1. Se o valor for menor que R$ 1.000,00, exiba: "Perfil iniciante: Sugerimos Tesouro
# Direto".
# 2. Se o valor for entre R$ 1.000,00 e R$ 5.000,00 (inclusive), exiba: "Perfil moderado:
# Sugerimos Fundos Imobiliários".
# 3. Se o valor for acima de R$ 5.000,00, exiba: "Perfil arrojado: Sugerimos Ações".
# *Lembre-se de tratar o input caso o usuário digite "R$" ou use vírgula.*

print("\nExercício 1:")
investimento = input("Valor do investimento: ")
investimento = investimento.replace("R$","").replace(",",".").replace(".","").replace(" ","").strip()
investimento = float(investimento)
print(investimento)
if investimento < 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto")
elif investimento > 1000 and investimento <= 5000:
    print("Perfil moderado: Sugerimos Fundos Imobiliários")
elif investimento > 5000:
    print("Perfil arrojado: Sugerimos Ações")


# --------------------------------------------------------------------------------------

# Exercício 2: Controle de Acesso ao Sistema (Setor de Segurança) Você tem uma lista
# de e-mails de administradores: admins = ["ana@empresa.com",
# "guilherme@empresa.com", "felipe@empresa.com"]. Crie um programa que peça
# o e-mail do usuário. O programa deve:
# 1. Padronizar o e-mail (letras minúsculas e sem espaços).
# 2. Verificar se o e-mail está na lista de admins.
# 3. Se estiver, exibir: "Acesso liberado! Bem-vindo ao painel de controle".
# 4. Caso contrário, exibir: "Acesso negado. Você não tem permissões de administrador".

print("\nExercício 2:")
admins = ["ana@empresa.com","guilherme@empresa.com", "felipe@empresa.com"]
email = input("Digite email: ")
email = email.lower()
verificacao = email in admins
if verificacao == True:
    print("Acesso liberado! Bem-vindo ao painel de controle")
else:
    print("Acesso negado. Você não tem permissões de administrador")

# --------------------------------------------------------------------------------------

# Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas) Um e-commerce
# aplica descontos automáticos no carrinho. Crie um programa que receba o valor total da
# compra e aplique a seguinte lógica:
# ● Compras a partir de R$ 500,00: 15% de desconto.
# ● Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
# ● Compras abaixo de R$ 200,00: Sem desconto. O programa deve exibir o valor do
# desconto e o valor final a pagar, formatados em R$.

print("\nExercício 3:")
valor_total_compra = float(input("Digite o valor da compra: "))
if valor_total_compra > 500.00:
    desconto = valor_total_compra * 0.15
    valor_final = valor_total_compra - desconto
elif valor_total_compra > 200 and valor_total_compra < 500:
    desconto = valor_total_compra * 0.1
    valor_final = valor_total_compra - desconto
else:
    desconto = 0.00
    valor_final = valor_total_compra
print(f"Valor total da compra: {valor_total_compra:.2f}\nDesconto: {desconto:.2f}\nValor Final: {valor_final:.2f}")

# --------------------------------------------------------------------------------------

# Exercício 4: Análise de Metas Combinadas (Setor Comercial) Uma empresa paga bônus
# se a meta individual do vendedor E a meta da loja forem batidas.
# 1. Peça as vendas do vendedor e a meta individual dele.
# 2. Peça as vendas totais da loja e a meta da loja.
# 3. Se o vendedor bater a meta dele E a loja bater a meta total, o bônus é de 20% sobre
# as vendas do vendedor.
# 4. Caso contrário, o bônus é zero. Exiba a mensagem: "Seu bônus este mês é de:
# R$[valor]".

print("\nExercício 4:")
vendas_vendedor = float(input("Valor total das suas vendas: "))
meta_vendedor = float(input("Digite sua meta: "))
print ("-" * 30)
venda_total = float(input("Total em vendas na loja: "))
meta_loja = float(input("Meta da loja: "))
if vendas_vendedor >= meta_vendedor and venda_total >= meta_loja:
    bonus = vendas_vendedor * 0.2
else:
    bonus = 0
print ("-" * 30)
print(f"Seu bônus este mês é de: R$ [{bonus:.2f}].")


# --------------------------------------------------------------------------------------

# Exercício 5: Sistema de Triagem de E-mails (Setor de Customer Experience) Crie um
# sistema que ajude a filtrar para qual departamento uma reclamação deve ir. O usuário deve
# digitar o assunto do e-mail.
# ● Se no assunto aparecer a palavra "pagamento" ou "boleto", exiba: "Encaminhado
# para o Financeiro".
# ● Se no assunto aparecer a palavra "entrega" ou "atraso", exiba: "Encaminhado para a
# Logística".
# ● Caso não seja nenhum desses, exiba: "Encaminhado para o Suporte Geral". Dica:
# Use o operador in para verificar se a palavra está dentro do texto.

print("\nExercício 5:")
assunto = input("Assunto: ")
assunto = assunto.lower()
# if assunto == "pagamento" or assunto == "boleto":
#     print("Encaminhado para o Financeiro.")
# elif assunto == "entrega" or assunto == "atraso":
#     print("Encaminhado para a Logística")
# else:
#     print("Encaminhado para o Suporte Geral")
if "pagamento" in assunto or "boleto" in assunto:
    print("Encaminhado para o Financeiro.")
elif "entrega" in assunto or "atraso" in assunto:
    print("Encaminhado para a Logística")
else:
    print("Encaminhado para o Suporte Geral")

print("")