CREATE VIEW dim_cliente AS
SELECT idCliente,
nomeCliente,
cidadeCliente,
estadoCliente,
paisCliente
FROM tb_cliente tc; 

CREATE VIEW dim_vendedor AS
SELECT idVendedor,
nomeVendedor,
sexoVendedor,
estadoVendedor
FROM tb_vendedor tv;

CREATE VIEW dim_carros AS
SELECT idCarro,
classiCarro,
marcaCarro,
modeloCarro,
anoCarro,
tco.tipoCombustivel
FROM tb_carro tc 
JOIN tb_combustivel tco on tc.idCombustivel = tco.idCombustivel;

CREATE VIEW dim_tempo AS
SELECT idLocacao,
dataLocacao,
horaLocacao,
dataEntrega,
horaEntrega
FROM tb_locacao tl;

CREATE VIEW fato_locacoes AS
SELECT idLocacao,
idCliente,
idCarro,
idVendedor,
qtdDiaria as quantidadeDiaria,
vlrDiaria as valorDiaria
FROM tb_locacao tl;

SELECT * FROM fato_locacoes fl;

SELECT * FROM dim_carros dca;

SELECT * FROM dim_cliente dcl;

SELECT * FROM dim_tempo dt;

SELECT * FROM dim_vendedor dv;

