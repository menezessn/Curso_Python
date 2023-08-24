import os
lista = []
while True:

    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
    
    
    
    if opcao == 'i':
        os.system('cls')
        item = input('Digite o nome do item: ')
        lista.append(item)
    elif opcao == 'a':
        try:
            os.system('cls')
            indice_item = int(input('Digite o indíce do item: '))
            del lista[indice_item]
        except:
            print('Indíce inválido')
    elif opcao == 'l':
        os.system('cls')
        for indice, valor in enumerate(lista):
            print(indice, valor)
    elif opcao == 's':
        os.system('cls')
        print('Encerrando o programa')
        break
    else: 
        os.system('cls')
        print('Opção inválida')