

print("-----Menu-----")
print("1-Criar Produto")
print("---------------")

menu = int(input("\nDigite a opção:" ))
import produtos.produto as produto
if menu == 1:
    produto.CriaProduto()
elif menu == 2:
    exit()