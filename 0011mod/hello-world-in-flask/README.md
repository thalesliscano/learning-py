Exercício 1: "Olá, Mundo!" com Flask e Uma Rota Simples
Conceitos Envolvidos: Instalação do Flask, criação de uma aplicação Flask, rotas (@app.route), retorno de string (texto).
Por que aprender isso? É o seu primeiro contato com o framework! Você vai entender como uma aplicação Flask nasce e como ela responde a requisições básicas. Isso é o fundamento de qualquer API ou site feito com Flask.
Descrição:

Crie um arquivo Python (você pode chamá-lo de app.py ou server.py, por exemplo) e faça o seguinte:

Importe o objeto Flask do módulo flask.
Crie uma instância da sua aplicação Flask. Geralmente, se usa app = Flask(__name__).
Defina uma rota para o endereço principal da sua aplicação (o "raiz" ou /). Use o decorador @app.route('/').
Dentro da função associada a essa rota, retorne a string "Olá, Mundo com Flask!".
Adicione o bloco if __name__ == '__main__': e faça sua aplicação rodar em modo de depuração.
Passos para Execução:

Salve o código no arquivo (ex: app.py).
Abra o terminal na pasta onde você salvou o arquivo.
Execute o comando: python app.py (ou o nome que você deu ao arquivo).
Abra seu navegador e acesse o endereço que o Flask indicar (normalmente http://127.0.0.1:5000/).
Você deve ver a mensagem "Olá, Mundo com Flask!".