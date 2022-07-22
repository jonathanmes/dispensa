

print("-----Menu-----")
print("1-Criar Produto")
print("2-Ver Produtos")
print('3-Criar Marca')
print("4-Ver Marcas")
print('5-Criar Unidade')
print("6-Ver Unidades")
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
    marca.CriaMarca()
elif menu == 4:
    marca.VerMarca()
elif menu == 5:
    unidade.CriaUnidade()
elif menu == 6:
    unidade.VerUnidade()
elif menu == 7:
    exit()