from django.shortcuts import render
import requests, json

# Create your views here.
def search(request):
    search_query = ''
    response = ''
    # extract search_query from frontend
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

        cluster = 'cluster_one'
        reqUrl = f"http://10.205.18.127:9200/{cluster}:*/_search"

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

    context = {
        'search_query': search_query,
        'response': response
    }
    return render(request, 'search/search.html', context)