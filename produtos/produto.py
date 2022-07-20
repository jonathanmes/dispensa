class Produto:
   def __init__(self, codigo_ean, produto, id_marca, id_unidade, qtd_unidade):
      self.codigo_ean = codigo_ean
      self.produto = produto
      self.id_marca = id_marca
      self.id_unidade = id_unidade
      self.qtd_unidade = qtd_unidade

   def CriarProduto(self):
      pass

   def AlterarProduto(self):
      pass

   def ExcluirProduto(self):
      pass

   def VerProduto(self):
      print(f"EAN: {self.codigo_ean} - Produto: {self.produto}")

computador = Produto('123','Papel','12313','12321','122')
computador.VerProduto()