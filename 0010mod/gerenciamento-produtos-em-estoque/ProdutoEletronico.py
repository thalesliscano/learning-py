from Produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, estoque, garantia_meses):
        super().__init__(nome, preco, estoque)
        self.garantia_meses = garantia_meses
    def exibir_informacoes(self):
        print(f"Nome do Produto: {self.nome}\nPreço: {self.preco}\nEstoque: {self._estoque}\nGarantia: {self.garantia_meses}")
