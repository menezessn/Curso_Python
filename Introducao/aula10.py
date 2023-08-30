import sys
'''as é para dar um apelido aos módulos'''
print(sys.platform)

#modularização organiza os códigos e deixa os programas mais legíveis
#o primeiro módulo executado pelo python se chama __main__
#pastas no python são chamadas de pacotes 

#import é um singleton, ou seja, só ocorre uma instância
#para repetir um módulo é preciso usar importlib.reload(nome_do_modulo)