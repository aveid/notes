from rest_framework import pagination


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'size'
    max_page_size = 10000