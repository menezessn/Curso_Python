def soma (x,y,z = None ):
    if z is None:
        print(f'{x=} {y=} ', x + y)
    else:
        print(f'{x=} {y=} {z=} ', x + y + z)

soma(1,2)

dicionario = {
    'nome:': 'Marcelo',
    'sobrenome:': 'de Menezes Nascimento',
    }

print(len(dicionario))
print(list(dicionario.keys())) 
print(list(dicionario.values())) 
print(list(dicionario.items()))
dicionario.setdefault('idade', 0)


