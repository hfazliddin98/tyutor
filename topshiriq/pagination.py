from rest_framework.pagination import PageNumberPagination


class TopshiriqPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'qiymat'
    max_page_size = 100