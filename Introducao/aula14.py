#recursividade

def fatorial (num):
    if num == 0:
        return 1
    return num * fatorial(num-1)

num_fatorial = fatorial(996)
print(num_fatorial)