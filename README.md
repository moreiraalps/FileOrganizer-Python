# FileOrganizer-Python

Um script robusto e automatizado para organização de diretórios desordenados. Desenvolvido para facilitar a rotina de profissionais de TI e usuários comuns, movendo arquivos para pastas categorizadas com base em suas extensões.

## 🚀 Funcionalidades

- **Mapeamento Inteligente:** Identifica diversos tipos de extensões (Documentos, Imagens, Scripts, Executáveis, etc).
- **Criação Dinâmica:** Cria as pastas de destino automaticamente caso elas não existam.
- **Segurança de I/O:** Utiliza a biblioteca `shutil` para garantir a integridade dos arquivos durante a movimentação.
- **Log em Tempo Real:** Exibe no terminal cada ação realizada para acompanhamento do usuário.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Bibliotecas Nativas:** - `os`: Para manipulação de caminhos e diretórios.
  - `shutil`: Para operações de alto nível em arquivos (mover/copiar).

## 📋 Como o sistema funciona

O fluxo segue uma lógica de validação sequencial:
1. O usuário insere o caminho da pasta.
2. O script varre todos os arquivos do diretório raiz.
3. Cada arquivo tem sua extensão extraída e comparada com o dicionário de categorias.
4. O arquivo é movido para sua respectiva pasta. Arquivos desconhecidos são movidos para a pasta `/Outros`.

## ⚙️ Como Executar

1. Certifique-se de ter o **Python** instalado.
2. Clone este repositório ou baixe o arquivo `organizer.py`.
3. Navegue até a pasta do projeto e execute:
   ```bash
   python organizer.py
