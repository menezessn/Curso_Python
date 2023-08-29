perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_certas = 0


for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for opcao, valor in enumerate(pergunta['Opções']):
        print(f'{opcao}) {valor}')
    resposta = int(input('Escolha uma opção: '))
    if pergunta['Opções'][resposta] == pergunta['Resposta']:
        print('Parabéns, resposta correta\n\n')
        respostas_certas+=1
    else:
        print('Você errou a resposta\n\n')

print(f'{respostas_certas} respostas certas de um total de {len(perguntas)} perguntas')
    

    