import copy

from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# print(*produtos, sep='\n')
produtos_copia = copy.deepcopy(produtos)
# print(*novos_produtos, sep='\n')
novos_produtos = [
    {**produto, 'preco':round(produto['preco'] * 1.1, 2)}
    for produto in produtos_copia
]
print(*novos_produtos, sep='\n')
print()

novos_produtos_copia_profunda = copy.deepcopy(novos_produtos)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(novos_produtos_copia_profunda, key = lambda produto:produto['nome'], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(novos_produtos_copia_profunda, key = lambda produto:produto['preco'])
print(*produtos_ordenados_por_preco, sep='\n')


