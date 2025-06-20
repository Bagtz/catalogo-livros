# 📚 Catálogo de Livros

Um sistema completo de gerenciamento de catálogo de livros desenvolvido em Python com interface gráfica usando Tkinter e banco de dados SQLite.

## 🚀 Funcionalidades

- ✅ **Interface Gráfica Intuitiva**: Desenvolvida com Tkinter
- ✅ **Operações CRUD Completas**:
  - **Create**: Adicionar novos livros
  - **Read**: Visualizar todos os livros
  - **Update**: Editar livros existentes
  - **Delete**: Excluir livros
- ✅ **Sistema de Busca**: Buscar por título ou autor
- ✅ **Persistência de Dados**: Banco de dados SQLite
- ✅ **Validação de Dados**: Validação completa dos campos
- ✅ **Tratamento de Exceções**: Tratamento robusto de erros
- ✅ **Interface Responsiva**: Redimensionável e otimizada

## 📋 Requisitos

- Python 3.7 ou superior
- Bibliotecas padrão do Python (tkinter, sqlite3, typing)

## 🗂️ Estrutura do Projeto

```
APP/
├── main.py           # Arquivo principal para executar a aplicação
├── livro.py          # Classe modelo Livro com validações
├── database.py       # Gerenciador do banco de dados SQLite
├── interface.py      # Interface gráfica com Tkinter
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação do projeto
```

## 📦 Campos do Livro

- **Código**: Número inteiro único (gerado automaticamente)
- **Título**: Texto obrigatório
- **Autor**: Texto obrigatório
- **Gênero**: Texto obrigatório
- **Editora**: Texto obrigatório
- **Ano de Publicação**: Número inteiro (1000-2030)

## 🚀 Como Executar

1. **Clone ou baixe o projeto**
2. **Navegue até o diretório do projeto**
3. **Execute o comando:**
   ```bash
   python main.py
   ```

## 🎯 Como Usar

### Adicionar um Novo Livro
1. Preencha todos os campos obrigatórios
2. Clique em "Adicionar"
3. O livro será salvo e um código será gerado automaticamente

### Editar um Livro
1. Clique em um livro na lista para selecioná-lo
2. Os campos serão preenchidos automaticamente
3. Modifique os dados desejados
4. Clique em "Atualizar"

### Excluir um Livro
1. Selecione um livro na lista
2. Clique em "Deletar"
3. Confirme a exclusão

### Buscar Livros
1. Escolha o tipo de busca (Título ou Autor) no dropdown
2. Digite o termo de busca
3. A busca é realizada automaticamente conforme você digita
4. Clique em "Mostrar Todos" para ver novamente todos os livros

### Limpar Campos
- Clique em "Limpar" para limpar todos os campos de entrada

## 🏗️ Arquitetura

### Programação Orientada a Objetos
- **Classe Livro**: Modelo de dados com validações
- **Classe DatabaseManager**: Gerencia todas as operações de banco de dados
- **Classe CatalogoInterface**: Interface gráfica completa

### Banco de Dados
- **SQLite**: Banco de dados local
- **Arquivo**: `catalogo_livros.db` (criado automaticamente)
- **Tabela**: `livros` com todos os campos necessários

## 🛡️ Tratamento de Exceções

O sistema inclui tratamento robusto de exceções para:
- Erros de validação de dados
- Erros de conexão com banco de dados
- Erros de interface gráfica
- Operações de CRUD

## 🔧 Validações Implementadas

- **Título, Autor, Gênero, Editora**: Não podem estar vazios
- **Ano de Publicação**: Deve ser número inteiro entre 1000 e 2030
- **Código**: Gerado automaticamente pelo banco de dados

## 📊 Funcionalidades Avançadas

- **Busca em Tempo Real**: Busca conforme você digita
- **Seleção Intuitiva**: Clique em um livro para editá-lo
- **Interface Responsiva**: Redimensionável com scrollbars
- **Barra de Status**: Mostra informações sobre operações
- **Confirmação de Exclusão**: Confirma antes de deletar

## 🎨 Interface

A interface é dividida em seções organizadas:
- **Entrada de Dados**: Campos para inserir/editar informações
- **Botões de Ação**: Adicionar, Atualizar, Deletar, Limpar
- **Lista de Livros**: Tabela com todos os livros ordenados por título
- **Sistema de Busca**: Busca por título ou autor
- **Barra de Status**: Informações sobre o estado da aplicação

## 🚨 Solução de Problemas

### Erro ao Inicializar
- Verifique se Python 3.7+ está instalado
- Certifique-se de que todos os arquivos estão no mesmo diretório

### Erro de Banco de Dados
- O arquivo `catalogo_livros.db` será criado automaticamente
- Verifique as permissões de escrita no diretório

### Erro de Interface
- Certifique-se de que o tkinter está instalado (geralmente incluído no Python)

## 👨‍💻 Desenvolvimento

Este projeto foi desenvolvido seguindo as melhores práticas:
- **PEP 8**: Padrão de codificação Python
- **Type Hints**: Tipagem para melhor manutenibilidade
- **Documentação**: Código bem documentado
- **Modularidade**: Código organizado em módulos

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais e pode ser utilizado livremente.

---

**Desenvolvido com ❤️ em Python** 