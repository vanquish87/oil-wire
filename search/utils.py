from elasticsearch import Elasticsearch
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def elastic_results(search_query, indexname):
    es = Elasticsearch("http://10.205.18.127:9200")

    search_query = search_query.replace(':', ':\\')

    try:
        get_data_query = {"query": {
                        "query_string": 
                            {
                            "query": f'{search_query}',
                            "default_operator": "OR"
                            }
                        }}
        response = es.search(index=indexname, body=get_data_query)

    except:
        response = {}

    return response
    


# creating a list of results as its complex to unpack
# a JSON with '_' in Template Engine
def hit_Json(search_query, indexname, response, results):
    for i in response['hits']['hits']:
        hit = {}
        if indexname == 'ocredpdf':
            hit['filename'] = i['_source']['filename']
            hit['ocr_url'] = 'http://' + i['_source']['ip'] + ':9000' + '/ocrfiles/view-pdf/' + i['_source']['sourcefilepath'] + '\\' + i['_source']['filename']

            full_text = i['_source']['attachment']['content'].lower()
            hit['snippet'] = snippet(search_query, full_text, hit)
                
        elif indexname == 'idttest':
            hit['filename'] = i['_source']['pdfdetails']['filename']
            hit['ocr_url'] = i['_source']['url']

            full_text = i['_source']['pdfdetails']['attachment']['content'].lower()
            hit['snippet'] = snippet(search_query, full_text, hit)
        
        elif indexname == 'mssql-well_list':
            hit['name'] = i['_source']['name']
        
        results.append(hit)

    return results


# creating snippet containing search_query
def snippet(search_query, full_text, hit):
    query_location = None
    if search_query in full_text:
        query_location = full_text.index(search_query)
    else:
        # adjusting for space conditions
        search_query_list = search_query.split(' ')
        for search_query in search_query_list:
            if search_query in full_text:
                query_location = full_text.index(search_query)
                if query_location:
                    break
    try:
        hit['snippet'] = full_text[query_location:query_location+150]
    except:
        hit['snippet'] = None
    
    return hit['snippet']



def paginationResults(request, results, results_num):
    page = request.GET.get('page')
    paginator = Paginator(results, results_num)

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        results = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        results = paginator.page(page)

    # if we have lots of pages but don't want to show all the buttons in paginator
    leftIndex = (int(page) - 2)
    # nearing initial pages
    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 2)
    # for nearing last pages
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, results