caminho_arquivo = 'aula15.txt'
dicionario =  {'nome': "Marcelo"}

with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write('linha1\n')
    arquivo.write('linha2\n')
    arquivo.seek(0,0)
    print(arquivo.read())

print(type(dicionario))

print(dicionario.get('nome'))
print(dicionario.get('idade'))


