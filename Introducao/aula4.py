import os

#Jogo de palavras

#Palavra que o usuário deverá adivinhar
letras_acertadas = ''

palavra_secreta = 'perfume'

tentativas = 0

while True:
    
    letra_digitada = input('Digite uma letra: ')
    tentativas+=1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra');
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formatada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada+=letra_secreta
        else:
            palavra_formatada+='*'
    print(palavra_formatada)
    


    if palavra_formatada == palavra_secreta:
        os.system('cls')
        print(f'Parabéns você encontrou a palavra: {palavra_formatada} em {tentativas} tentativas')
        break

