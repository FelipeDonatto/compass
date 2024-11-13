import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col
from pyspark.sql.functions import explode
import datetime


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

def get_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month if len(str(datetime.datetime.now().month)) == 2 else f'0{datetime.datetime.now().month}'
    day = datetime.datetime.now().day if len(str(datetime.datetime.now().day)) == 2 else f'0{datetime.datetime.now().day}'
    return f'{year}/{month}/{day}'


json_file = "s3://felipedonattobucket/Trusted/Parquet/2024/10/09/melhores_animacoes.parquet"
df = spark.read.parquet(json_file)
df_exploded = df.withColumn("genre_id", explode(df["genre_ids"]))

movies_df = df.select("id","original_language", "original_title", "title", "overview",
                     "adult")
movie_genres_df = df_exploded.select("id", "genre_ids")
movie_votes = df.select("id", "vote_count", "vote_average", "popularity")
movie_posters = df.select("id", "backdrop_path", "poster_path")
movie_dates = df.select("id", "release_date")

genres_data = [
    (28, "Action"),
    (12, "Adventure"),
    (16, "Animation"),
    (35, "Comedy"),
    (80, "Crime"),
    (99, "Documentary"),
    (18, "Drama"),
    (10751, "Family"),
    (14, "Fantasy"),
    (36, "History"),
    (27, "Horror"),
    (10402, "Music"),
    (9648, "Mystery"),
    (10749, "Romance"),
    (878, "Science Fiction"),
    (10770, "TV Movie"),
    (53, "Thriller"),
    (10752, "War"),
    (37, "Western")
]
genres_df = spark.createDataFrame(genres_data, ["genre_id", "genre_name"])

movies_df.write.mode('overwrite').parquet(f"s3://felipedonattobucket/Refined/Parquet/{get_date()}/")
genres_df.write.mode('append').parquet(f"s3://felipedonattobucket/Refined/Parquet/{get_date()}/")
movie_genres_df.write.mode('append').parquet(f"s3://felipedonattobucket/Refined/Parquet/{get_date()}/")
movie_votes.write.mode('append').parquet(f"s3://felipedonattobucket/Refined/Parquet/{get_date()}/")
movie_posters.write.mode('append').parquet(f"s3://felipedonattobucket/Refined/Parquet/{get_date()}/")
movie_dates.write.mode('append').parquet(f"s3://felipedonattobucket/Refined/Parquet/{get_date()}/")

print("Arquivos parquet criados no bucket s3")

job.commit()
