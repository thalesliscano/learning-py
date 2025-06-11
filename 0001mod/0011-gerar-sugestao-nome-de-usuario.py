'''
Exercício 3: Gerador de Nomes de Usuário Simples

Conceitos Envolvidos: Variáveis, tipos de dados (strings), entrada/saída, laços de repetição (for), funções de string (strip(), lower(), replace()), fatiamento de strings.
Cenário de Backend: Ao cadastrar um novo usuário, o sistema pode sugerir um nome de usuário baseado no nome completo.
Descrição:

Crie um programa Python que:

Peça ao usuário para digitar seu nome completo (ex: "João da Silva Sauro").

Gere um nome de usuário sugerido seguindo estas regras:

Converter para letras minúsculas.
Remover espaços em branco do início e fim.
Substituir todos os espaços internos por um . (ponto).
Limitar o nome de usuário a no máximo 15 caracteres. Se for maior, pegue apenas os primeiros 15 caracteres.
Imprima o nome de usuário sugerido.

Exemplo de Saída:

Entrada: Maria Antônia da Costa

Saída: maria.antonia.d (15 caracteres, 'a.costa' foi cortado)

Entrada: Pedro Alcântara

Saída: pedro.alcantara (15 caracteres)

Entrada: Ana

Saída: ana

O que você achou desses exercícios? Eles te parecem um bom desafio para aquecer os motores e revisar esses conceitos? Se tiver alguma dúvida ou quiser que eu explique alguma parte, é só falar!
'''

nome_completo = input("Digite seu nome completo:").lower().strip().replace(" ", ".")
nome_usuario_sugerido = ""

i = 0
while(i < 15):
    nome_usuario_sugerido += nome_completo[i]
    i+= 1
print(nome_usuario_sugerido)
