#!/usr/bin/env python3
"""
Catálogo de Livros - Aplicação Principal
Desenvolvido com Python, Tkinter e SQLite
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Adicionar o diretório atual ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from interface import CatalogoInterface
except ImportError as e:
    print(f"Erro ao importar módulos: {e}")
    sys.exit(1)


def main():
    """Função principal que executa a aplicação"""
    try:
        # Criar janela principal
        root = tk.Tk()
        
        # Configurar ícone (opcional)
        try:
            # Se houver um ícone, descomente a linha abaixo
            # root.iconbitmap('icon.ico')
            pass
        except:
            pass
        
        # Centralizar a janela na tela
        root.update_idletasks()
        width = 900
        height = 700
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Definir tamanho mínimo
        root.minsize(800, 600)
        
        # Criar a aplicação
        app = CatalogoInterface(root)
        
        # Configurar evento de fechamento
        def on_closing():
            """Manipula o fechamento da aplicação"""
            if messagebox.askokcancel("Sair", "Deseja realmente sair do catálogo?"):
                root.destroy()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Exibir informações sobre a aplicação
        print("=" * 50)
        print("    CATÁLOGO DE LIVROS - VERSÃO 1.0")
        print("=" * 50)
        print("Aplicação iniciada com sucesso!")
        print("Funcionalidades disponíveis:")
        print("• Adicionar novos livros")
        print("• Visualizar todos os livros")
        print("• Editar livros existentes")
        print("• Excluir livros")
        print("• Buscar por título ou autor")
        print("• Banco de dados SQLite para persistência")
        print("=" * 50)
        
        # Iniciar loop principal da interface
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Erro Fatal", f"Erro ao inicializar aplicação: {e}")
        print(f"Erro fatal: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 