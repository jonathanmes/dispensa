

print("-----Menu-----")
print("\n----Produto----")
print("1-Criar Produto")
print("2-Ver Produtos")
print("3-Editar Produtos")
print("4-Excluir Itens")
print("\n----Marca----")
print('5-Criar Marca')
print("6-Ver Marcas")
print("7-Editar Marcas")
print("8-Excluir Marcas")
print("\n---Unidades---")
print('9-Criar Unidade')
print("10-Ver Unidades")
print("11-Editar Unidades")
print("12-Excluir Unidade\n")
print("0-Sair")
print("---------------")

menu = int(input("\nDigite a opção:" ))
import produtos.produto as produto
import produtos.marca as marca
import produtos.unidade as unidade

if menu == 1:
    produto.CriaProduto()
elif menu == 2:
    produto.VerProduto()
elif menu == 3:
    produto.EditarProduto()
elif menu == 4:
    produto.ExcluirProduto()
elif menu == 5:
    marca.CriaMarca()
elif menu == 6:
    marca.VerMarca()
elif menu == 7:
    marca.EditarMarca()
elif menu == 8:
    marca.ExcluirMarca()
elif menu == 9:
    unidade.CriaUnidade()
elif menu == 10:
    unidade.VerUnidade()
elif menu == 11:
    unidade.ExcluirUnidade()
elif menu == 12:
    unidade.ExcluirUnidade()
elif menu == 0:
    exit()