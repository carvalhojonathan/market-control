from models import *
from dao import *
from datetime import datetime, timedelta

class ControllerCategoria:
    """
    Classe responsável por controlar as operações relacionadas às categorias.
    Métodos:
    - cadastrarCategoria(novaCategoria): Cadastra uma nova categoria.
    - removerCategoria(categoriaRemover): Remove uma categoria existente.
    - alterarCategoria(categoriaAtual, novaCategoria): Altera o nome de uma categoria existente.
    - listarCategorias(): Lista todas as categorias cadastradas.
    """
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
            with open('arquivos/categorias.txt', 'w') as arq:
                [arq.write(f'{i.categoria}\n') for i in x]

        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem categoria'), x.quantidade) 
                           if (x.produto.categoria == categoriaRemover) else (x), estoque))
        with open('arquivos/estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + 
                               str(i.produto.preco) + '|' + 
                               i.produto.categoria + '|' + 
                               str(i.quantidade) + '\n')

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

                estoque = DaoEstoque.ler()
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Categoria alterada'), x.quantidade) 
                                   if (x.produto.categoria == categoriaAtual) else (x), estoque))
                with open('arquivos/estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + '|' + 
                                    str(i.produto.preco) + '|' + 
                                    i.produto.categoria + '|' + 
                                    str(i.quantidade) + '\n')

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
    """
    Classe responsável por controlar o estoque de produtos.
    Métodos:
    - cadastrarProduto(nome, preco, categoria, quantidade): Cadastra um novo produto no estoque.
    - removerProduto(nome): Remove um produto do estoque.
    - alterarProduto(nome, novoNome, novoPreco, novaCategoria, novaQuantidade): Altera as informações de um produto no estoque.
    - listarProdutos(): Lista todos os produtos cadastrados no estoque.
    """
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
    """
    Classe responsável por controlar as vendas e gerar relatórios.
    Métodos:
    - realizarVenda: Realiza uma venda de um produto específico.
    - relatorioVendas: Gera um relatório de vendas, mostrando a quantidade vendida de cada produto.
    - visualizarVendas: Visualiza as vendas realizadas em um período de tempo específico.
    """
    def realizarVenda(self, nomeProduto, vendedor = 'admin', comprador = 'nao identificado', quantidadeVendida = 1):
        x = DaoEstoque.ler()
        prod = list(filter(lambda x: x.produto.nome == nomeProduto, x))
        if len(prod) > 0:
            for i in prod:
                if i.quantidade >= quantidadeVendida:
                    i.quantidade -= quantidadeVendida
                    vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
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

    def relatorioVendas(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade = int(i.quantidadeVendida)
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': x['quantidade']+quantidade} 
                                    if x['produto'] == nome else (x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})
            
        produtosOrdernados = sorted(produtos, key = lambda x: x['quantidade'], reverse = True)
        print('---------------------------')
        print('--- RELATÓRIO DE VENDAS ---')
        print('---------------------------')
        print(f'{"#. Produto":<10}    | {"Quantidade":>10}')
        print('---------------------------')
        if produtosOrdernados == []:
            print('Nenhuma venda realizada!')
        else:
            for i, produto in enumerate(produtosOrdernados, start=1):
                print(f'{i}. {produto["produto"]:<10} | {produto["quantidade"]:>10}')
        print('---------------------------')

    def visualizarVendas(self, dataInicial = (datetime.now() - timedelta(days=30)).strftime('%d/%m/%Y'), dataFinal = datetime.now().strftime('%d/%m/%Y')):
        vendas = DaoVenda.ler()
        dataInicial1 = datetime.strptime(dataInicial, '%d/%m/%Y')
        dataFinal1 = datetime.strptime(dataFinal, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicial1 
                                         and datetime.strptime(x.data, '%d/%m/%Y') <= dataFinal1, vendas))
        
        for i, venda in enumerate(vendasSelecionadas, start=1):
            print('---------------------------')
            print(f'Venda nº {i}')
            print('---------------------------')
            print(f'Produto: {venda.itensVendidos.nome}')
            print(f'Vendedor: {venda.vendedor}')
            print(f'Comprador: {venda.comprador}')
            print(f'Quantidade: {venda.quantidadeVendida}')
            print(f'Valor: R$ {int(venda.itensVendidos.preco) * int(venda.quantidadeVendida)}')
            print(f'Data: {venda.data}')
        print('---------------------------')
        print(f'TOTAL VENDIDO: R$ {sum([int(venda.itensVendidos.preco) * int(venda.quantidadeVendida) for venda in vendasSelecionadas])}')
        print('---------------------------')

