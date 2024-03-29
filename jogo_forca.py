secreto = 'perfume'                 
digitadas = []
chances = 3

while True:

    # Define qtd de chances
    if chances <= 0:
        print('Você perdeu!!!!')
        break

    letra = input('Digite uma letra: ')

    # Qtd de caracteres digitados
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    # Guarda letras corretas
    digitadas.append(letra)

    # Mostra se a letra existe
    if letra in secreto:
        print(f'UHUUUL, a letra "{letra}" existe na palavra secreta!')
    else:
        print(f'AAAAH, a letra "{letra}" NÃO EXISTE na palavra secreta!')

        # Retira letra inexistente de "digitadas"
        digitadas.pop()

    # Guarda letra correta ou *
    secreto_temporario = ''

    # Mostra letras acertadas e faltantes (*)
    for letra_secreta in secreto:

        # Concatenar letra digitada e *
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:

            # Ocultar com '*' a letra inexistente
            secreto_temporario += "*"

    # Chegar descoberta palavra secreta
    if secreto_temporario == secreto:
        print(f'Que legal, vocẽ ganhou!!!!! a palavra era: {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

    # Qtd de erros
    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
