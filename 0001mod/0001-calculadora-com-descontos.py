'''
Ah, entendi! Que ótimo que você já tem um conhecimento prévio em programação e Python! Isso vai acelerar bastante nosso aprendizado.

Se você já tem essa base, podemos focar em exercícios que reforcem os conceitos essenciais do Python e que são muito usados no desenvolvimento backend. Perfeito!

Então, para o Módulo 1: Primeiros Passos com Python, vamos praticar com alguns exercícios que misturam os tópicos, pois na vida real, eles raramente aparecem isolados. Assim, você já começa a pensar de forma mais integrada.

Vou te dar alguns exercícios que cobrem variáveis, tipos de dados, operadores, estruturas de controle (if/else, for/while) e funções, com um toque prático de backend.

Módulo 1: Exercícios de Reforço em Python para Backend
Exercício 1: Calculadora de Preço Total com Desconto

Conceitos Envolvidos: Variáveis, tipos de dados (números, texto), operadores aritméticos, if/else, entrada/saída de dados, formatação de texto.
Cenário de Backend: Imagine que seu backend recebe informações de um pedido de e-commerce.
Descrição:

Crie um programa Python que faça o seguinte:

Peça ao usuário para digitar o nome de um produto (ex: "Celular").
Peça ao usuário para digitar o preço unitário do produto (ex: 1500.00).
Peça ao usuário para digitar a quantidade desejada (ex: 2).
Calcule o preço total bruto (preço unitário * quantidade).
Regra de Desconto:
Se o preço total bruto for maior ou igual a R$ 2000,00, aplique um desconto de 10%.
Caso contrário, não aplique desconto.
Calcule o preço final após o desconto.
Imprima todas as informações de forma clara:
Nome do produto
Preço unitário
Quantidade
Preço total bruto
Valor do desconto (se houver)
Preço final a pagar
Exemplo de Saída (para preço unitário 1500 e quantidade 2):

Produto: Celular
Preço Unitário: R$ 1500.00
Quantidade: 2
Preço Total Bruto: R$ 3000.00
Desconto Aplicado: R$ 300.00 (10%)
Preço Final a Pagar: R$ 2700.00
'''

produto = input("Digite o produto desejado: ")
preco_unitario = float(input("Digite o preço na etiqueta: "))
quantidade = int(input("Digite quantos produtos: "))
desconto = 0

calculo = preco_unitario * quantidade

print(f"Produto: {produto}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Preço total bruto: R$ {calculo:.2f}")
if(calculo > 2000):
    desconto = calculo * (10/100)
    print(f"Desconto aplicado: R$ {desconto:.2f} (10%)" )
else:
    desconto += desconto
    print("Nenhum desconto aplicado")
print(f"Preço final a pagar: R$ {calculo - desconto:.2f}")


