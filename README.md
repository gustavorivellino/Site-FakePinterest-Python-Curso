Este projeto é uma aplicação web inspirada no Pinterest, desenvolvida com Flask. As funcionalidades incluem:

Autenticação: Rotas de login e criação de conta usando o Flask-Login para autenticar usuários e proteger páginas específicas. As senhas são criptografadas com bcrypt para segurança.

Upload e Exibição de Fotos: Usuários podem fazer upload de fotos no perfil. As imagens são salvas com secure_filename para evitar problemas de segurança, e o caminho é armazenado no banco de dados.

Banco de Dados: O SQLAlchemy é utilizado como ORM para manipular dados dos usuários e das fotos. As tabelas armazenam informações de conta e fotos com seus respectivos usuários.

Interface de Usuário: Templates HTML renderizam formulários para login, criação de conta e upload de imagens. Há uma página de feed que exibe todas as fotos enviadas por usuários.

Rotas Principais:

/: Página inicial de login.
/criarconta: Permite criar uma nova conta.
/perfil/<id_usuario>: Página de perfil onde usuários podem visualizar e gerenciar suas fotos.
/logout: Desloga o usuário.
/feed: Exibe o feed com todas as fotos enviadas.

Esse projeto usa Flask-WTF para formulários, Flask-Bcrypt para segurança e Flask-Login para gerenciar sessões. É um sistema básico de compartilhamento de imagens com autenticação e um feed público.
