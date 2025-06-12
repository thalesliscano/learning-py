class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self._estoque = estoque
    
    def exibir_informacoes(self):
        print(f"Nome do Produto: {self.nome}\nPreço: {self.preco}\nEstoque: {self._estoque}")
    def adicionar_estoque(self, quantidade):
        if(quantidade > 0):
            self._estoque += quantidade
        else:
            print("Passe um valor mairo que 0")
    def remover_estoque(self, quantidade):
        if(quantidade <= self._estoque):
            self._estoque -= quantidade
        else:
            print("Erro!!!! estoque não pode ficar negativo.")