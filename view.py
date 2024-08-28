import os
import controller

def criar_arquivos(*args):
    """
    Cria arquivos de texto vazios para armazenar os dados do sistema.
    Verifica se o diretório 'arquivos' existe e, caso não exista, o cria.
    Em seguida, itera sobre os argumentos fornecidos e verifica se cada arquivo já existe.
    Se o arquivo não existir, ele é criado com conteúdo vazio.
    ----------------------------------------
    Parâmetros:
    *args: str
        Nomes dos arquivos a serem criados.
    """
    if not os.path.exists('arquivos'):
        os.makedirs('arquivos')

    for arquivo in args:
        if not os.path.exists(arquivo):
            with open(arquivo, 'w') as arq:
                arq.write('')

criar_arquivos('arquivos/categorias.txt', 
               'arquivos/estoque.txt', 
               'arquivos/fornecedores.txt', 
               'arquivos/clientes.txt', 
               'arquivos/funcionarios.txt', 
               'arquivos/vendas.txt')

if __name__ == "__main__":
    while True:
        menu_principal = int(input('============== MENU ===============\n'
                                   'Digite 1 para acessar [Categorias]\n'
                                    'Digite 2 para acessar [Estoque]\n'
                                    'Digite 3 para acessar [Fornecedor]\n'
                                    'Digite 4 para acessar [Cliente]\n'
                                    'Digite 5 para acessar [Funcionário]\n'
                                    'Digite 6 para acessar [Vendas]\n'
                                    'Digite 7 para acessar [+ Vendidos]\n'
                                    'Digite 0 para [sair]\n'
                                    '===================================\n'))
        
        if menu_principal == 1:
            cat = controller.ControllerCategoria()
            while True:
                menu_categoria = int(input('Digite 1 para [Cadastrar]\n'
                                           'Digite 2 para [Alterar]\n'
                                           'Digite 3 para [Remover]\n'
                                           'Digite 4 para [Listar]\n'
                                           'Digite 0 para sair\n'))
                if menu_categoria == 1:
                    categoria = input('Digite o nome da categoria que deseja cadastrar: ')
                    cat.cadastrarCategoria(categoria)
                elif menu_categoria == 2:
                    categoria = input('Digite o nome da categoria que deseja alterar: ')
                    novo_nome = input('Digite o novo nome da categoria: ')
                    cat.alterarCategoria(categoria, novo_nome)
                elif menu_categoria == 3:
                    categoria = input('Digite o nome da categoria que deseja remover: ')
                    cat.removerCategoria(categoria)
                elif menu_categoria == 4:
                    cat.listarCategorias()
                elif menu_categoria == 0:
                    print('Saindo...')
                    break
                else:
                    print('Opção inválida! Digite um número de 1 a 4, ou digite 0 para sair.')

        elif menu_principal == 2:
            est = controller.ControllerEstoque()
            while True:
                menu_estoque = int(input('Digite 1 para [Cadastrar]\n'
                                         'Digite 2 para [Alterar]\n'
                                         'Digite 3 para [Remover]\n'
                                         'Digite 4 para [Listar]\n'
                                         'Digite 0 para sair\n'))
                if menu_estoque == 1:
                    nome = input('Digite o nome do produto que deseja cadastrar: ')
                    quantidade = int(input('Digite a quantidade do produto: '))
                    preco = float(input('Digite o valor do produto: '))
                    categoria = input('Digite a categoria do produto: ')
                    est.cadastrarProduto(nome, preco, categoria, quantidade)
                elif menu_estoque == 2:
                    nome = input('Digite o nome do produto que deseja alterar: ')
                    novo_nome = input('Digite o novo nome do produto: ')
                    nova_quantidade = int(input('Digite a nova quantidade do produto: '))
                    novo_preco = float(input('Digite o novo valor do produto: '))
                    nova_categoria = input('Digite a nova categoria do produto: ')
                    est.alterarProduto(nome, novo_nome, novo_preco, nova_categoria, nova_quantidade)
                elif menu_estoque == 3:
                    nome = input('Digite o nome do produto que deseja remover: ')
                    est.removerProduto(nome)
                elif menu_estoque == 4:
                    est.listarProdutos()
                elif menu_estoque == 0:
                    print('Saindo...')
                    break
                else:
                    print('Opção inválida! Digite um número de 1 a 4, ou digite 0 para sair.')

        elif menu_principal == 3:
            forn = controller.ControllerFornecedor()
            while True:
                menu_fornecedor = int(input('Digite 1 para [Cadastrar]\n'
                                           'Digite 2 para [Alterar]\n'
                                           'Digite 3 para [Remover]\n'
                                           'Digite 4 para [Listar]\n'
                                           'Digite 0 para sair\n'))
                if menu_fornecedor == 1:
                    nome = input('Digite o nome do fornecedor que deseja cadastrar: ')
                    cnpj = input('Digite o CNPJ do fornecedor: ')
                    telefone = input('Digite o telefone do fornecedor: ')
                    categoria = input('Digite a categoria do fornecedor: ')
                    forn.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif menu_fornecedor == 2:
                    cnpj = input('Digite o CNPJ do fornecedor que deseja alterar: ')
                    novo_cnpj = input('Digite o novo CNPJ do fornecedor: ')
                    novo_nome = input('Digite o novo nome do fornecedor: ')
                    novo_telefone = input('Digite o novo telefone do fornecedor: ')
                    nova_categoria = input('Digite a nova categoria do fornecedor: ')
                    forn.alterarFornecedor(cnpj, novo_cnpj, novo_nome, novo_telefone, nova_categoria)
                elif menu_fornecedor == 3:
                    cnpj = input('Digite o CNPJ do fornecedor que deseja remover: ')
                    forn.removerFornecedor(cnpj)
                elif menu_fornecedor == 4:
                    forn.visualizarFornecedores()
                elif menu_fornecedor == 0:
                    print('Saindo...')
                    break
                else:
                    print('Opção inválida! Digite um número de 1 a 4, ou digite 0 para sair.')
        
        elif menu_principal == 4:
            cli = controller.ControllerCliente()
            while True:
                menu_cliente = int(input('Digite 1 para [Cadastrar]\n'
                                         'Digite 2 para [Alterar]\n'
                                         'Digite 3 para [Remover]\n'
                                         'Digite 4 para [Listar]\n'
                                         'Digite 0 para sair\n'))
                if menu_cliente == 1:
                    nome = input('Digite o nome do cliente que deseja cadastrar: ')
                    cpf = input('Digite o CPF do cliente: ')
                    telefone = input('Digite o telefone do cliente: ')
                    email = input('Digite o email do cliente: ')
                    endereco = input('Digite o endereço do cliente: ')
                    cli.cadastrarClientes(nome, telefone, cpf, email, endereco)
                elif menu_cliente == 2:
                    cpf = input('Digite o CPF do cliente que deseja alterar: ')
                    novo_cpf = input('Digite o novo CPF do cliente: ')
                    novo_nome = input('Digite o novo nome do cliente: ')
                    novo_telefone = input('Digite o novo telefone do cliente: ')
                    novo_email = input('Digite o novo email do cliente: ')
                    novo_endereco = input('Digite o novo endereço do cliente: ')
                    cli.alterarClientes(cpf, novo_cpf, novo_nome, novo_telefone, novo_email, novo_endereco)
                elif menu_cliente == 3:
                    cpf = input('Digite o CPF do cliente que deseja remover: ')
                    cli.removerClientes(cpf)
                elif menu_cliente == 4:
                    cli.visualizarClientes()
                elif menu_cliente == 0:
                    print('Saindo...')
                    break
                else:
                    print('Opção inválida! Digite um número de 1 a 4, ou digite 0 para sair.')

        elif menu_principal == 5:
            fun = controller.ControllerFuncionario()
            while True:
                menu_funcionario = int(input('Digite 1 para [Cadastrar]\n'
                                           'Digite 2 para [Alterar]\n'
                                           'Digite 3 para [Remover]\n'
                                           'Digite 4 para [Listar]\n'
                                           'Digite 0 para sair\n'))
                if menu_funcionario == 1:
                    nome = input('Digite o nome do funcionário que deseja cadastrar: ')
                    clt = input('Digite a CLT do funcionário: ')
                    cpf = input('Digite o CPF do funcionário: ')
                    telefone = input('Digite o telefone do funcionário: ')
                    email = input('Digite o email do funcionário: ')
                    endereco = input('Digite o endereço do funcionário: ')
                    fun.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif menu_funcionario == 2:
                    nome = input('Digite o nome do funcionário que deseja alterar: ')
                    novo_nome = input('Digite o novo nome do funcionário: ')
                    novo_clt = input('Digite a nova CLT do funcionário: ')
                    novo_cpf = input('Digite o novo CPF do funcionário: ')
                    novo_telefone = input('Digite o novo telefone do funcionário: ')
                    novo_email = input('Digite o novo email do funcionário: ')
                    novo_endereco = input('Digite o novo endereço do funcionário: ')
                    fun.alterarFuncionario(nome, novo_clt, novo_nome, novo_telefone, novo_cpf, novo_email, novo_endereco)
                elif menu_funcionario == 3:
                    nome = input('Digite o nome do funcionário que deseja remover: ')
                    fun.removerFuncionario(nome)
                elif menu_funcionario == 4:
                    fun.visualizarFuncionarios()
                elif menu_funcionario == 0:
                    print('Saindo...')
                    break
                else:
                    print('Opção inválida! Digite um número de 1 a 4, ou digite 0 para sair.')
        
        elif menu_principal == 6:
            ven = controller.ControllerVenda()
            while True:
                menu_vendas = int(input('Digite 1 para [Realizar venda]\n'
                                       'Digite 2 para [Visualizar vendas]\n'
                                       'Digite 0 para sair\n'))
                if menu_vendas == 1:
                    produto = input('Digite o nome do produto vendido: ')
                    quantidadeVendida = int(input('Digite a quantidade vendida do produto: '))
                    vendedor = input('Digite o nome do vendedor: ')
                    comprador = input('Digite o nome do comprador: ')
                    ven.realizarVenda(produto, vendedor, comprador, quantidadeVendida)
                elif menu_vendas == 2:
                    ven.visualizarVendas()
                elif menu_vendas == 0:
                    print('Saindo...')
                    break
                else:
                    print('Opção inválida! Digite um número de 1 a 4, ou digite 0 para sair.')

        elif menu_principal == 7:
            ven = controller.ControllerVenda()
            ven.relatorioVendas()
        
        elif menu_principal == 0:
            print('FINALIZANDO PROGRAMA')
            break

        else:
            print('Opção inválida! Digite um número de 1 a 7, ou digite 0 para sair.')