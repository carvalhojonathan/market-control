from models import *

class DaoCategoria:
    """
    Classe de acesso a dados para a entidade Categoria.

    Métodos:
    --------
    salvar(cls, categoria):
        Salva uma nova categoria no arquivo 'categorias.txt'.
    
    ler(cls):
        Lê todas as categorias do arquivo 'categorias.txt' e retorna uma lista de objetos Categoria.
    """

    @classmethod
    def salvar(cls, categoria):
        with open('arquivos/categorias.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
            
    @classmethod
    def ler(cls):
        with open('arquivos/categorias.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat

class DaoVenda:
    """
    Classe de acesso a dados para a entidade Venda.

    Métodos:
    --------
    salvar(cls, venda):
        Salva uma nova venda no arquivo 'vendas.txt'.
    
    ler(cls):
        Lê todas as vendas do arquivo 'vendas.txt' e retorna uma lista de objetos Venda.
    """

    @classmethod
    def salvar(cls, venda):
        with open('arquivos/vendas.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + '|' + 
                           str(venda.itensVendidos.preco) + '|' +  
                           venda.itensVendidos.categoria + '|' + 
                           venda.vendedor + '|' + 
                           venda.comprador + '|' + 
                           str(venda.quantidadeVendida) + '|' + 
                           venda.data)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('arquivos/vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()
        
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        
        return vend

class DaoEstoque:
    """
    Classe de acesso a dados para a entidade Estoque.

    Métodos:
    --------
    salvar(cls, produto, quantidade):
        Salva um novo item de estoque no arquivo 'estoque.txt'.
    
    ler(cls):
        Lê todos os itens de estoque do arquivo 'estoque.txt' e retorna uma lista de objetos Estoque.
    """

    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('arquivos/estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' +
                           str(produto.preco) + '|' + 
                           produto.categoria + '|' + 
                           str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('arquivos/estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                produto = Produtos(i[0], i[1], i[2])
                quantidade = int(i[3])
                est.append(Estoque(produto, quantidade))
        
        return est
    
class DaoFornecedor:
    """
    Classe de acesso a dados para a entidade Fornecedor.

    Métodos:
    --------
    salvar(cls, fornecedor):
        Salva um novo fornecedor no arquivo 'fornecedores.txt'.
    
    ler(cls):
        Lê todos os fornecedores do arquivo 'fornecedores.txt' e retorna uma lista de objetos Fornecedor.
    """

    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('arquivos/fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' + 
                           fornecedor.cnpj + '|' + 
                           fornecedor.telefone + '|' + 
                           fornecedor.categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('arquivos/fornecedores.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()
        
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        
        return forn
    
class DaoPessoa:
    """
    Classe de acesso a dados para a entidade Pessoa.

    Métodos:
    --------
    salvar(cls, pessoa):
        Salva uma nova pessoa no arquivo 'clientes.txt'.
    
    ler(cls):
        Lê todas as pessoas do arquivo 'clientes.txt' e retorna uma lista de objetos Pessoa.
    """

    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('arquivos/clientes.txt', 'a') as arq:
            arq.writelines(pessoa.nome + '|' + 
                           pessoa.telefone + '|' + 
                           pessoa.cpf + '|' + 
                           pessoa.email + '|' + 
                           pessoa.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('arquivos/clientes.txt', 'r') as arq:
            cls.pessoa = arq.readlines()
        
        cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))
        cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa))

        pes = []
        for i in cls.pessoa:
            pes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        
        return pes

class DaoFuncionario:
    """
    Classe de acesso a dados para a entidade Funcionario.

    Métodos:
    --------
    salvar(cls, funcionario):
        Salva um novo funcionário no arquivo 'funcionarios.txt'.
    
    ler(cls):
        Lê todos os funcionários do arquivo 'funcionarios.txt' e retorna uma lista de objetos Funcionario.
    """

    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('arquivos/funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + '|' + 
                           funcionario.nome + '|' + 
                           funcionario.telefone + '|' + 
                           funcionario.cpf + '|' + 
                           funcionario.email + '|' + 
                           funcionario.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('arquivos/funcionarios.txt', 'r') as arq:
            cls.funcionario = arq.readlines()
        
        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))

        func = []
        for i in cls.funcionario:
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        
        return func