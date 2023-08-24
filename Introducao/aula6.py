import re
#Verificador de CPF


#Input cpf
cpf_digitado = re.sub(r'[^0-9]', '', input ('Insert your CPF(without dots or hyphen ): ') ) 
print(f'You typed: {cpf_digitado}')

if cpf_digitado == cpf_digitado[0]*len(cpf_digitado):
    print('Você digitou apenas dígitos iguais')

#length verification

elif(len(cpf_digitado)!=11):
    print('O CPF digitado é inválido')
else:
    cpf_nove_digitos = cpf_digitado[:9]
    #verificacao digito
    multiplicador=10
    indice = 0
    digito1 = 0
    while multiplicador>1:
        digito1+= int(cpf_nove_digitos[indice])*multiplicador
        indice+=1
        multiplicador-=1
    digito1 = (digito1*10)%11
    if digito1 > 9:
        digito1 = 0
    print(digito1)

    indice = 0
    multiplicador = 11
    digito2=0
    cpf_dez_digitos = cpf_nove_digitos + str(digito1)
    while multiplicador>1:
        digito2+= int(cpf_dez_digitos[indice])*multiplicador
        indice+=1
        multiplicador-=1
    digito2 = (digito2*10)%11
    digito2 = digito2 if digito2 <= 9 else 0
    print(digito2)
    
    cpf_gerado = cpf_nove_digitos + str(digito1) + str(digito2)
    if cpf_gerado == cpf_digitado:
        print('O CPF digitado é válido')
    else:
        print('O CPF digitado é inválido')
        






