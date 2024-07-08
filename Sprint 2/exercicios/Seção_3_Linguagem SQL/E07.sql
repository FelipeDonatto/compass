select distinct autor.nome
from autor left join livro on autor.codautor = livro.autor
where (select count(*) from livro where livro.autor == autor.codautor) == 0
order by autor.nome;