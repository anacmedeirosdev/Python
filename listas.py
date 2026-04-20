# Exercício 1: Dashboard de Vendas (Análise de Dados) Você recebeu uma lista com as
# vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um
# programa que exiba um pequeno relatório contendo:
# 1. O total de vendas na semana.
# 2. A média de vendas diária.
# 3. O valor da melhor venda e da pior venda do período.

print ("\nExercício 1:")
vendas = [1500, 2000, 800, 3500, 1200]
quantidade = len(vendas)
total_vendas = 0


for v in vendas:
    total_vendas = total_vendas + v
    media_vendas = total_vendas / quantidade

maior_venda = max(vendas)
menor_venda = min(vendas)

print (f"Total de vendas: {total_vendas:.2f}\nMédia diária de vendas: {media_vendas:.2f}\nMaior venda: {maior_venda:.2f}\nMenor venda: {menor_venda:.2f}")
total_vendas = sum(vendas) #Função que soma todos os itens de uma lista.


# --------------------------------------------------------------------------------------

# Exercício 2: Gestão de Estoque (Edição e Verificação) Uma loja de eletrônicos possui os
# seguintes produtos: estoque = ["monitor", "teclado", "mouse", "headset"].
# O gerente pediu para:
# 1. Adicionar o item "webcam" ao final da lista.
# 2. O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa
# alteração na lista.
# 3. Verificar se "impressora" está no estoque. O programa deve exibir True ou
# False.
# 4. Remover o "mouse" da lista, pois saiu de linha.

print("\nExercício 2:")
estoque = ["monitor", "teclado", "mouse", "headset"]
print(estoque)
estoque.append("webcam")
print(estoque)
estoque[1] = "teclado mecanico"
# posicao_palavra = estoque.index("teclado")
# estoque[posicao_palavra] = "teclado mecanico"
verificacao = "impressora" in estoque
print(estoque)
estoque.remove("mouse")
print(estoque)
verificacao = "impressora" in estoque
print(verificacao)


# --------------------------------------------------------------------------------------

# Exercício 3: Organização de Preços (Ordenação e Slicing) Uma importadora listou os
# preços de frete em dólar: fretes = [50, 80, 20, 150, 40]. Para apresentar em uma
# reunião, você deve:
# 1. Ordenar a lista do maior para o menor preço.
# 2. Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova
# lista chamada top_fretes.
# 3. Exibir a lista original ordenada e a lista dos top_fretes.

print("\nExercício 3:")
fretes = [50, 80, 20, 150, 40]
fretes.sort()
print(f"Frestes da Loja: {fretes}")
fretes.sort(reverse=True)
# print(fretes)
top_fretes = fretes[:2]
print(f"Maiores fretes: {top_fretes}")

# --------------------------------------------------------------------------------------

# Exercício 4: Sistema de Logística (Busca e Extensão) A empresa "LogTrack" tem uma
# rota de entregas: rota = ["Sao Paulo", "Campinas", "Jundiai",
# "Sorocaba"]. Novas cidades foram adicionadas por uma empresa parceira:
# novas_cidades = ["Itu", "Valinhos"]. Seu script deve:
# 1. Unir as duas listas em uma só (usando extend).
# 2. Identificar em qual posição (índice) está a cidade de "Sorocaba".
# 3. Exibir a lista completa e a posição encontrada.
# 4. Exibir uma mensagem final: “Sorocaba é a Xa cidade da rota”

print("\nExercício 4:")
rota = ["Sao Paulo", "Campinas", "Jundiai","Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]
rota.extend(novas_cidades)
# Juntar listas
print(rota)
posicao_cidade = rota.index("Sorocaba") + 1
print(f"Sorocaba é a {posicao_cidade}ª da rota.")

# --------------------------------------------------------------------------------------

# Exercício 5: Atualização de Preços Interativa (Input + Lista) Você tem uma lista de
# preços de produtos: precos = [100.0, 250.0, 500.0] e uma com o nome: vinhos
# = ["Branco", "Tinto","Champagne"]. Crie um programa interativo que:
# 1. Peça para o usuário digitar qual o nome do produto.
# 2. Peça para o usuário digitar o novo preço.
# 3. Atualize o preço na lista e exiba as listas completas com os nomes e os preços

print("\nExercício 5:")
precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto","Champagne"]
novo_produto = input("Nome do novo produto: ")
preco_produto = float(input(f"Preço do produto {novo_produto}: "))
precos.append(preco_produto)
vinhos.append(novo_produto)
print(f"{precos}\n{vinhos}")
for p, v in zip(precos,vinhos):
    print(f"O {v} custa R${p:.2f}")

print("")