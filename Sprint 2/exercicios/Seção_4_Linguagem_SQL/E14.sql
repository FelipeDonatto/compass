select estado, round(a/cast(b as real),2) as gastomedio from (select sum(qtd*vrunt) as a, count(qtd) as b, estado 
from tbvendas 
where status == 'Concluído'  
group by estado)
order by gastomedio desc;