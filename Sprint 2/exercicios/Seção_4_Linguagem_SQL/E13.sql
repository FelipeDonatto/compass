select cdpro, nmc as nmcanalvendas, nmp as nmpro,
(select sum(qtd) from tbvendas 
where status == 'Concluído' 
and tbvendas.cdpro == cdpro
and tbvendas.nmpro == nmp 
and tbvendas.nmcanalvendas == nmc) as quantidade_vendas
from (select distinct cdpro, nmcanalvendas as nmc, nmpro as nmp
from tbvendas
where status == 'Concluído'
group by cdpro, nmcanalvendas
order by qtd) 
order by quantidade_vendas
