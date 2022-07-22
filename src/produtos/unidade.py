import mysql.connector

banco = mysql.connector.connect(
   host = 'localhost',
   user='root',
   passwd='',
   database='dispensa'
)
def CriaUnidade():
    unidade = input("Unidade: ")
    cursor = banco.cursor()
    add = ("INSERT INTO UNIDADE(UNIDADE) VALUES('{}')".format(unidade))

    cursor.execute(add)
    banco.commit()
    cursor.close()
    banco.close()

def VerUnidade():
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM UNIDADE")
    result = cursor.fetchall()

    for x in result:
        print(x)

def EditarUnidade():
   VerUnidade()
   pass

def ExcluirUnidade():
   VerUnidade()
   cursor = banco.cursor()
   id = input("ID: ")
   add = ("DELETE FROM UNIDADE WHERE ID_UNIDADE = '{}'".format(id))
   cursor.execute(add)
   banco.commit()
   cursor.close()
   banco.close()