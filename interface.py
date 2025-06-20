import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter.ttk import Treeview
from livro import Livro
from database import DatabaseManager


class CatalogoInterface:
    """Interface gráfica para o catálogo de livros"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Livros")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        try:
            self.db_manager = DatabaseManager()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao inicializar banco de dados: {e}")
            self.root.destroy()
            return
        
        self.configurar_estilo()
        
        self.criar_interface()
        
        self.atualizar_lista()
    
    def configurar_estilo(self):
        """Configura o estilo da interface"""
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Heading.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Action.TButton', font=('Arial', 10))
    
    def criar_interface(self):
        """Cria todos os elementos da interface"""

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        
        titulo = ttk.Label(main_frame, text="Catálogo de Livros", style='Heading.TLabel')
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        self.criar_frame_entrada(main_frame)
        
        self.criar_frame_botoes(main_frame)
        
        self.criar_frame_lista(main_frame)
        
        self.criar_frame_busca(main_frame)

        self.criar_barra_status(main_frame)
    
    def criar_frame_entrada(self, parent):
        """Cria o frame com campos de entrada de dados"""
        frame_entrada = ttk.LabelFrame(parent, text="Dados do Livro", padding="10")
        frame_entrada.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N), padx=(0, 10))
        
        self.var_codigo = tk.StringVar()
        self.var_titulo = tk.StringVar()
        self.var_autor = tk.StringVar()
        self.var_genero = tk.StringVar()
        self.var_editora = tk.StringVar()
        self.var_ano = tk.StringVar()
        
        ttk.Label(frame_entrada, text="Código:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.entry_codigo = ttk.Entry(frame_entrada, textvariable=self.var_codigo, state='readonly')
        self.entry_codigo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2, padx=(5, 0))
        
        ttk.Label(frame_entrada, text="Título:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.entry_titulo = ttk.Entry(frame_entrada, textvariable=self.var_titulo)
        self.entry_titulo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2, padx=(5, 0))
        
        ttk.Label(frame_entrada, text="Autor:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.entry_autor = ttk.Entry(frame_entrada, textvariable=self.var_autor)
        self.entry_autor.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=2, padx=(5, 0))
        
        ttk.Label(frame_entrada, text="Gênero:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.entry_genero = ttk.Entry(frame_entrada, textvariable=self.var_genero)
        self.entry_genero.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=2, padx=(5, 0))
        
        ttk.Label(frame_entrada, text="Editora:").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.entry_editora = ttk.Entry(frame_entrada, textvariable=self.var_editora)
        self.entry_editora.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=2, padx=(5, 0))
        
        ttk.Label(frame_entrada, text="Ano:").grid(row=5, column=0, sticky=tk.W, pady=2)
        self.entry_ano = ttk.Entry(frame_entrada, textvariable=self.var_ano)
        self.entry_ano.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=2, padx=(5, 0))
        
        frame_entrada.grid_columnconfigure(1, weight=1)
    
    def criar_frame_botoes(self, parent):
        """Cria o frame com botões de ação"""
        frame_botoes = ttk.Frame(parent)
        frame_botoes.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N), padx=(10, 0))
        
        ttk.Button(frame_botoes, text="Adicionar", command=self.adicionar_livro,
                  style='Action.TButton').grid(row=0, column=0, pady=5, sticky=(tk.W, tk.E))
        ttk.Button(frame_botoes, text="Atualizar", command=self.atualizar_livro,
                  style='Action.TButton').grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))
        ttk.Button(frame_botoes, text="Deletar", command=self.deletar_livro,
                  style='Action.TButton').grid(row=2, column=0, pady=5, sticky=(tk.W, tk.E))
        ttk.Button(frame_botoes, text="Limpar", command=self.limpar_campos,
                  style='Action.TButton').grid(row=3, column=0, pady=5, sticky=(tk.W, tk.E))
        
        frame_botoes.grid_columnconfigure(0, weight=1)
    
    def criar_frame_lista(self, parent):
        """Cria o frame com a lista de livros"""
        frame_lista = ttk.LabelFrame(parent, text="Lista de Livros", padding="10")
        frame_lista.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(20, 0))
        
        frame_lista.grid_rowconfigure(0, weight=1)
        frame_lista.grid_columnconfigure(0, weight=1)
        
        colunas = ('Código', 'Título', 'Autor', 'Gênero', 'Editora', 'Ano')
        self.tree = ttk.Treeview(frame_lista, columns=colunas, show='headings', height=15)
        
        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        scrollbar_v = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar_h = ttk.Scrollbar(frame_lista, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=scrollbar_v.set, xscrollcommand=scrollbar_h.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar_v.grid(row=0, column=1, sticky=(tk.N, tk.S))
        scrollbar_h.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.tree.bind('<<TreeviewSelect>>', self.on_select)
    
    def criar_frame_busca(self, parent):
        """Cria o frame de busca"""
        frame_busca = ttk.LabelFrame(parent, text="Buscar Livros", padding="10")
        frame_busca.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))

        frame_busca.grid_columnconfigure(1, weight=1)

        ttk.Label(frame_busca, text="Buscar por:").grid(row=0, column=0, sticky=tk.W)

        self.combo_busca = ttk.Combobox(frame_busca, values=['Título', 'Autor'], state='readonly')
        self.combo_busca.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0))
        self.combo_busca.set('Título')

        self.var_busca = tk.StringVar()
        self.entry_busca = ttk.Entry(frame_busca, textvariable=self.var_busca)
        self.entry_busca.grid(row=0, column=2, sticky=(tk.W, tk.E), padx=(5, 0))

        ttk.Button(frame_busca, text="Buscar", command=self.buscar_livros).grid(row=0, column=3, padx=(5, 0))
        ttk.Button(frame_busca, text="Mostrar Todos", command=self.atualizar_lista).grid(row=0, column=4, padx=(5, 0))

        self.var_busca.trace('w', self.buscar_automatico)
    
    def criar_barra_status(self, parent):
        """Cria a barra de status"""
        self.status_var = tk.StringVar()
        self.status_var.set("Pronto")
        
        status_bar = ttk.Label(parent, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def atualizar_status(self, mensagem):
        """Atualiza a barra de status"""
        self.status_var.set(mensagem)
        self.root.update_idletasks()
    
    def validar_campos(self):
        """Valida os campos de entrada"""
        if not self.var_titulo.get().strip():
            raise ValueError("Título é obrigatório")
        if not self.var_autor.get().strip():
            raise ValueError("Autor é obrigatório")
        if not self.var_genero.get().strip():
            raise ValueError("Gênero é obrigatório")
        if not self.var_editora.get().strip():
            raise ValueError("Editora é obrigatória")
        if not self.var_ano.get().strip():
            raise ValueError("Ano é obrigatório")
        
        try:
            ano = int(self.var_ano.get())
            if ano < 1000 or ano > 2030:
                raise ValueError("Ano deve estar entre 1000 e 2030")
        except ValueError:
            raise ValueError("Ano deve ser um número inteiro válido")
    
    def criar_livro_from_campos(self):
        """Cria um objeto Livro a partir dos campos da interface"""
        self.validar_campos()
        
        livro = Livro()
        livro.titulo = self.var_titulo.get().strip()
        livro.autor = self.var_autor.get().strip()
        livro.genero = self.var_genero.get().strip()
        livro.editora = self.var_editora.get().strip()
        livro.ano_publicacao = int(self.var_ano.get())
        
        if self.var_codigo.get():
            livro.codigo = int(self.var_codigo.get())
        
        return livro
    
    def adicionar_livro(self):
        """Adiciona um novo livro"""
        try:
            livro = self.criar_livro_from_campos()
            codigo = self.db_manager.criar_livro(livro)
            
            self.atualizar_lista()
            self.limpar_campos()
            self.atualizar_status(f"Livro adicionado com sucesso! Código: {codigo}")
            messagebox.showinfo("Sucesso", f"Livro adicionado com código {codigo}")
            
        except ValueError as e:
            messagebox.showerror("Erro de Validação", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar livro: {e}")
    
    def atualizar_livro(self):
        """Atualiza um livro existente"""
        if not self.var_codigo.get():
            messagebox.showwarning("Aviso", "Selecione um livro para atualizar")
            return
        
        try:
            livro = self.criar_livro_from_campos()
            sucesso = self.db_manager.atualizar_livro(livro)
            
            if sucesso:
                self.atualizar_lista()
                self.limpar_campos()
                self.atualizar_status("Livro atualizado com sucesso!")
                messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Livro não encontrado para atualização")
                
        except ValueError as e:
            messagebox.showerror("Erro de Validação", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar livro: {e}")
    
    def deletar_livro(self):
        """Deleta um livro"""
        if not self.var_codigo.get():
            messagebox.showwarning("Aviso", "Selecione um livro para deletar")
            return
        
        resposta = messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar este livro?")
        if not resposta:
            return
        
        try:
            codigo = int(self.var_codigo.get())
            sucesso = self.db_manager.deletar_livro(codigo)
            
            if sucesso:
                self.atualizar_lista()
                self.limpar_campos()
                self.atualizar_status("Livro deletado com sucesso!")
                messagebox.showinfo("Sucesso", "Livro deletado com sucesso!")
            else:
                messagebox.showerror("Erro", "Livro não encontrado para exclusão")
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar livro: {e}")
    
    def limpar_campos(self):
        """Limpa todos os campos de entrada"""
        self.var_codigo.set("")
        self.var_titulo.set("")
        self.var_autor.set("")
        self.var_genero.set("")
        self.var_editora.set("")
        self.var_ano.set("")
        
        self.entry_codigo.config(state='readonly')
    
    def atualizar_lista(self):
        """Atualiza a lista de livros"""
        try:
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            livros = self.db_manager.listar_livros()
            
            for livro in livros:
                self.tree.insert('', 'end', values=(
                    livro.codigo,
                    livro.titulo,
                    livro.autor,
                    livro.genero,
                    livro.editora,
                    livro.ano_publicacao
                ))
            
            total = len(livros)
            self.atualizar_status(f"Total de livros: {total}")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar livros: {e}")
    
    def on_select(self, event):
        """Manipula a seleção de um item na lista"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            
            self.var_codigo.set(values[0])
            self.var_titulo.set(values[1])
            self.var_autor.set(values[2])
            self.var_genero.set(values[3])
            self.var_editora.set(values[4])
            self.var_ano.set(values[5])
    
    def buscar_livros(self):
        """Busca livros por título ou autor"""
        termo_busca = self.var_busca.get().strip()
        if not termo_busca:
            self.atualizar_lista()
            return
        
        try:
            tipo_busca = self.combo_busca.get()
            
            if tipo_busca == 'Título':
                livros = self.db_manager.buscar_livros_por_titulo(termo_busca)
            else:
                livros = self.db_manager.buscar_livros_por_autor(termo_busca)
            
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            for livro in livros:
                self.tree.insert('', 'end', values=(
                    livro.codigo,
                    livro.titulo,
                    livro.autor,
                    livro.genero,
                    livro.editora,
                    livro.ano_publicacao
                ))
            
            self.atualizar_status(f"Encontrados {len(livros)} livro(s) para '{termo_busca}'")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na busca: {e}")
    
    def buscar_automatico(self, *args):
        """Busca automática conforme o usuário digita"""
        self.root.after(500, self.buscar_livros) 