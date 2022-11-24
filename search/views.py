from django.shortcuts import render
import requests, json
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def search(request):
    search_query = ''
    response = ''
    results = []
    # extract search_query from frontend
    if request.GET.get('search_query') and request.GET.get('indexname'):
        search_query = request.GET.get('search_query')
        indexname=request.GET.get('indexname')

        reqUrl = f'http://10.205.18.127:9200/{indexname}/_search?q="{search_query}"'

        response = requests.request("GET", reqUrl).json()

        # creating a list of results as its complex to unpack
        # a JSON with '_' in Template Engine
        if response['hits']['hits']:
            for i in response['hits']['hits']:

                hit = {}
                if indexname == 'ocredpdf':
                    hit['filename'] = i['_source']['filename']
                    hit['ocr_url'] = 'http://' + i['_source']['ip'] + ':9000' + '/ocrfiles/view-pdf/' + i['_source']['sourcefilepath'] + '\\' + i['_source']['filename']

                    # creating snippet containing search_query
                    full_text = i['_source']['attachment']['content'].lower()
                    if search_query in full_text:
                        query_location = full_text.index(search_query)
                    try:
                        hit['snippet'] = full_text[query_location:query_location+150]
                    except:
                        hit['snippet'] = None
                        
                elif indexname == 'idttest':
                    hit['filename'] = i['_source']['pdfdetails']['filename']
                    hit['ocr_url'] = i['_source']['url']

                    # creating snippet containing search_query
                    full_text = i['_source']['pdfdetails']['attachment']['content'].lower()
                    if search_query in full_text:
                        query_location = full_text.index(search_query)
                    try:
                        hit['snippet'] = full_text[query_location:query_location+150]
                    except:
                        hit['snippet'] = None

                
                elif indexname == 'mssql-well_list':
                    hit['name'] = i['_source']['name']

                results.append(hit)

        options = ('cegdis', 'epinet', 'user-upload', 'edt', 'idt')

    context = {
        'search_query': search_query,
        'response': response,
        'results': results,
    }
    return render(request, 'search/search.html', context)


