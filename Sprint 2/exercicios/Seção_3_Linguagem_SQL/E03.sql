select distinct (select count(editora) from livro where livro.editora == editora.codeditora) as quantidade, editora.nome, endereco.estado, endereco.cidade from livro 
inner join editora on editora.codeditora = livro.editora 
inner join endereco on editora.endereco = endereco.codendereco;