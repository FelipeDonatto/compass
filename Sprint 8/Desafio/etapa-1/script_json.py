import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import datetime

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_JSON_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
json_file = args['S3_JSON_PATH']

def get_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month if len(str(datetime.datetime.now().month)) == 2 else f'0{datetime.datetime.now().month}'
    day = datetime.datetime.now().day if len(str(datetime.datetime.now().day)) == 2 else f'0{datetime.datetime.now().day}'
    return f'{year}/{month}/{day}'

df_json = glueContext.create_data_frame.from_options(
    "s3", 
    {"paths": [json_file], "recurse": True}, 
    format="json"
)
df_json.show(15)
df_json.write.parquet(f"s3://felipedonattobucket/Trusted/Parquet/{get_date()}/")
print("Arquivos parquet criados no bucket s3")

job.commit()