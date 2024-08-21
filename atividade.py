#importando as bibliotecas 

import pandas as pd
import sqlite3

# identificando de onde vem meu arquivos
atividade = sqlite3.connect('C:/Users/alice/Desktop/banco/atividade')

# criando uma varialvel cursor 
atv = atividade.cursor()

#criar tabela 
#atv.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')
# Inserindo 5 linhas 
#atv.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Caio", 28, "Direito")')
#atv.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "José", 30, "Direito")')
#atv.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Mário", 24, "Engenharia")')
#atv.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Camila", 23, "Engenharia")')
#atv.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Eduarda", 26, "Odontologia")')

#Consultas básicas

#visualizar = atv.execute('SELECT nome FROM alunos')
#visualizar = atv.execute('SELECT nome, idade FROM alunos WHERE idade > 20  and idade < 26')

#visualizar = atv.execute('SELECT * FROM alunos ORDER BY nome')
#visualizar = atv.execute('SELECT COUNT(*) FROM alunos')
#for alunos in visualizar:
#     print(alunos)

# Atualização e remoção 
#atv.execute('UPDATE alunos SET idade = 19 WHERE curso = "Odontologia"')
#atv.execute('DELETE FROM alunos WHERE id % 3 == 0')

#Criar uma Tabela e Inserir Dados
#atv.execute('CREATE TABLE clientes( id INT, idade INT, saldo FLOAT)')
#atv.execute(' INSERT INTO  clientes( id, idade, saldo) VALUES(4, 26, 450)')
#atv.execute(' INSERT INTO  clientes( id, idade, saldo) VALUES(2, 24, 150)')
#atv.execute(' INSERT INTO  clientes( id, idade, saldo) VALUES(6, 30, 1450)')
#atv.execute(' ALTER TABLE clientes ADD COLUMN nome VARCHAR(100)')
#atv.execute('UPDATE clientes SET nome = "João" WHERE id = 2')
#atv.execute('UPDATE clientes SET nome = "Maria" WHERE id = 4')
#atv.execute('UPDATE clientes SET nome = "Carlos" WHERE id = 6')

#Consultas e Funções Agregadas
#dados =atv.execute('SELECT alunos.nome, alunos.idade FROM alunos INNER JOIN clientes ON alunos.id = clientes.id WHERE alunos.idade > 29')
#for alunos in dados:
#    print(alunos)

#Saldo médio dos clientes
#resposta = atv.execute('SELECT AVG(saldo) FROM clientes')
#resposta = atv.execute('SELECT* FROM clientes ORDER BY saldo DESC')
#resposta = atv.execute('SELECT COUNT( *) FROM clientes WHERE saldo > 1000')
#for clientes in resposta:
#   print(clientes)

#Atualizando saldo 
#atv.execute('UPDATE clientes SET saldo = 1150 WHERE saldo = 150')
# Removendo cliente
#atv.execute('DELETE FROM clientes WHERE id = 2')

#Junção de Tabelas
#atv.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT,  produto VARCHAR(1000),  valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')
#atv.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(49, 2,"carro",45000)')
#atv.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(77, 4,"moto",15000)')

#Consulta
consulta = atv.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
for cliente in consulta:
    print(consulta)

#Commitando e fechando
atividade.commit()
atividade.close
