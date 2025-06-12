from Produto import Produto

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preco,estoque, data_validade):
        super().__init__(nome, preco, estoque)
        self.data_validade = data_validade
    def exibir_informacoes(self):
        print(f"Nome do Produto: {self.nome}\nPreço: {self.preco}\nEstoque: {self._estoque}\nGarantia: {self.data_validade}")