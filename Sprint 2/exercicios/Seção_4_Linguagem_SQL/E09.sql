select cdpro, nmpro from (select distinct cdpro, nmpro, count(cdpro)
from tbvendas 
where dtven >= "2014-02-93" 
and dtven <= "2018-02-02" 
and status == "Concluído"
group by cdpro
limit 1);