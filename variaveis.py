# Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)
# Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a
# equipe de vendas. Objetivo: Calcule o valor do bônus e o faturamento final da empresa
# após subtrair esse bônus.
# ● Faturamento inicial: 50.000
# ● Percentual de bônus: 0.10

faturamento = 50000
bonus = 50000 * 0.1
faturamento_final = faturamento + bonus

print ("\nExercício 1:")
print ("O faturamento final da empresa é de R$",faturamento_final)

# Exercício 2: Controle de Estoque de E-commerce (Logística)
# Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no
# estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um
# fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final.

estoque = 250
vendidos = 78
novas_mercadorias = 100
estoque = estoque - vendidos + novas_mercadorias

print ("\nExercício 2:")
if estoque == 1:
    print ("O estoque atual tem",estoque,"peça.")
else:
    print ("O estoque atual tem",estoque,"peça.")

# Exercício 3: Divisão de Cargas (Logística/Transporte)
# Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada
# caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão
# totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma
# última viagem menor? (Use %)

caixas = 1250
caminhoes_cheios = caixas // 12
caixas_restantes = caixas % 12
print ("\nExercício 3:")
print ("  -Objetivo 1:",caminhoes_cheios,"caminhões sairão cheios.")
print ("  -Objetivo 2: Sobraram", caixas_restantes,"caixas para serem enviadas em uma última viagem.")

# Exercício 4: Análise de Margem de Lucro (Financeiro)
# Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$
# 5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro
# líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana
# chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

faturamento = 15000.00
custos_fixos = 5000.00
imposto = faturamento * 0.15
lucro = faturamento - imposto - custos_fixos
meta_atingida = bool(lucro > faturamento * 0.30)

print ("\nExercício 3:")
print ("O lucro foi R$",lucro,"\nMeta de 30% de lucro atingida:",meta_atingida)

# Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
# Cenário: Um contrato de manutenção de software tem a duração de 40 meses. O cliente
# quer ver esse tempo no formato: "X anos e Y meses". Objetivo: Utilize os operadores de
# divisão inteira e resto da divisão para converter os 40 meses.

duração_contrato_mes = 40
ano = 40 // duração_contrato_mes
mes = duração_contrato_mes % 12
print ("\nExercício 5:")
print ("O contrato de manutenção de software tem duração de:",ano,"anos e", mes,"meses")

# Print para deixar esteticamente organizado no terminal
print("")