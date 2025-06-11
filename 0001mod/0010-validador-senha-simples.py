'''
Conceitos Envolvidos: Variáveis, tipos de dados (strings), operadores de comparação, if/elif/else, funções de string (len(), islower(), isupper(), isdigit(), isalnum()).
Cenário de Backend: Em um sistema de autenticação, o backend precisa validar senhas recebidas de usuários.
Descrição:

Crie uma função chamada validar_senha que recebe uma senha (string) como argumento e retorna True se a senha for "forte" e False caso contrário.

Considere uma senha "forte" se ela atender a todas as seguintes condições:

Ter pelo menos 8 caracteres.
Conter pelo menos uma letra maiúscula.
Conter pelo menos uma letra minúscula.
Conter pelo menos um dígito (número).
No final do seu programa, chame essa função com algumas senhas de teste e imprima se elas são fortes ou não.

Exemplo:

Python

# Sua função validar_senha(senha) deve ser definida aqui

print(f"Senha 'MinhaSenha123': {validar_senha('MinhaSenha123')}") # Deve retornar True
print(f"Senha 'senhafraca': {validar_senha('senhafraca')}")     # Deve retornar False (não tem maiúscula, dígito)
print(f"Senha 'SENHAFORTE': {validar_senha('SENHAFORTE')}")     # Deve retornar False (não tem minúscula, dígito)
print(f"Senha '12345678': {validar_senha('12345678')}")         # Deve retornar False (não tem maiúscula, minúscula)
print(f"Senha 'Curta1': {validar_senha('Curta1')}")           # Deve retornar False (menos de 8 caracteres)
'''
def validar_senha(senha):
    total_caracteres = 0
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"

    maior_que_oito = False
    tem_minuscula = False
    tem_maiuscula = False
    tem_numero = False

    for i in senha:
        total_caracteres += 1

    if(total_caracteres >= 8):
        maior_que_oito = True
        for i in letras_maiusculas:
            if(i in senha):
                tem_maiuscula = True
        for i in letras_minusculas:
            if(i in senha):
                tem_minuscula = True
        for i in senha:
            if(i in "1234567890"):
                tem_numero = True
        if(maior_que_oito and tem_minuscula and tem_maiuscula and tem_numero):
            print(f"Minha senha: {senha}: Senha nos conformes!")
        if(not tem_minuscula):
            print(f"Minha senha: {senha}: Não tem minuscula!")
        if(not tem_maiuscula):
            print(f"Minha senha: {senha}: Não tem maiuscula!")
        if(not tem_numero):
            print(f"Minha senha: {senha}: Não tem número!")

        print(tem_maiuscula)
        print(tem_minuscula)
        print(tem_numero)
    else:
        print(f"Minha senha: {senha} = Senha menor que 8 caracteres")
        
    


validar_senha("123456Rd78")