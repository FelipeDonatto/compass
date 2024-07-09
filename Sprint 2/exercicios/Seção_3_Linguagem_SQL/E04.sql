select distinct autor.nome, autor.codautor, autor.nascimento, (select count(*) from livro where livro.autor == autor.codautor) as quantidade 
from autor left join livro on autor.codautor = livro.autor
order by autor.nome;