import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as F

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH', 'S3_OUTPUT_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
source_file = args['S3_INPUT_PATH']
target_path = args['S3_OUTPUT_PATH']

df = glueContext.create_data_frame.from_options(
"s3",
{
"paths": [
source_file
]
},
"csv",
{"withHeader": True, "separator":","},
)

df.printSchema();

df = df.withColumn('nome', F.upper(df['nome']));


count = df.count();
print(f"Número de linhas: {count}")

year_and_sex = df.groupBy("ano", "sexo")
year_and_sex_sorted_count = year_and_sex.count().orderBy("ano", ascending=False);
year_and_sex_sorted_count.show(10);

female_name = df.filter(df['sexo'] == 'F').groupBy(F.col("nome"), F.col("ano")).agg(F.sum("total").alias("registros")).orderBy(F.desc("registros")).show(1);
male_name =  df.filter(df['sexo'] == 'M').groupBy(F.col("nome"), F.col("ano")).agg(F.sum("total").alias("registros")).orderBy(F.desc("registros")).show(1);

total_by_year = year_and_sex.agg(F.sum("total").alias("registros")).orderBy(F.col("ano")).limit(10).write.mode("overwrite").json(target_path);

job.commit()
