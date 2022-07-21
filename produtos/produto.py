import mysql.connector

banco = mysql.connector.connect(
   host = 'localhost',
   user='root',
   passwd='',
   database='dispensa'
)
def CriaProduto():
   codigo_ean = input('Código EAN: ')
   produto = input('Nome do Produto: ')
   id_marca = input('Marca: ')
   id_unidade = input('Unidade: ')
   qtd = input('Quantidade Mínima: ')
   cursor = banco.cursor()
   add = ("INSERT INTO PRODUTO(CODIGO_EAN, PRODUTO, ID_MARCA, ID_UNIDADE, QTD) VALUES ('{}','{}','{}','{}','{}')".format(codigo_ean,produto,id_marca,id_unidade,qtd))
     
   cursor.execute(add)
   banco.commit()
   cursor.close()
   banco.close()
   

##CriaProduto()