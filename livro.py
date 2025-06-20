class Livro:
    """Classe que representa um livro no catálogo"""
    
    def __init__(self, codigo=None, titulo="", autor="", genero="", editora="", ano_publicacao=0):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._editora = editora
        self._ano_publicacao = ano_publicacao
    
    # Propriedades com validação
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        if valor is not None and not isinstance(valor, int):
            raise ValueError("Código deve ser um número inteiro")
        if valor is not None and valor <= 0:
            raise ValueError("Código deve ser um número positivo")
        self._codigo = valor
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        if not isinstance(valor, str):
            raise ValueError("Título deve ser uma string")
        if not valor.strip():
            raise ValueError("Título não pode estar vazio")
        self._titulo = valor.strip()
    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, valor):
        if not isinstance(valor, str):
            raise ValueError("Autor deve ser uma string")
        if not valor.strip():
            raise ValueError("Autor não pode estar vazio")
        self._autor = valor.strip()
    
    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, valor):
        if not isinstance(valor, str):
            raise ValueError("Gênero deve ser uma string")
        if not valor.strip():
            raise ValueError("Gênero não pode estar vazio")
        self._genero = valor.strip()
    
    @property
    def editora(self):
        return self._editora
    
    @editora.setter
    def editora(self, valor):
        if not isinstance(valor, str):
            raise ValueError("Editora deve ser uma string")
        if not valor.strip():
            raise ValueError("Editora não pode estar vazio")
        self._editora = valor.strip()
    
    @property
    def ano_publicacao(self):
        return self._ano_publicacao
    
    @ano_publicacao.setter
    def ano_publicacao(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Ano de publicação deve ser um número inteiro")
        if valor < 1000 or valor > 2030:
            raise ValueError("Ano de publicação deve estar entre 1000 e 2030")
        self._ano_publicacao = valor
    
    def __str__(self):
        return f"Livro(código={self.codigo}, título='{self.titulo}', autor='{self.autor}')"
    
    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            'codigo': self.codigo,
            'titulo': self.titulo,
            'autor': self.autor,
            'genero': self.genero,
            'editora': self.editora,
            'ano_publicacao': self.ano_publicacao
        }
    
    @classmethod
    def from_dict(cls, dados):
        """Cria um objeto Livro a partir de um dicionário"""
        livro = cls()
        if 'codigo' in dados:
            livro.codigo = dados['codigo']
        livro.titulo = dados['titulo']
        livro.autor = dados['autor']
        livro.genero = dados['genero']
        livro.editora = dados['editora']
        livro.ano_publicacao = dados['ano_publicacao']
        return livro 