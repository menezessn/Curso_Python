import os



lista_tarefas = []
lista_desfazer = []
lista_refazer = []



while True:

    print("Comandos: listar, desfazer, refazer, clear, sair")
    entrada = input('Digite uma tarefa ou comando: ').lower()

    if(entrada == 'listar'):
        print(*lista_tarefas, sep='\n')
    elif(entrada == 'desfazer'):
        if (len(lista_tarefas)== 0):
            print('Nada a desfazer')
        else:
            lista_desfazer.append(lista_tarefas.pop())
            print(*lista_tarefas, sep='\n')
    elif(entrada == 'refazer'):
        if (len(lista_desfazer)== 0):
            print('Nada a refazer')
        else:
            lista_tarefas.append(lista_desfazer.pop())   
            print(*lista_tarefas, sep='\n')
    elif(entrada == 'clear'):
        os.system("cls")
    elif entrada == 'sair':
        break
    else:
        lista_tarefas.append(entrada)
        print(*lista_tarefas, sep='\n')


