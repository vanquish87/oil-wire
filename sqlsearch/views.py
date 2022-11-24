from django.shortcuts import render
from .utils import column_names, column_rows_other, column_rows


# Create your views here.
def sql_search_dp(request, search_query):
    table_name = 'EPINET_GTO_DP_AQC'
    rows = column_rows(table_name, search_query)

    # getting column names via ES
    hit = column_names(table_name)

    context = {
        'rows': rows,
        'hit': hit,
    }
    return render(request, 'sqlsearch/search-dp.html', context)


def sql_search_nob(request, search_query):
    table_name = 'EPINET_GTO_NOB_AQC'
    rows = column_rows(table_name, search_query)

    # getting column names via ES
    hit = column_names(table_name)

    context = {
        'rows': rows,
        'hit': hit,
    }    
    return render(request, 'sqlsearch/search-dp.html', context)


def sql_search_dp_other(request, search_query):
    table_name = 'EPINET_GTO_DP_AQC'    
    rows = column_rows_other(table_name, search_query)
    # getting column names via ES
    hit = column_names(table_name)

    context = {
        'rows': rows,
        'hit': hit,
    }
    return render(request, 'sqlsearch/search-dp-other.html', context)



def sql_search_nob_other(request, search_query):
    table_name = 'EPINET_GTO_NOB_AQC'
    rows = column_rows_other(table_name, search_query)
    # getting column names via ES
    hit = column_names(table_name)

    context = {
        'rows': rows,
        'hit': hit,
    }    
    return render(request, 'sqlsearch/search-dp-other.html', context)
