Exercício 2: Rota Dinâmica com Parâmetro de URL
Conceitos Envolvidos: Rotas dinâmicas, parâmetros de URL, strings formatadas (f-strings).
Por que aprender isso? Muitas vezes, você precisará que sua API responda de forma diferente com base em informações passadas na própria URL (ex: /usuarios/123 para ver o usuário com ID 123). Este exercício te mostra como pegar esses dados.
Descrição:

No mesmo arquivo do Exercício 1, adicione uma nova rota:

Crie uma rota que aceite um nome como parte da URL. Por exemplo, se o usuário acessar /saudacao/Fulano, ele deve receber uma saudação personalizada.
Use o decorador @app.route('/saudacao/<nome>'). O <nome> indica que essa parte da URL é uma variável.
A função associada a essa rota deve receber o nome como argumento.
Dentro da função, retorne uma string formatada como "Olá, <nome_digitado>! Bem-vindo(a) ao Flask!".
Exemplos de Acesso:

http://127.0.0.1:5000/saudacao/Thales deve mostrar: "Olá, Thales! Bem-vindo(a) ao Flask!"
http://127.0.0.1:5000/saudacao/Programador deve mostrar: "Olá, Programador! Bem-vindo(a) ao Flask!"