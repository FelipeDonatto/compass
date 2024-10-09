from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark import SparkContext, SQLContext
import random 


spark = SparkSession \
                .builder \
                .master ("local[*]") \
                .appName("Exercicio Intro") \
                .getOrCreate()
                
df_nomes = spark.read.format("csv").load("./nomes_aleatorios.txt")

df_nomes.show(5)
df_nomes.printSchema()

df_nomes = df_nomes.withColumnRenamed("_c0", "nome")
df_nomes.printSchema()
df_nomes.show(10)

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    F.expr("CASE WHEN rand() < 0.33 THEN 'Fundamental' WHEN rand() < 0.66 THEN 'Médio' ELSE 'Superior' END")
)


df_nomes = df_nomes.withColumn(
    "Pais",
    F.expr(
        f"""
        CASE
            WHEN rand() < 1/13 THEN 'Argentina'
            WHEN rand() < 2/13 THEN 'Bolívia'
            WHEN rand() < 3/13 THEN 'Brasil'
            WHEN rand() < 4/13 THEN 'Chile'
            WHEN rand() < 5/13 THEN 'Colômbia'
            WHEN rand() < 6/13 THEN 'Equador'
            WHEN rand() < 7/13 THEN 'Guiana'
            WHEN rand() < 8/13 THEN 'Paraguai'
            WHEN rand() < 9/13 THEN 'Peru'
            WHEN rand() < 10/13 THEN 'Suriname'
            WHEN rand() < 11/13 THEN 'Uruguai'
            WHEN rand() < 12/13 THEN 'Venezuela'
            ELSE 'Guiana Francesa'
        END
        """
    )
)
df_nomes.show(5)
df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (F.floor(F.rand() * (2010 - 1945 + 1)) + 1945).cast("int")
)
df_nomes.show(5)

seculo_21 = df_nomes.select("Nome", "AnoNascimento").where(F.col("AnoNascimento") >= 2000)
seculo_21.show(10)

df_nomes.createOrReplaceTempView("pessoas")
spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000").show(10)


df_millennials = df_nomes.select("Nome", "AnoNascimento").where((F.col("AnoNascimento") >= 1980) & (F.col("AnoNascimento") <= 1994))
millennials_count = df_millennials.count()

spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994").show(1)


df_geracoes = spark.sql("""
    SELECT
        Pais,
        CASE
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
""")

df_geracoes.show()