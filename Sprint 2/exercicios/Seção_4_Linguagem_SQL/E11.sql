select distinct cdcli, nmcli, sum(tbvendas.vrunt * tbvendas.qtd) as gasto
from tbvendas 
where status == "Concluído"
group by tbvendas.cdcli
order by gasto desc limit 1;