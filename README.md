# O que é API?
- É um conjunto de rotinas para acesso a um aplicativo/software/plataforma baseada na Web.
- Acrônimo de Application Programing Interface - Interface de programação de aplicativos.
- APIs são importantes quando se tem a intenção de realizar integrações com outros serviços.
- Com as APIs a comunicação de software fica transparente ao usuário.
- APIs podem ser locais, baseada em web e baseada em programas.

# O que é REST?
- É um modelo a ser utilizado para projetar arquiteturas de software baseado em comunicação via rede.
- Acrônimo de Representational State Transfer - Transferência de Estado Representacional.
- REST projeta a idéia de que todo recurso deveria responder aos mesmos métodos.

# O que é REST API?
- É uma API desenvolvida utilizando os princípios da arquitetura REST.
- Um REST API é utilizado na comunicação/ integração entre software através de serviços web.
- Um REST API é consumido através de requisiçõs HTTP.
- REST APIs são geralmente representadas em seus formatos por JSON e XML. Também são usados páginas HTML, PDF e arquivos de imagens.
- Ao implementar um REST API, cada método deve ser responsável por um tipo diferente de ação. Exemplo: Consulta, Alteração, Inclusão e Exclusão.

# Métodos do protocolo HTTP
- GET - Método que solicita algum recurso ou objeto do servidor por meio da URI.
- POST - Método usado para envio de arquivo/dados ou formulário HTML para o servidor.
- PUT - Aceitar criar ou modificar um objeto do servidor.
- DELETE - Informa por meio da URI o objeto a ser deletado.

# URL x URN x URI?
- URL: Uniform Resource Locator - Localizador de Recurso Universal. É o HOST que será acessado. ex: globallabs.academy.
- URN: Uniforme Resourse Name - Nome do Recurso Universal. É o recurso que será identificado. ex: /category/blog/
- URI: Uniform Resourse Identifier - Identificador de Recurso Universal. É o identificador da página. ex: https://globallabs.academy/category/blog. O URI une o Protocolo (https://), URL (globallabs.academy) e a URN (category/blog/).

# XML - Extensible Markup Language
- É uma linguagem de marcação muito utilizada para compartilhamento de informações através de requisições HTTP.

# JSON - JavaScript Obejct Notation
- É um formato de troca de dados entre sistemas independente da linguagem utilizada derivada do JavaScript, muitas linguages possuem suporte nativo a JSON.

# FLASK
- É um microframework para Python utilizado para desenvolvimento de aplicações WEB.
- É chamado de microframework porque mantém um núcleo simples, mas é estendível.
- Flask não possui camada de abstração para banco de dados, validação de formulários entre outros, mas é possível estender com outras bibliotecas.
- Por ser leve e simples de se usar, Flask é um dos frameworks Python mais utilizados para desenvolvimento de APIs.

# REST x RESTful
- REST é um estilo arquitetônico, um modelo para se seguir ao desenvolver APIs.
- RESTful é um serviço web que utiliza desse paradigma. É utilizado para definir aplicações que implementam webservices que utilizam a arquitetura REST.
- Podemos dizer que uma aplicação web que segue a arquitetura REST, é RESTful. ou seja, tem a capacidade de seguir a arquitetura REST.

# Flask-RESTful
- É uma extensão do Flask que adiciona suporte para a construção rápida de REST APIs.
- O uso Flask-RESTful acaba incentivando as práticas recomendadas para a arquitetura REST com configuração leve.

# APIs criadas no Repositório.
- run: API REST mostrando a mensagem 'Hello World' no localhost na porta 5000.
- first_api: API REST simples que soma números.
- task_api: API REST que gerencia cadastro de tarefas.
- Na Pasta dev_api:
    - dev_api: API REST que manipula registros em uma lista dados de funcionários.
    - dev_api_restful: API RESTful que manipula registros em uma lista dados de funcionários.
- API RESTful com persistencia no BD e autenticação:
    - api_atividade: API RESTful com manipulação de dados das tabelas Pessoa, Atividades e Usuarios, por meio de autenticação.
    - models: Código onde ficam os módelos de classes a serem persistidas no banco de dados.  
    - utils: Possui funções teste para manipulação das tabelas.
- OBS: Os métodos HTTP foram testado pelo Postman.
- OBS: O db de atividades é gerado na raiz da pasta.
