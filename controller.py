from models import *
from dao import *
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
                break
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print(f'Categoria ´{novaCategoria}` cadastrada com sucesso!')
        else:
            print(f'A categoria ´{novaCategoria}` já existe!')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        if len(cat) <= 0:
            print(f'A categoria ´{categoriaRemover}` não existe!')
        else:
            for i in range(len(x)):
               if x[i].categoria == categoriaRemover:
                   del x[i]
                   break
            print(f'Categoria `{categoriaRemover}´ removida com sucesso!')
    #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('arquivos/categorias.txt', 'w') as arq:
                [arq.write(f'{i.categoria}\n') for i in x]

    def alterarCategoria(self, categoriaAtual, novaCategoria):
        x = DaoCategoria.ler()
        cat1 = list(filter(lambda x: x.categoria == categoriaAtual, x))

        if len(cat1) > 0:
            cat2 = list(filter(lambda x: x.categoria == novaCategoria, x))
            if len(cat2) > 0:
                print(f'Já existe uma categoria chamada ´{novaCategoria}`')
            else:
                x = list(map(lambda x: Categoria(novaCategoria) if (x.categoria == categoriaAtual) else (x), x))
                print(f'A categoria `{categoriaAtual}´ foi alterada para `{novaCategoria}´ com sucesso!')
                #TODO: COLOCAR SEM CATEGORIA TAMBÉM NO ESTOQUE
                with open('arquivos/categorias.txt', 'w') as arq:
                    [arq.writelines(f'{i.categoria}\n') for i in x]
        else:
            print(f'A categoria ´{categoriaAtual}` não existe!')

    def listarCategorias(self):
        x = DaoCategoria.ler()
        if len(x) == 0:
            print('Nenhuma categoria cadastrada!')
        else:
            [print(f'Categoria: {i.categoria}') for i in x]

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        prod = list(filter(lambda x: x.produto.nome == nome, x))
        cat = list(filter(lambda x: x.categoria == categoria, y))
        if len(cat) > 0:
            if len(prod) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print(f'Produto ´{nome}` cadastrado com sucesso!')
            else:
                print(f'Produto ´{nome}` já cadastrado no estoque!')
        else:
            print(f'A categoria ´{categoria}` não existe!')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        prod = list(filter(lambda x: x.produto.nome == nome, x))
        if len(prod) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print(f'Produto removido com sucesso!')
            with open('arquivos/estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + '|' + 
                                    i.produto.preco + '|' + 
                                    i.produto.categoria + '|' + 
                                    str(i.quantidade) + '\n')
        else:
            print(f'O produto não existe!')

    def alterarProduto(self, nome, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        prod = list(filter(lambda x: x.produto.nome == nome, x))
        cat = list(filter(lambda x: x.categoria == novaCategoria, y))

        if len(cat) > 0:
            if len(prod) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if (x.produto.nome == nome) else (x), x))
                    print(f'Produto ´{nome}` alterado para ´{novoNome}` com sucesso!')
                    with open('arquivos/estoque.txt', 'w') as arq:
                        for i in x:
                            arq.writelines(i.produto.nome + '|' + 
                                            str(i.produto.preco) + '|' + 
                                            i.produto.categoria + '|' + 
                                            str(i.quantidade) + '\n')
                else:
                    print(f'Já existe um produto chamado ´{novoNome}`')
            else:
                print(f'O produto ´{nome}` não existe!')
        else:
            print(f'A categoria não existe!')

    def listarProdutos(self):
        x = DaoEstoque.ler()
        if len(x) == 0:
            print('Nenhum produto cadastrado!')
        else:
            print('-------------------')
            print(f'----- ESTOQUE -----')
            print('-------------------')
            for i in x:
                print(f'Nome: {i.produto.nome}')
                print(f'Preço: R$ {i.produto.preco}')
                print(f'Categoria: {i.produto.categoria}')
                print(f'Quantidade: {i.quantidade}')
                print('-------------------')

class ControllerVenda:
    def realizarVenda(self, nomeProduto, vendedor = 'admin', comprador = 'não identificado', quantidadeVendida = 1):
        x = DaoEstoque.ler()
        prod = list(filter(lambda x: x.produto.nome == nomeProduto, x))
        if len(prod) > 0:
            for i in prod:
                if i.quantidade >= quantidadeVendida:
                    i.quantidade -= quantidadeVendida
                    vendido = Venda(i.produto, vendedor, comprador, quantidadeVendida)
                    DaoVenda.salvar(vendido)
                    valorCompra = quantidadeVendida * int(i.produto.preco)
                    print('---------------------------')
                    print(f'Venda realizada com sucesso!')
                    print('---------------------------')
                    print(f'Produto: {i.produto.nome}')
                    print(f'Valor unitário: R$ {i.produto.preco}')
                    print(f'Quantidade: {quantidadeVendida}')
                    print(f'Valor total: R$ {valorCompra}')
                    print('---------------------------')
                    with open('arquivos/estoque.txt', 'w') as arq:
                        for item in x:
                            arq.writelines(item.produto.nome + '|' + 
                                           str(item.produto.preco) + '|' + 
                                           item.produto.categoria + '|' + 
                                           str(item.quantidade) + '\n')
                    break
                else:
                    print('---------------------------')
                    print(f'Quantidade insuficiente no estoque!')
                    print('---------------------------')
                    print(f'Produto: {i.produto.nome}')
                    print(f'Estoque disponível: {i.quantidade}')
                    print(f'Quantidade solicitada: {quantidadeVendida}')
                    print('---------------------------')
        else:
            print('---------------------------')
            print(f'O produto {nomeProduto} não existe no estoque!')
            print('---------------------------')

# a = ControllerEstoque()
# a.cadastrarProduto('Uva', '2', 'Frutas', 10)

a = ControllerVenda()
a.realizarVenda('Uva')