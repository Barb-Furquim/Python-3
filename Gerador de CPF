from random import randint                            # Gera números inteiros aleatórios
numero = str(randint(100000000, 999999999))

novo_cpf = numero                                     # Para retirar os dois ultimos números
reverso = 10
total = 0

for index in range(19):                               # Contar 19 laços de forma crescente
    if index > 8:                                     # Contar os índices maiores que 8
        index -= 9                                    # Diminuir 9 do índice

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:                                   # contagem decrescente dos laços
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)
