nome_filme ='Enrolados' 
nome_sala = 'Sala Roxa'
duracao = 100 
quantidade_de_espectador = 250 
Valor_do_ingresso = 49.99
Valor_do_ingresso_meia = Valor_do_ingresso / 2

print(f'Venha assistir ao filme {nome_filme} na sala de cinema {nome_sala}')
print (f'O filme {nome_filme} tem a duração de {duracao} minutos e você pode assiastir ele por apenas R$ {Valor_do_ingresso} a inteira 😃')
print (F'E o valor do ingresso como meia é de R${Valor_do_ingresso_meia}')

quantidade_ingressos = input('quantos ingressos você quer comprar:')
quantidade_ingressos = int(quantidade_ingressos)
valor_final = quantidade_ingressos * Valor_do_ingresso
print(f'Você comprou {quantidade_ingressos} ingressos por R${valor_final}')