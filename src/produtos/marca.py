import mysql.connector

banco = mysql.connector.connect(
   host = 'localhost',
   user='root',
   passwd='',
   database='dispensa'
)

def CriaMarca():
    marca = input('Marca: ')
    cursor = banco.cursor()
    add = ("INSERT INTO MARCA(MARCA) VALUES('{}')".format(marca))

    cursor.execute(add)
    banco.commit()
    cursor.close()
    banco.close()

def VerMarca():
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM MARCA")
    result = cursor.fetchall()

    for x in result:
        print(x)

def EditarMarca():
   VerMarca()
   pass

def ExcluirMarca():
   VerMarca()
   cursor = banco.cursor()
   id = input("ID: ")
   add = ("DELETE FROM MARCA WHERE ID_MARCA = '{}'".format(id))
   cursor.execute(add)
   banco.commit()
   cursor.close()
   banco.close()