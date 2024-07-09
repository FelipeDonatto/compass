select vendedor, valor_total_vendas, round((rate * valor_total_vendas)/100, 2) as comissao from (select distinct tbvendedor.nmvdd as vendedor,
(select sum(tbvendas.qtd * tbvendas.vrunt) from tbvendas where tbvendas.cdvdd == tbvendedor.cdvdd and tbvendas.status == 'Concluído') as valor_total_vendas,
tbvendedor.perccomissao as rate
from tbvendedor
inner join tbvendas on tbvendas.cdvdd == tbvendedor.cdvdd)
order by comissao desc;
