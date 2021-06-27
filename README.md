# InstaAccountScraping
Retorna tabela excel com número de posts, seguidores e seguidos de lista de usuários do instagram dada a partir de interação com selenium.

## Setup
* Para que o projeto seja executado corretamente, garante a instalação e configuração do `Python 3.8.x` e `pip` (como [nesse tutorial](https://python.org.br/instalacao-windows/)).
* Clone o diretório ou baixe os arquivos pelo [link](https://github.com/Ocramoi/InstaAccountScraping/releases/download/v0.1/release_0_1.zip).
* Acesse o diretório clonado ou descompacte o arquivo baixado.

## Configuração
* Dentro de um ambiente virtual ou no python de sistema, instale os requerimentos do projeto com `pip install -r requirements.txt`. 
* A lista de usuários deve ser dada pelo arquivo `lista.txt`, com um usuário por linha (sem @).
* A tabela de saída por padrão terá nome `tabela.xlsx`, porém isso, aleḿ do nome do arquivo de entrada e pausa entre requisições podem ser modificadas no arquivo `env.py`.

## Execução 
* Com os arquivos preparados e configurados, simplesmente rode `main.py` com sua versão do python, como: `python main.py`.
* Uma nova janela do navegador será aberta, faça login e siga como indicado.
