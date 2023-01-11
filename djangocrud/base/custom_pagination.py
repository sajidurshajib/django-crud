from rest_framework import pagination


class CustomNamePagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'limit'
    max_page_size = 20
    page_query_param = 'page'
