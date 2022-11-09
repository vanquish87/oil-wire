from django.shortcuts import render
import requests, json

# Create your views here.
def search(request):
    search_query = ''
    response = ''
    results = []
    # extract search_query from frontend
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

        # cluster = 'ongc-delhi-prod'
        # cluster = 'ongc-deharadun-prod'
        # reqUrl = f"http://10.205.3.174:9200/{cluster}:*/_search"
        reqUrl = f"http://10.205.18.127:9200/*/_search"

        body = {
            "_source":'*',
            "query":{
                    "query_string":{
                        "query":f"*{search_query}*",
                        # "fields": ["host_ip"]
                        }
                    }
                }

        headersList = {
            "Accept": "*/*",
            "User-Agent": "Jasmeet Singh",
            "Content-Type": "application/json"
            }

        payload = json.dumps(body)
        response = requests.request("GET", reqUrl, data=payload,  headers=headersList).json()

        # creating a list of results as its complex to unpack
        # a JSON with '_' in Template Engine
        if response['hits']['hits']:
            for i in response['hits']['hits']:
                hit = {}
                hit['filename'] = i['_source']['filename']
                hit['ocrfilepath'] = i['_source']['ocrfilepath']
                results.append(hit)

        options = ('cegdis', 'epinet', 'user-upload', 'edt', 'idt')

    context = {
        'search_query': search_query,
        'response': response,
        'results': results,
    }
    return render(request, 'search/search.html', context)
