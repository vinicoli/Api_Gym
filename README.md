# Projeto API para Controle de Academia

Este projeto tem como objetivo desenvolver uma API utilizando o Django Rest Framework para fornecer um sistema de controle completo para uma academia. A API permitirá o gerenciamento de alunos, instrutores, planos de treino, horários de aulas e muito mais. Com essa API, será possível criar, ler, atualizar e excluir dados relacionados à academia de forma eficiente e segura.

## Funcionalidades Principais

A API para controle de academia oferecerá as seguintes funcionalidades principais:

1. **Gerenciamento de Alunos**: Cadastro, listagem, edição e remoção de alunos, incluindo informações pessoais, histórico de pagamentos e presença nas aulas.

2. **Gerenciamento de Instrutores**: Cadastro, listagem, edição e remoção de instrutores, contendo informações sobre as especialidades e horários disponíveis.

3. **Gerenciamento de Planos de Treino**: Criação, listagem, edição e exclusão de planos de treino, detalhando os exercícios, séries e repetições recomendadas para cada aluno.

4. **Controle de Aulas**: Possibilidade de criar um calendário com os horários das aulas disponíveis, incluindo o tipo de aula, o instrutor responsável e o número máximo de participantes.

5. **Autenticação e Permissões**: Sistema de autenticação seguro para garantir que apenas usuários autorizados tenham acesso às funcionalidades restritas.

6. **API Pública**: Disponibilização de uma API pública para permitir integração com outros sistemas ou aplicações de terceiros.
## Configuração do Ambiente de Desenvolvimento

Para executar o projeto em um ambiente de desenvolvimento local, siga os passos abaixo:

1. **Pré-requisitos**: Certifique-se de ter instalado o Python (versão 3.8 ou superior), o Django (versão 4.2 ) e o Django Rest Framework (versão 3.14) em seu ambiente.

2. **Clone o repositório**: Faça um clone deste repositório em sua máquina local utilizando o seguinte comando:
   git clone https://github.com/jonaspeixoto/Api_Gym.git

3. **Configuração do ambiente virtual (opcional, mas recomendado)**: Crie um ambiente virtual para isolar as dependências do projeto. 

4. **Instalação das dependências**: Navegue até a pasta do projeto e instale as dependências utilizando o gerenciador de pacotes pip:

   ```
   cd gym_api
   pip install -r requirements.txt
   ```

5. **Configuração Variaveis de Abiente**: Crie  um arquivo de configuração para informações das variaveis de ambiente.
   ```
   cd gym_api
   cd gym_api
   ```

6. **Realizando as Migrações**: Execute as migrações para criar as tabelas necessárias no banco de dados:

   ```
   python manage.py migrate
   ```

7. **Criando um Superusuário**: Crie um superusuário para ter acesso ao painel administrativo do Django:

   ```
   python manage.py createsuperuser
   ```

8. **Executando o Servidor de Desenvolvimento**: Inicie o servidor de desenvolvimento do Django para testar a API:

   ```
   python manage.py runserver
   ```

## Colaboradores:






