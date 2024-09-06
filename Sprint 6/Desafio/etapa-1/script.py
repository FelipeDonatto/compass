import logging
import boto3
from botocore.exceptions import ClientError
import os
import datetime

# função simples para obter a data atual e facilitar a inserção no nome dos arquivos
def get_date():
    year = datetime.datetime.now().year
    #verifica se o número de mês tem 2 digitos, se não, adiciona 0 na frente
    month = datetime.datetime.now().month if len(str(datetime.datetime.now().month)) == 2 else f'0{datetime.datetime.now().month}'
    #verifica se o número de dia tem 2 digitos, se não, adiciona 0 na frente
    day = datetime.datetime.now().day if len(str(datetime.datetime.now().day)) == 2 else f'0{datetime.datetime.now().day}'
    return f'{year}/{month}/{day}'

# template para upload de arquivos da documentação do boto3
# usando variaveis de ambiente inseridas no docker para acessar o AWS
def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.environ.get('AWS_SESSION_TOKEN'),
)

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(f"{file_name} uploaded to {bucket}")
    except ClientError as e:
        logging.error(e)
        return False
    return True


upload_file('./dados/movies.csv', 'felipedonattobucket', f'Raw/Local/CSV/Movies/{get_date()}/movies.csv')
upload_file('./dados/series.csv', 'felipedonattobucket', f'Raw/Local/CSV/Series/{get_date()}/series.csv')