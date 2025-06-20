import sqlite3
from typing import List, Optional
from livro import Livro


class DatabaseManager:
    """Classe responsável por gerenciar a conexão e operações com o banco de dados"""
    
    def __init__(self, db_name: str = "catalogo_livros.db"):
        self.db_name = db_name
        self.criar_tabela()
    
    def obter_conexao(self):
        """Cria uma conexão com o banco de dados"""
        try:
            conn = sqlite3.connect(self.db_name)
            conn.row_factory = sqlite3.Row 
            return conn
        except sqlite3.Error as e:
            raise Exception(f"Erro ao conectar com o banco de dados: {e}")
    
    def criar_tabela(self):
        """Cria a tabela de livros se ela não existir"""
        try:
            with self.obter_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS livros (
                        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        genero TEXT NOT NULL,
                        editora TEXT NOT NULL,
                        ano_publicacao INTEGER NOT NULL
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Erro ao criar tabela: {e}")
    
    def criar_livro(self, livro: Livro) -> int:
        """
        Insere um novo livro no banco de dados
        Retorna o código do livro inserido
        """
        try:
            with self.obter_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO livros (titulo, autor, genero, editora, ano_publicacao)
                    VALUES (?, ?, ?, ?, ?)
                ''', (livro.titulo, livro.autor, livro.genero, livro.editora, livro.ano_publicacao))
                
                codigo_inserido = cursor.lastrowid
                conn.commit()
                return codigo_inserido
        except sqlite3.IntegrityError as e:
            raise Exception(f"Erro de integridade: {e}")
        except sqlite3.Error as e:
            raise Exception(f"Erro ao inserir livro: {e}")
    
    def listar_livros(self) -> List[Livro]:
        """Retorna todos os livros do banco de dados"""
        try:
            with self.obter_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM livros ORDER BY titulo')
                rows = cursor.fetchall()
                
                livros = []
                for row in rows:
                    dados = {
                        'codigo': row['codigo'],
                        'titulo': row['titulo'],
                        'autor': row['autor'],
                        'genero': row['genero'],
                        'editora': row['editora'],
                        'ano_publicacao': row['ano_publicacao']
                    }
                    livros.append(Livro.from_dict(dados))
                
                return livros
        except sqlite3.Error as e:
            raise Exception(f"Erro ao listar livros: {e}")
    
    def buscar_livro_por_codigo(self, codigo: int) -> Optional[Livro]:
        """Busca um livro específico pelo código"""
        try:
            with self.obter_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM livros WHERE codigo = ?', (codigo,))
                row = cursor.fetchone()
                
                if row:
                    dados = {
                        'codigo': row['codigo'],
                        'titulo': row['titulo'],
                        'autor': row['autor'],
                        'genero': row['genero'],
                        'editora': row['editora'],
                        'ano_publicacao': row['ano_publicacao']
                    }
                    return Livro.from_dict(dados)
                return None
        except sqlite3.Error as e:
            raise Exception(f"Erro ao buscar livro: {e}")
    
    def atualizar_livro(self, livro: Livro) -> bool:
        """
        Atualiza um livro existente no banco de dados
        Retorna True se a atualização foi bem-sucedida
        """
        try:
            with self.obter_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE livros 
                    SET titulo = ?, autor = ?, genero = ?, editora = ?, ano_publicacao = ?
                    WHERE codigo = ?
                ''', (livro.titulo, livro.autor, livro.genero, livro.editora, 
                      livro.ano_publicacao, livro.codigo))
                
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            raise Exception(f"Erro ao atualizar livro: {e}")
    
    def deletar_livro(self, codigo: int) -> bool:
        """
        Remove um livro do banco de dados
        Retorna True se a remoção foi bem-sucedida
        """
        try:
            with self.obter_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM livros WHERE codigo = ?', (codigo,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            raise Exception(f"Erro ao deletar livro: {e}")
    
    def buscar_livros_por_titulo(self, titulo: str) -> List[Livro]:
        """Busca livros que contenham o título especificado"""
        try:
            with self.obter_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT * FROM livros WHERE titulo LIKE ? ORDER BY titulo',
                    (f'%{titulo}%',)
                )
                rows = cursor.fetchall()
                
                livros = []
                for row in rows:
                    dados = {
                        'codigo': row['codigo'],
                        'titulo': row['titulo'],
                        'autor': row['autor'],
                        'genero': row['genero'],
                        'editora': row['editora'],
                        'ano_publicacao': row['ano_publicacao']
                    }
                    livros.append(Livro.from_dict(dados))
                
                return livros
        except sqlite3.Error as e:
            raise Exception(f"Erro ao buscar livros por título: {e}")
    
    def buscar_livros_por_autor(self, autor: str) -> List[Livro]:
        """Busca livros pelo autor"""
        try:
            with self.obter_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT * FROM livros WHERE autor LIKE ? ORDER BY titulo',
                    (f'%{autor}%',)
                )
                rows = cursor.fetchall()
                
                livros = []
                for row in rows:
                    dados = {
                        'codigo': row['codigo'],
                        'titulo': row['titulo'],
                        'autor': row['autor'],
                        'genero': row['genero'],
                        'editora': row['editora'],
                        'ano_publicacao': row['ano_publicacao']
                    }
                    livros.append(Livro.from_dict(dados))
                
                return livros
        except sqlite3.Error as e:
            raise Exception(f"Erro ao buscar livros por autor: {e}")
    
    def contar_livros(self) -> int:
        """Retorna o número total de livros no catálogo"""
        try:
            with self.obter_conexao() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT COUNT(*) FROM livros')
                return cursor.fetchone()[0]
        except sqlite3.Error as e:
            raise Exception(f"Erro ao contar livros: {e}") 