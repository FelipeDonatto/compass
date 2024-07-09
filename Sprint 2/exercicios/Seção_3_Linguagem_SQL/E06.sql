select distinct autor.codautor, autor.nome, (select count(*) from livro where livro.autor == autor.codautor) as quantidade_publicacoes
from autor left join livro on autor.codautor = livro.autor
order by quantidade_publicacoes desc limit 1;