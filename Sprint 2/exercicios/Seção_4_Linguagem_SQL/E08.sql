select cdvdd, nmvdd from (
select distinct tbvendedor.cdvdd, tbvendedor.nmvdd, (select count(*) from tbvendas where tbvendedor.cdvdd == tbvendas.cdvdd) as vendas
from tbvendedor 
inner join tbvendas on tbvendedor.cdvdd == tbvendas.cdvdd
limit 1);