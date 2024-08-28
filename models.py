from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        """
        Inicializa uma nova categoria.

        Parâmetros:
        -----------
        categoria : str
            Nome da categoria.
        """
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):
        """
        Inicializa um novo produto.

        Parâmetros:
        -----------
        nome : str
            Nome do produto.
        preco : float
            Preço do produto.
        categoria : Categoria
            Categoria do produto.
        """
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        """
        Inicializa um novo item de estoque.

        Parâmetros:
        -----------
        produto : Produtos
            Produto no estoque.
        quantidade : int
            Quantidade do produto no estoque.
        """
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendidos: Produtos, vendedor, comprador, 
                 quantidadeVendida, data = datetime.now().strftime('%d/%m/%Y')):
        """
        Inicializa uma nova venda.

        Parâmetros:
        -----------
        itensVendidos : Produtos
            Produto vendido.
        vendedor : str
            Nome do vendedor.
        comprador : str
            Nome do comprador.
        quantidadeVendida : int
            Quantidade vendida do produto.
        data : str, opcional
            Data da venda no formato 'dd/mm/yyyy'. Padrão é a data atual.
        """
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        """
        Inicializa um novo fornecedor.

        Parâmetros:
        -----------
        nome : str
            Nome do fornecedor.
        cnpj : str
            CNPJ do fornecedor.
        telefone : str
            Telefone do fornecedor.
        categoria : Categoria
            Categoria fornecida.
        """
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        """
        Inicializa uma nova pessoa.

        Parâmetros:
        -----------
        nome : str
            Nome da pessoa.
        telefone : str
            Telefone da pessoa.
        cpf : str
            CPF da pessoa.
        email : str
            Email da pessoa.
        endereco : str
            Endereço da pessoa.
        """
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        """
        Inicializa um novo funcionário.

        Parâmetros:
        -----------
        clt : str
            Número da carteira de trabalho do funcionário.
        nome : str
            Nome do funcionário.
        telefone : str
            Telefone do funcionário.
        cpf : str
            CPF do funcionário.
        email : str
            Email do funcionário.
        endereco : str
            Endereço do funcionário.
        """
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)