class ControllerFornecedor:
    """
    Classe responsável por controlar as operações relacionadas aos fornecedores.
    Métodos:
    - cadastrarFornecedor: cadastra um novo fornecedor.
    - alterarFornecedor: altera os dados de um fornecedor existente.
    - removerFornecedor: remove um fornecedor existente.
    - visualizarFornecedores: exibe os fornecedores cadastrados.
    """
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))
        if len(listaCnpj) > 0:
            print('Já existe um fornecedor com este CNPJ!')
        elif len(listaTelefone) > 0:
            print('Já existe um fornecedor com este telefone!')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                fornecedor = Fornecedor(nome, cnpj, telefone, categoria)
                DaoFornecedor.salvar(fornecedor)
                print('Fornecedor cadastrado com sucesso!')
            else:
                print('CNPJ ou telefone inválido!')
    
    def alterarFornecedor(self, cnpjAtual, novoCnpj, novoNome, novoTelefone, novaCategoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpjAtual, x))
        if len(listaCnpj) > 0:
            forn = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(forn) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) 
                             if (x.cnpj == cnpjAtual) else (x), x))
                print('Fornecedor alterado com sucesso!')
                with open('arquivos/fornecedores.txt', 'w') as arq:
                    for i in x:
                        arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + i.categoria + '\n')
            else:
                print('Já existe um fornecedor com este CNPJ!')
        else:
            print('Fornecedor não encontrado!')

    def removerFornecedor(self, cnpj):
        x = DaoFornecedor.ler()
        forn = list(filter(lambda x: x.cnpj == cnpj, x))
        if len(forn) > 0:
            for i in range(len(x)):
                if x[i].cnpj == cnpj:
                    del x[i]
                    break
            print('Fornecedor removido com sucesso!')
            with open('arquivos/fornecedores.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + i.categoria + '\n')
        else:
            print('Fornecedor não encontrado!')

    def visualizarFornecedores(self):
        x = DaoFornecedor.ler()
        if len(x) == 0:
            print('Nenhum fornecedor cadastrado!')
        else:
            print('--------------------')
            print('--- FORNECEDORES ---')
            print('--------------------')
            for i in x:
                print(f'Nome: {i.nome}')
                print(f'CNPJ: {i.cnpj}')
                print(f'Telefone: {i.telefone}')
                print(f'Categoria: {i.categoria}')
                print('--------------------')

class ControllerCliente:
    """
    Classe responsável por controlar as operações relacionadas aos clientes.
    Métodos:
    - cadastrarClientes(nome, telefone, cpf, email, endereco): Cadastra um novo cliente.
    - alterarClientes(cpfAtual, novoCpf, novoNome, novoTelefone, novoEmail, novoEndereco): Altera os dados de um cliente existente buscando pelo CPF.
    - removerClientes(cpf): Remove um cliente buscando pelo CPF.
    - visualizarClientes(): Exibe todos os clientes cadastrados.
    """
    def cadastrarClientes(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('Já existe um cliente com este CPF!')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                cliente = Pessoa(nome, telefone, cpf, email, endereco)
                if cliente in x:
                    print('Já existe um cliente com este CPF!')
                else:
                    DaoPessoa.salvar(cliente)
                    print('Cliente cadastrado com sucesso!')
            else:
                print('CPF ou telefone inválido!')
    
    def alterarClientes(self, cpfAtual, novoCpf, novoNome, novoTelefone, novoEmail, novoEndereco):
        x = DaoPessoa.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpfAtual, x))
        if len(listaCpf) > 0:
            cli = list(filter(lambda x: x.cpf == novoCpf, x))
            if len(cli) == 0:
                x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) 
                             if (x.cpf == cpfAtual) else (x), x))
                print('Cliente alterado com sucesso!')
                with open('arquivos/clientes.txt', 'w') as arq:
                    for i in x:
                        arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco + '\n')
            else:
                print('Já existe um cliente com este CPF!')
        else:
            print('Cliente não encontrado!')

    def removerClientes(self, cpf):
        x = DaoPessoa.ler()
        cli = list(filter(lambda x: x.cpf == cpf, x))
        if len(cli) > 0:
            for i in range(len(x)):
                if x[i].cpf == cpf:
                    del x[i]
                    break
            print(f'Cliente `{cli[0].nome}´ removido com sucesso!')
            with open('arquivos/clientes.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco + '\n')
        else:
            print('Cliente não encontrado!')

    def visualizarClientes(self):
        x = DaoPessoa.ler()
        if len(x) == 0:
            print('Nenhum cliente cadastrado!')
        else:
            print('-------------------')
            print('---- CLIENTES ----')
            print('-------------------')
            for i in x:
                print(f'Nome: {i.nome}')
                print(f'CPF: {i.cpf}')
                print(f'Telefone: {i.telefone}')
                print(f'Email: {i.email}')
                print(f'Endereço: {i.endereco}')
                print('-------------------')

class ControllerFuncionario:
    """
    Classe responsável por controlar as operações relacionadas aos funcionários.
    Métodos:
    - cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco): Cadastra um novo funcionário.
    - alterarFuncionario(nomeAtual, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco): Altera os dados de um funcionário existente buscando pelo nome.
    - removerFuncionario(nome): Remove um funcionário existente buscando pelo nome.
    - visualizarFuncionarios(): Exibe a lista de funcionários cadastrados.
    """
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listaCpf) > 0:
            print('Já existe um funcionário com este CPF!')
        elif len(listaClt) > 0:
            print('Já existe um funcionário com esta CLT!')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                funcionario = Funcionario(clt, nome, telefone, cpf, email, endereco)
                DaoFuncionario.salvar(funcionario)
                print('Funcionário cadastrado com sucesso!')
            else:
                print('CPF ou telefone inválido!')
    
    def alterarFuncionario (self, nomeAtual, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()
        busca = list(filter(lambda x: x.nome == nomeAtual, x))
        if len(busca) > 0:
            func = list(filter(lambda x: x.clt == novoClt, x))
            if len(func) == 0:
                x = list(map(lambda x: Funcionario(novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) 
                             if (x.nome == nomeAtual) else (x), x))
                print('Funcionário alterado com sucesso!')
                with open('arquivos/funcionarios.txt', 'w') as arq:
                    for i in x:
                        arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco + '\n')
            else:
                print('Já existe um funcionário com esta CLT!')
        else:
            print('Funcionário não encontrado!')

    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()
        func = list(filter(lambda x: x.nome == nome, x))
        if len(func) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
            print(f'Funcionário `{func[0].nome}´ removido com sucesso!')
            with open('arquivos/funcionarios.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco + '\n')
        else:
            print('Funcionário não encontrado!')

    def visualizarFuncionarios(self):
        x = DaoFuncionario.ler()
        if len(x) == 0:
            print('Nenhum funcionário cadastrado!')
        else:
            print('-------------------')
            print('--- FUNCIONÁRIOS ---')
            print('-------------------')
            for i in x:
                print(f'CLT: {i.clt}')
                print(f'Nome: {i.nome}')
                print(f'Telefone: {i.telefone}')
                print(f'CPF: {i.cpf}')
                print(f'Email: {i.email}')
                print(f'Endereço: {i.endereco}')
                print('-------------------')

