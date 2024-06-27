# rm -rf ./vendas/*
# comando utilizado para limpar o diretorio e testar

mkdir -p vendas && mkdir -p vendas/backups; #cria os diretorios checando se ja existem
date1=$(date +"-%Y%m%d"); #define a data

cp ./ecommerce/dados_de_vendas.csv ./vendas/;
cp ./vendas/dados_de_vendas.csv "./vendas/backups/dados$date1.csv";
#copia os dados
mv "./vendas/backups/dados$date1.csv" "./vendas/backups/backup-dados$date1.csv";
#renomeia o arquivo
date=$(date +"%Y/%m/%d %H:%M");
#altera novamente a data para os relatorios
echo "$date" >> ./vendas/backups/relatorio.txt
echo $(sed -n '2p' "./vendas/backups/backup-dados$date1.csv") >> ./vendas/backups/relatorio.txt
echo $(tail -n 1  "./vendas/backups/backup-dados$date1.csv") >> ./vendas/backups/relatorio.txt
echo $(tail -n +2 "./vendas/backups/backup-dados$date1.csv" | wc -l) "itens diferentes vendidos" >> ./vendas/backups/relatorio.txt
echo $(head -n 10 "./vendas/backups/backup-dados$date1.csv") >> ./vendas/backups/relatorio.txt

zip -r "./vendas/backups/backup-dados$date1.zip" "./vendas/backups/backup-dados$date1.csv" && rm -rf "./vendas/backups/backup-dados$date1.csv" && rm -rf "./vendas/dados_de_vendas.csv";
 