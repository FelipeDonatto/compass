select estado, nmpro, round(qtd/cast(sales as real),4) as quantidade_media from (select sum(qtd) as qtd, count(qtd) as sales, nmpro, estado 
from tbvendas 
where status == 'Concluído'  
group by estado, nmpro);