- Estudar SQL Alchemy framework
- Modelar o que pensou em termos de atributos e importamentos com base no funcionamento do SQL Alchemy
- Mínimo 3 entidades no banco de dados
- 7 Funcionalidades

Tema: Sistema de Reserva de Imóveis

## Entidades Principais:

1. Propriedade: Representa um imóvel disponível para reserva, com atributos como endereço, tipo de imóvel (casa, apartamento, etc.), número de quartos, preço da diária, etc.

2. Proprietário: Representa o proprietário do imóvel, com atributos como nome, contato, endereço, etc.
3. Reserva: Representa uma reserva de um imóvel, com atributos como data de check-in, data de check-out, propriedade reservada, cliente que fez a reserva, etc.

## Funcionalidades do Sistema:

1. Cadastro de Propriedades e Proprietários: Os usuários podem cadastrar novas propriedades e seus respectivos proprietários.

2. Consulta de Propriedades e Proprietários: Os usuários podem consultar informações sobre as propriedades disponíveis e os proprietários cadastrados.

3. Realização de Reservas: Os usuários podem reservar imóveis para estadias futuras.

4. Consulta de Reservas: Os usuários podem verificar as reservas feitas e suas datas de check-in e check-out.

5. Cancelamento de Reservas: Os usuários podem cancelar suas reservas, liberando o imóvel para outros clientes.

6. Alteração de Reservas: Os usuários podem alterar as datas de check-in e check-out de suas reservas, se necessário.

7. Disponibilidade de Propriedades: Os usuários podem verificar a disponibilidade de uma propriedade em determinadas datas.

## Aspectos Importantes do Projeto:

1. Relacionamentos entre Entidades: Utilize os recursos de relacionamentos para modelar a relação entre propriedades, proprietários e reservas.

2. Operações CRUD: Implemente operações básicas para criar, ler, atualizar e excluir propriedades, proprietários e reservas.

3. Tratamento de Exceções: Implemente tratamento de exceções para lidar com situações como tentativa de reserva de um imóvel já reservado, cadastro de um proprietário já existente, etc.

4. Interface de Usuário (UI): Desenvolva uma interface de usuário simples para interação com o sistema, permitindo aos usuários realizar todas as funcionalidades mencionadas de forma intuitiva.
