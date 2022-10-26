num_notas = 0                                 # Contador
notas = []                                    # Guarda as notas já digitadas

while (num_notas < 4):

    # Soma + 1 ao contador para definir qual Bimestre a nota se refere
    print('Insira uma NOTA (Bimestre: {})'.format(num_notas + 1))

    # Checagem para evitar erros no código
    try:
        nota = float(input())                # Checa se o input é um número
    except ValueError:
        print('Você inseriu uma letra, tente novamente!')
        
        # Repete a mesma volta do loop
        continue                             

    notas += [nota]                          # Inclui a nota digitada na lista "notas"
    num_notas += 1                           # Soma + 1 ao contador "num_notas"

media = sum(notas) / 4                       # Soma todas as notas e / 4
print(f'Sua média é {media:.1f}')           
