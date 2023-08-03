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

1. **Pré-requisitos**: Certifique-se de ter instalado o Docker (versão 20.10 ou superior), o Django (versão 4.2 ) e o Docker compose (versão v2.15 ou superior) em seu ambiente.

2. **Clone o repositório**: Faça um clone deste repositório em sua máquina local utilizando o seguinte comando e em seguida vá para o diretório de trabalho:
   ```
   git clone https://github.com/jonaspeixoto/Api_Gym.git
   ```
   ```
   cd Apy_Gym
   ```

3. **Criação de serviço docker**: Crie uma imagem docker para o servidor de desenvolvimento utilizando docker compose:
   ```
   docker-compose build
   ```
4. **Inicialização do servidor de desenvolvimento**: Inicialize o servidor de desenvolvimento utilizando o docker compose:

   ```
   docker-compose up
   ```
   Isso fará o docker-compose executar para você, na inicialização do container docker, os seguintes comandos:
   ```
   python manage.py wait_for_db
   python manage.py migrate
   python manage.py runserver 0.0.0.0:8000
   ```

5. **Abrindo aplicação no browser**: Com o servidor executando, em um browser de sua preferência, vá para o seguinte link:
   ```
   http://127.0.0.1:8000/
   ```
   ou
   ```
   http://localhost:8000/
   ```

6. **Execução de comandos shell no container docker**: Execute, durante o desenvolvimento, comandos shell no container docker utilizando a seguinte sintaxe (substituindo o comando entre aspas abaixo pelo comando desejado):
   ```
   docker-compose run --rm gym_api sh -c "python manage.py test"
   ```

## Colaboradores:

Eduardo Soares - [Github]() - [LinkedIn]() - email@example.com

Jonas Peixoto - [Github]() - [LinkedIn]() - email@example.com

Vinícius Oliveira - [Github](https://github.com/vinicoli) - [LinkedIn](https://www.linkedin.com/in/vinicoli) - vinioliveira.web@gmail.com