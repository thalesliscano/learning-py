Exercício 1: Modelando um Usuário de Sistema

Conceitos Envolvidos: Classes, Objetos, Atributos, Métodos, Construtor (__init__), Encapsulamento (atributos privados/protegidos, getters/setters).
Cenário de Backend: Em qualquer sistema backend, você precisará modelar entidades como usuários, produtos, pedidos, etc. Este exercício simula a criação de um modelo de Usuário.
Descrição:

Crie uma classe Python chamada Usuario que represente um usuário em um sistema.

A classe Usuario deve ter os seguintes atributos:

_id (privado/protegido): Um identificador único para o usuário (pode ser um número inteiro, comece com 1 para o primeiro usuário, 2 para o segundo, etc. ou use uma string simples por enquanto).

_nome_usuario (privado/protegido): O nome de usuário para login (string).

_senha_hash (privado/protegido): Uma representação "hash" da senha (string). Por enquanto, você pode simplesmente armazenar a senha real, mas imagine que na prática seria um hash criptografado.

_email (privado/protegido): O endereço de email do usuário (string).

_ativo (privado/protegido): Um booleano indicando se a conta está ativa (True) ou desativada (False).

A classe deve ter um método construtor (__init__) que inicialize esses atributos. Os atributos _id e _ativo podem ter valores padrão (ex: _id pode ser gerado automaticamente, _ativo como True).

Crie os seguintes métodos para a classe:

get_nome_usuario(): Retorna o nome de usuário.
get_email(): Retorna o email do usuário.
set_email(novo_email): Atualiza o email do usuário.
desativar_conta(): Altera o status _ativo para False.
ativar_conta(): Altera o status _ativo para True.
verificar_senha(senha_digitada): Recebe uma senha e retorna True se ela corresponder à _senha_hash (lembre-se, por enquanto, você pode comparar a string diretamente), False caso contrário.
Teste no final:

Crie dois objetos (instâncias) da classe Usuario.
Acesse e imprima o nome de usuário e email de cada um usando os métodos get.
Altere o email de um dos usuários usando set_email.
Desative a conta de um usuário e depois ative novamente.
Tente verificar uma senha correta e uma incorreta para cada usuário