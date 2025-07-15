# 📦 FME Stock Control

**FME Stock Control** é um sistema de gerenciamento de estoque em modo console desenvolvido em **Python**. Ele permite o controle completo de produtos, entradas, saídas e usuários. Os dados são persistidos em arquivos `.txt` armazenados localmente.

---

## 📌 Sobre o Projeto

O objetivo principal deste projeto é aplicar conceitos de **lógica de programação**, **manipulação de arquivos** e **estruturas de dados**, através de um sistema funcional com interface de linha de comando (CLI).

### Funcionalidades

- ✅ Cadastro e gerenciamento de produtos
- ✅ Controle de entrada e saída de produtos
- ✅ Autenticação de múltiplos usuários
- ✅ Armazenamento de dados em arquivos locais (`.txt`)

> Este projeto foi desenvolvido como trabalho acadêmico da disciplina de **Lógica de Programação**.

---

## 🗂️ Estrutura de Diretórios

```bash
FME-STOCK-CONTROL/
├── src/                           # Código principal (menus e execução)
│   └── startup.py                 # Ponto de entrada da aplicação
├──   lib/                         # Funções auxiliares
│       └── fileLibrary.py         # Manipulação de arquivos (.txt)
├──   services/                    # Funcionalidades do sistema
│       ├── entrada_produtos.py
│       ├── produto.py
│       ├── saida_produtos.py
│       └── usuario.py
├──   storage/                     # Persistência de dados
│       ├── entrada.txt
│       ├── produtos.txt
│       ├── saida.txt
│       └── usuarios.txt
└── README.md

```     

## 🚀 Como Executar o Projeto

---

### 💻 Opção 1 — Usando o Visual Studio Code

1. Abra o projeto no Visual Studio Code
2. Navegue até o arquivo `src/startup.py`
3. Pressione F5 para iniciar
4. Se necessário, selecione a opção `"Python File - Current Active File"`


> 🔧 Certifique-se de ter a extensão Python instalada e o interpretador Python corretamente configurado
---

### 🖥️ Opção 2 — Usando o Terminal

1. Abra o terminal (CMD, Bash, etc.)
2. Navegue até o diretório ```src```:

3. ```bash
    cd FME-STOCK-CONTROL/src
    Execute o arquivo de inicialização:
   ```
4. ```bash
    python startup.py
   ```

> 📦 Você precisa ter o Python instalado e adicionado ao PATH do sistema

---

## 🛠️ Dicas Úteis
---

- ✅ Instale a extensão Python no VS Code (desenvolvida pela Microsoft)
- ✅ Use a extensão Code Runner para rodar scripts com um clique
- ✅ Mantenha os arquivos .txt na pasta storage/ para evitar erros na execução
- ✅ Teste os módulos separadamente, se quiser entender cada funcionalidade de forma modular