Exercício 3: Rota com Múltiplos Tipos de Parâmetros e Validação Simples
Conceitos Envolvidos: Múltiplos parâmetros em rotas, conversão de tipo (Flask faz automaticamente com <int:nome>), tratamento de erros básicos.
Por que aprender isso? Para criar APIs que lidam com diferentes tipos de dados na URL (como IDs numéricos, nomes de usuário, etc.) e para começar a pensar em como lidar com entradas inválidas.
Descrição:

No seu app.py, crie mais uma rota:

Defina uma rota chamada /calcular_dobro/<int:numero>.
A parte <int:numero> indica que o Flask deve esperar um número inteiro e passá-lo para a função como a variável numero.
A função associada deve receber o numero como argumento.
Dentro da função, calcule o dobro do numero e retorne uma string formatada como "O dobro de <numero> é <dobro_do_numero>.".
Desafio Extra: O que acontece se você tentar acessar /calcular_dobro/abc? Como o Flask já tenta converter para int, ele vai gerar um erro. Por enquanto, apenas observe o erro. No futuro, aprenderemos a lidar com isso de forma elegante.