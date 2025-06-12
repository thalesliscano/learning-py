from Produto import Produto
from ProdutoEletronico import ProdutoEletronico
from ProdutoAlimenticio import ProdutoAlimenticio

prod1 = Produto("Livro", 30.0, 50)
prod2 = ProdutoEletronico("SmartPhone", 2655.0, 10, 12)
prod3 = ProdutoAlimenticio("Arroz", 15.0, 100, "2025-12-31")

prod1.exibir_informacoes()
prod2.exibir_informacoes()
prod3.exibir_informacoes()

print("-"*10)
prod1.exibir_informacoes()
prod1.adicionar_estoque(10)
prod1.exibir_informacoes()
prod1.remover_estoque(60)
prod1.remover_estoque(1)
prod1.exibir_informacoes()

