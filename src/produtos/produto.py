from ast import main
from zlib import DEF_BUF_SIZE
import mysql.connector
import produtos.unidade as unidade
import produtos.marca as  marca


banco = mysql.connector.connect(
   host = 'localhost',
   user='root',
   passwd='',
   database='dispensa'
)
def CriaProduto():
   codigo_ean = input('Código EAN: ')
   produto = input('Nome do Produto: ')
   id_marca = int(AdicionarMarca())
   id_unidade = int(AdicionarUnidade())
   qtd = input('Quantidade: ')
   cursor = banco.cursor()
   add = ("INSERT INTO PRODUTO(CODIGO_EAN, PRODUTO, ID_MARCA, ID_UNIDADE, QTD_UNIDADE) VALUES ('{}','{}','{}','{}','{}')".format(codigo_ean,produto,id_marca,id_unidade,qtd))
     
   cursor.execute(add)
   banco.commit()
   cursor.close()
   banco.close()

def VerProduto():
   cursor = banco.cursor()
   cursor.execute("SELECT *  FROM VIEW_PRODUTO ")
   result = cursor.fetchall()

   for x in result:
      print(x)

def AdicionarMarca():
   marca.VerMarca()
   id = input('ID Marca: ')
   return id

def AdicionarUnidade():
   unidade.VerUnidade()
   id = input("ID Unidade: ")
   return id

def EditarProduto():
   VerProduto()
   cursor = banco.cursor()
   ean = input("Código EAN: ")
   produto = input("Nome do Produto: ")
   add = ("update PRODUTO set PRODUTO = '{}' where CODIGO_EAN = '{}'".format(produto,ean))
   cursor.execute(add)
   banco.commit()
   cursor.close()
   banco.close()


def ExcluirProduto():
   VerProduto()
   cursor = banco.cursor()
   ean = input("Código EAN: ")
   add = ("DELETE FROM PRODUTO WHERE CODIGO_EAN = '{}'".format(ean))
   cursor.execute(add)
   banco.commit()
   cursor.close()
   banco.close()


 