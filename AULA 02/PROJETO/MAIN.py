nome_cliente = input('Qual é o seu nome?: ').title()

nome_filme = "A Branca de neve"

valor_inteira = 40.99
ingresso_meia = valor_inteira / 2

idade_cliente = input ("Qual a sua idade?: ")
idade_cliente = int(idade_cliente)

print(f'Seja bem vindo(a) {nome_cliente}')
print(f'O filme que está em cartaz é {nome_filme}')
print(f'O ingresso inteira está R${valor_inteira} e o valor do ingresso meia está R$ {ingresso_meia:.2f}')

quantidade_de_ingresso = input ('Quantos ingressos o Sr.(a) deseja?:')
quantidade_de_ingresso = int(quantidade_de_ingresso)

if idade_cliente <= 24 or  idade_cliente >= 60:
    valor_final = quantidade_de_ingresso * ingresso_meia

else:
    valor_final = quantidade_de_ingresso * valor_inteira

if quantidade_de_ingresso <= 3 :
    valor_final *= 0.95

elif quantidade_de_ingresso <= 5:
    valor_final *= 0.90 

elif quantidade_de_ingresso <= 10:
    valor_final *= 0.80

else: 
    valor_final *= 0.70

print (f'Sua compra saiu o total de R${valor_final: .2f}')
