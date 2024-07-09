select distinct tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc,
(select sum(tbvendas.qtd * tbvendas.vrunt) from tbvendas where tbvendas.cdvdd == tbvendedor.cdvdd and tbvendas.status == 'Concluído') as valor_total_vendas
from tbvendedor
inner join tbvendas on tbvendas.cdvdd == tbvendedor.cdvdd
inner join tbdependente on tbvendedor.cdvdd == tbdependente.cdvdd 
order by valor_total_vendas asc limit 1;
