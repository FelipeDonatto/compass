CREATE TABLE tb_cliente(
	idCliente INT NOT NULL,  
  	nomeCliente VARCHAR(255),
  	cidadeCliente VARCHAR(255),
  	estadoCliente VARCHAR(255),
  	paisCliente VARCHAR(255),
  	PRIMARY KEY(idCliente)
);

INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao tl ORDER BY idCliente; 

ALTER TABLE tb_locacao DROP COLUMN nomeCliente;
ALTER TABLE tb_locacao DROP COLUMN cidadeCliente;
ALTER TABLE tb_locacao DROP COLUMN estadoCliente;
ALTER TABLE tb_locacao DROP COLUMN paisCliente;

CREATE TABLE tb_combustivel(
	idCombustivel INT NOT NULL,  
  	tipoCombustivel VARCHAR(255),
  	PRIMARY KEY(idCombustivel)
);

INSERT INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao tl ORDER BY idCombustivel; 

ALTER TABLE tb_locacao DROP COLUMN tipoCombustivel;

CREATE TABLE tb_carro(
	idCarro INT NOT NULL,  
  	classiCarro VARCHAR(255),
  	marcaCarro VARCHAR(255),
  	modeloCarro VARCHAR(255),
  	anoCarro INT,
  	idCombustivel INT,
  	PRIMARY KEY(idCarro),
    FOREIGN KEY(idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);

INSERT INTO tb_carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel 
FROM tb_locacao tl ORDER BY idCarro; 

ALTER TABLE tb_locacao DROP COLUMN classiCarro;
ALTER TABLE tb_locacao DROP COLUMN marcaCarro;
ALTER TABLE tb_locacao DROP COLUMN modeloCarro;
ALTER TABLE tb_locacao DROP COLUMN anoCarro;
ALTER TABLE tb_locacao DROP COLUMN idCombustivel;

CREATE TABLE tb_vendedor(
	idVendedor INT NOT NULL,  
  	nomeVendedor VARCHAR(255),
  	sexoVendedor INT,
  	estadoVendedor VARCHAR(255),
  	PRIMARY KEY(idVendedor)
);

INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao tl ORDER BY idVendedor;

ALTER TABLE tb_locacao DROP COLUMN nomeVendedor;
ALTER TABLE tb_locacao DROP COLUMN sexoVendedor;
ALTER TABLE tb_locacao DROP COLUMN estadoVendedor;

CREATE TEMPORARY TABLE temp AS
SELECT 
    *
FROM tb_locacao;

DROP TABLE tb_locacao;

CREATE TABLE tb_locacao (
    idLocacao INTEGER PRIMARY KEY, 
    idCliente INTEGER, 
    idCarro INTEGER,
    kmCarro INTEGER, 
    dataLocacao DATETIME, 
    horaLocacao TIME,
    qtdDiaria INTEGER, 
    vlrDiaria DECIMAL,
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INTEGER,
    FOREIGN KEY(idCliente) REFERENCES tb_cliente(idCliente),
    FOREIGN KEY(idCarro) REFERENCES tb_carro(idCarro),
    FOREIGN KEY(idVendedor) REFERENCES tb_vendedor(idVendedor)
    );

INSERT INTO tb_locacao(
idLocacao,
idCliente,
idCarro,
kmCarro,
dataLocacao,
horaLocacao,
qtdDiaria,
vlrDiaria,
dataEntrega,
horaEntrega,
idVendedor
) SELECT 
	idLocacao,
	idCliente,
	idCarro,
	kmCarro,
	dataLocacao,
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega,
	horaEntrega,
	idVendedor
FROM temp;

DROP TABLE temp;
