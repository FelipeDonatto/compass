import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col
import datetime

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_SHOWS','S3_INPUT_PATH_MOVIES', 'S3_INPUT_PATH_TMDB'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
movies_file = args['S3_INPUT_PATH_MOVIES']
shows_file = args['S3_INPUT_PATH_SHOWS']
tmdb_file = args['S3_INPUT_PATH_TMDB']

def get_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month if len(str(datetime.datetime.now().month)) == 2 else f'0{datetime.datetime.now().month}'
    day = datetime.datetime.now().day if len(str(datetime.datetime.now().day)) == 2 else f'0{datetime.datetime.now().day}'
    return f'{year}/{month}/{day}'

df_movies = glueContext.create_data_frame.from_options("s3",{"paths": [movies_file]},"csv",{"withHeader": True, "separator":"|"},)
df_movies_filtrado = df_movies.filter(col("genero").contains("Animation"))
df_movies_filtrado = df_movies_filtrado.filter(col("numeroVotos") >= 1000)
df_movies_final = df_movies_filtrado.drop("generoArtista", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos")
df_movies_unicos = df_movies_final.dropDuplicates(["tituloPincipal", "anoLancamento"])
df_movies_unicos.show(15)

df_shows = glueContext.create_data_frame.from_options("s3",{"paths": [shows_file]},"csv",{"withHeader": True, "separator":"|"},)
df_shows_filtrado = df_shows.filter(col("genero").contains("Animation"))
df_shows_filtrado = df_shows_filtrado.filter(col("numeroVotos") >= 1000)
df_shows_final = df_shows_filtrado.drop("generoArtista", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos")
df_shows_unicos = df_shows_final.dropDuplicates(["tituloPincipal", "anoLancamento"])
df_shows_unicos.show(15)

df_movies_unicos.write.mode('append').parquet(f"s3://felipedonattobucket/Trusted/Parquet/{get_date()}/")
df_shows_unicos.write.mode('append').parquet(f"s3://felipedonattobucket/Trusted/Parquet/{get_date()}/")
print("Arquivos parquet criados no bucket s3")


job.commit()