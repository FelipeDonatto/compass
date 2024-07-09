select DISTINCT autor.nome from livro
inner join editora on editora.codeditora == livro.editora 
inner join endereco on endereco.codendereco == editora.endereco
inner join autor on autor.codautor == livro.autor 
where endereco.estado != "RIO GRANDE DO SUL" and endereco.estado != "PARANÁ"
order by autor.nome;