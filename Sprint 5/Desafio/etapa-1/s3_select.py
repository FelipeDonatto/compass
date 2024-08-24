import boto3


client = boto3.client('s3')

AWS_ACCESS_KEY_ID="ASIAQEIP27Z5NHSNRJYC"
AWS_SECRET_ACCESS_KEY="QLw3rrCPdAsz2kR1JrpfeCtgSIxPdu7vU/WEDKLw"
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjELT//////////wEaCXVzLWVhc3QtMSJIMEYCIQDkxLzn6mGtBLTzhNk4ObOyU0ocGgxcWnunZrmsJuh5dgIhAN7CQkAOsJ/vLfqmjRngog74rdqsgjEMqPYDAqPnWvwIKqoDCLz//////////wEQABoMMDA5MTYwMDMxODY2Igz6Ofbx8wD8iq69mOEq/gL30sbILWc8S8Tq3xU9/yzYgnJpduBQVTpPH1x4Uw+dLgHRoUD/eYS7m0GE1nBThcelFajd95sOuAS9QnJmCikJa/dwx+oXYE2736GtvvckdcC87l3IkJMC3moO9x4hXUWPjga2v8z/b6bH1SYXRGcUHoVZ2bfwQ9YApCeSACWMNQqIrRuMz7d6dtqkxmrdQliV8yR3anSYjj98LcJnTRQCEMROyOkapegeKa2dN5cq0EEBXDQdWRdjmIyFYozJvGx4K0V/oBmyMqqgyxD8fyz1fwIawKpz5C/k1t5cU2+KMDm6UsNs328U7AFgUqXCSqwMxbCyjO8BXr/XR31kZ+scAQT0V4qLMZKi/bM0JcOcO4WQwNcHK9VftstDTmnAp6axL/Sld7DI+tGWvlA7t5eUfiDonPGaA/B7yH0nd9ywzBgwLFzU1/wvj3bpV6isD5A59AjDUQJHQmlkK2aWOO0jH6Wk66dtnNrPCVYrYiTeD6oPJqIVEpJsgLnW6jphMJ//prYGOqUBXJnTi/WSzTqLUAC0CGt4G0LvKhGN9d9++CU7Ff12kSHVE2IjErmT+7NcusbrrwBrmzuY5UQSvesrZNTfqQc0qJzWrEux29s9EOz8t5f6W9zLOGfjcGYomDbBAw6L+EQ/aIrIw9IbXSJJOMRv+0KJRUZe9xGCLCkwNMrCnNXpVd6hmqZtIXRvYPxwA+R7SGRDWzX1SkujeoQE8xowAjDlrd+vYXdP"








client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN
)

resp = client.select_object_content(
    Bucket='felipedonattobucket', 
    Key='transferencias_voluntarias_dpda_31mai23.csv', 
    Expression="select s._1 as NroInstrumento, s._4 as ValorDoInstrumento, (CASE s._11 WHEN 'Em execução' THEN 'Sendo executado' ELSE 'Planejamento' END) as Situcao, EXTRACT(YEAR FROM TO_TIMESTAMP(s._12)) as AnoDeInicio, s._8 as NomeProponente, UPPER(s._7) as Objetivo from s3object s WHERE s._12 BETWEEN '2023-01-01' AND '2024-01-01' and s._9 is not NULL;",
    ExpressionType='SQL',
    InputSerialization={
        "CSV": {
            'FileHeaderInfo': 'NONE',
            'FieldDelimiter': ';',
        },
    },
    OutputSerialization={
        'CSV': {}
    },
)

file = open('./transferencias_voluntarias.csv', 'w',encoding='UTF-8')
print("Arquivo 'transferencias_voluntarias.csv' criado com sucesso!")
file.truncate(0)
file.write("NroInstrumento;ValorDoInstrumento;Situcao;AnoDeInicio;NomeProponente;Objetivo\n")
for event in resp['Payload']:
    if 'Records' in event:
        fileContent = str((event['Records']['Payload'].decode('utf-8-sig')))
        file.write(fileContent)

resp2 = client.select_object_content(
    Bucket='felipedonattobucket', 
    Key='transferencias_voluntarias_dpda_31mai23.csv', 
    # Expression="select max(cast(s._4 as float)) as valorMaximo, min(cast(s._4 as float)) as valorMinimo from s3object s where s._4 is not null",
    # não funciona com o cast, erro de conversão.
    # o s3 select converte tudo para string e depois não consegue converter para float
    # por isso, precisei fazer 2 counts para as funções de agregação, uma vez que elas não funcionam com strings.
    Expression="SELECT count(s._9) as SaoPaulo FROM s3object s WHERE s._9 = 'SP'",
    ExpressionType='SQL',
    InputSerialization={
        "CSV": {
            'FileHeaderInfo': 'NONE',
            'FieldDelimiter': ';',
        },
    },
    OutputSerialization={
        'CSV': {}
    },
)

file = open('./transferencias_voluntarias_count_1.csv', 'w',encoding='UTF-8')
print("Arquivo 'transferencias_voluntarias_count_1.csv' criado com sucesso!")
file.truncate(0)
file.write("São Paulo\n")

for event in resp2['Payload']:
    if 'Records' in event:
        fileContent = str((event['Records']['Payload'].decode('utf-8-sig')))
        file.write(fileContent)

resp3 = client.select_object_content(
    Bucket='felipedonattobucket', 
    Key='transferencias_voluntarias_dpda_31mai23.csv', 
    Expression="SELECT count(s._9) as SaoPaulo FROM s3object s WHERE s._9 = 'RS'",
    ExpressionType='SQL',
    InputSerialization={
        "CSV": {
            'FileHeaderInfo': 'NONE',
            'FieldDelimiter': ';',
        },
    },
    OutputSerialization={
        'CSV': {}
    },
)

file = open('./transferencias_voluntarias_count_2.csv', 'w',encoding='UTF-8')
print("Arquivo 'transferencias_voluntarias_count_2.csv' criado com sucesso!")
file.truncate(0)
file.write("Rio Grande do Sul\n")
for event in resp3['Payload']:
    if 'Records' in event:
        fileContent = str((event['Records']['Payload'].decode('utf-8-sig')))
        file.write(fileContent)

