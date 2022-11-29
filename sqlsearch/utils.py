import requests
import pymssql, itertools
import pandas as pd
from django.conf import settings


# getting column names via ES
def column_names(table_name):
    reqUrl = 'http://10.205.18.127:9200/mssql_mother_database/_search'
    response = requests.request("GET", reqUrl).json()

    if response['hits']['hits']:
        for i in response['hits']['hits']:
            hit = {}
            if i['_source']['table_name'] == 'EPINET_GTO_NOB_AQC' and table_name == 'EPINET_GTO_NOB_AQC':

                hit['table_name'] = i['_source']['table_name']
                hit['Key_1'] = i['_source']['DATA_TYPE'][0]['Key_1'].split(':')[2]
                hit['Key_2'] = i['_source']['DATA_TYPE'][0]['Key_2'].split(':')[2]
                hit['Key_3'] = i['_source']['DATA_TYPE'][0]['Key_3'].split(':')[2]
                hit['Key_4'] = i['_source']['DATA_TYPE'][0]['Key_4'].split(':')[2]
                hit['Key_5'] = i['_source']['DATA_TYPE'][0]['Key_5'].split(':')[2]
                hit['Key_6'] = i['_source']['DATA_TYPE'][0]['Key_6'].split(':')[2]
                hit['Key_7'] = i['_source']['DATA_TYPE'][0]['Key_7'].split(':')[2]
                hit['Key_8'] = i['_source']['DATA_TYPE'][0]['Key_8'].split(':')[2]
                hit['Key_9'] = i['_source']['DATA_TYPE'][0]['Key_9'].split(':')[2]
                hit['Key_10'] = i['_source']['DATA_TYPE'][0]['Key_10'].split(':')[2]
                hit['Key_11'] = i['_source']['DATA_TYPE'][0]['Key_11'].split(':')[2]
                hit['Key_12'] = i['_source']['DATA_TYPE'][0]['Key_12'].split(':')[2]
                
            else:
                hit['table_name'] = i['_source']['table_name']
                hit['Key_1'] = i['_source']['DATA_TYPE'][0]['Key_1'].split(':')[2]
                hit['Key_2'] = i['_source']['DATA_TYPE'][0]['Key_2'].split(':')[2]
                hit['Key_3'] = i['_source']['DATA_TYPE'][0]['Key_3'].split(':')[2]
                hit['Key_4'] = i['_source']['DATA_TYPE'][0]['Key_4'].split(':')[2]
                hit['Key_5'] = i['_source']['DATA_TYPE'][0]['Key_5'].split(':')[2]
                hit['Key_6'] = i['_source']['DATA_TYPE'][0]['Key_6'].split(':')[2]
                hit['Key_7'] = i['_source']['DATA_TYPE'][0]['Key_7'].split(':')[2]
                hit['Key_8'] = i['_source']['DATA_TYPE'][0]['Key_8'].split(':')[2]
                hit['Key_9'] = i['_source']['DATA_TYPE'][0]['Key_9'].split(':')[2]
    return hit


# getting column rows for normal condition
def column_rows(table_name, search_query):
    conn = pymssql.connect("10.205.18.137:1433", "sas", "Ongc2022", "Mother_Database")
    try:
        with conn.cursor() as cur:
            query1 = f"select * from Mother_Database.dbo.{table_name} WHERE UWI_1 like '%{search_query}%';"

            cur.execute(query1)
            rows = cur.fetchall()
    finally:
        conn.close()

    return rows


# getting column rows for other condition
def column_rows_other(table_name, search_query):

    conn = pymssql.connect("10.205.18.137:1433", "sas", "Ongc2022", "Mother_Database")

    cursor = conn.cursor()
    query1=f"select * from Mother_Database.dbo.{table_name};"

    cursor.execute(query1)
    x = pd.read_sql(query1, conn)
    x = pd.DataFrame(x).astype(str)
    
    x.replace(['NaN','nan','None','none'],'-', inplace = True)

    #print(sub_string)
    search_query=search_query.lower()
    mask = x.applymap(lambda x: search_query in x.lower() if isinstance(x,str) else False).to_numpy()
    y=x.loc[mask]
    

    if len(x.loc[mask]) == 0:
        s=search_query.split(" ")
        for i in s:
            substring=i.lower()
            mask = x.applymap(lambda x: substring in x.lower() if isinstance(x,str) else False).to_numpy()
            y=y.append(x.loc[mask],ignore_index=True)

            
    # username_ds_or_nob.csv in location via settings.py
    file_name = str(settings.SAS_CSV) + '\\' + 'jimmy' + '_' + table_name.split('_')[2] + '.csv'

    y.to_csv(file_name, index=False)
    
    y = y.transpose()

    rows = y.to_dict()
    # pprint(rows)
    rows = dict(itertools.islice(rows.items(), 0 ,20))

    return rows