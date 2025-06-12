Exercício 2: Gerenciamento de Produtos em Estoque (Herança Simples)

Conceitos Envolvidos: Herança, Classes Base, Classes Derivadas, Atributos e Métodos.
Cenário de Backend: Sistemas de e-commerce ou estoque precisam gerenciar diferentes tipos de produtos.
Descrição:

Crie uma hierarquia de classes para produtos:

Classe Base: Produto

Atributos: nome (string), preco (float), estoque (inteiro).
Construtor: Inicializa esses atributos.
Métodos:
exibir_informacoes(): Imprime o nome, preço e estoque do produto.
adicionar_estoque(quantidade): Adiciona quantidade ao estoque.
remover_estoque(quantidade): Remove quantidade do estoque. ATENÇÃO: Não permita que o estoque fique negativo. Se a quantidade a remover for maior que o estoque atual, imprima uma mensagem de erro e não faça a remoção.
Classe Derivada: ProdutoEletronico

Herda de Produto.
Atributos Adicionais: garantia_meses (inteiro).
Construtor: Deve chamar o construtor da classe base (super().__init__()) e inicializar garantia_meses.
Sobrescreva o método exibir_informacoes(): Além das informações do produto base, também imprima a garantia_meses.
Classe Derivada: ProdutoAlimenticio

Herda de Produto.
Atributos Adicionais: data_validade (string, por simplicidade, ou use datetime se já souber).
Construtor: Deve chamar o construtor da classe base (super().__init__()) e inicializar data_validade.
Sobrescreva o método exibir_informacoes(): Além das informações do produto base, também imprima a data_validade.
Teste no final:

Crie uma instância de Produto (ex: "Livro", 30.00, 50).
Crie uma instância de ProdutoEletronico (ex: "Smartphone", 2500.00, 10, 12).
Crie uma instância de ProdutoAlimenticio (ex: "Arroz", 15.00, 100, "2025-12-31").
Chame exibir_informacoes() para cada um.
Tente adicionar e remover estoque de um dos produtos, incluindo tentativas de remover mais do que o disponível.