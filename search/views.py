from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import elastic_results, hit_Json, paginationResults

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

        response = elastic_results(search_query, indexname)

        if response:
            results = hit_Json(search_query, indexname, response, results)

    results_num = 5
    custom_range, results = paginationResults(request, results, results_num)

    context = {
        'search_query': search_query,
        'response': response,
        'results': results,
        'custom_range': custom_range,
    }
    
    return render(request, 'search/search.html', context)






