import json
import requests
import logging
import boto3
import os
from botocore.exceptions import ClientError
import datetime

api_key = 'xxxx'
s3_client = boto3.client(
    's3',
    aws_access_key_id="xxxx",
    aws_secret_access_key="xxxx",
    aws_session_token="xxxx"
)
url = 'https://api.themoviedb.org/3/discover/movie'
bucket_name = "felipedonattobucket"
file_name = 'melhores_animacoes.json'
params = {
    'api_key': api_key,
    'sort_by': 'vote_average.desc', 
    'with_genres': '16', 
    'vote_count.gte': 1000, 
    'language': 'pt-BR', 
    'page': 1  
}

def get_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month if len(str(datetime.datetime.now().month)) == 2 else f'0{datetime.datetime.now().month}'
    day = datetime.datetime.now().day if len(str(datetime.datetime.now().day)) == 2 else f'0{datetime.datetime.now().day}'
    return f'{year}/{month}/{day}'
    
def get_top_rated_animations(api_key, num_results=100):
    results = []
    page = 1

    while len(results) < num_results:
        params['page'] = page
        response = requests.get(url, params=params)
        data = response.json()

        if 'results' in data:
            results.extend(data['results'])
        else:
            print("Erro ao buscar dados:", data)
            break

        if page >= data['total_pages']: 
            break

        page += 1

    return results[:num_results]

def lambda_handler(event, context):
    top_animations = get_top_rated_animations(api_key, num_results=100)
    json_data = json.dumps(top_animations, ensure_ascii=False, indent=4)

    try:
        response = s3_client.put_object(Body=json_data, Bucket=bucket_name, Key=f'Raw/TMDB/JSON/{get_date()}/melhores_animacoes.json', ContentType='application/json')
    except ClientError as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Erro ao salvar arquivo no S3.')
        }
    return True
