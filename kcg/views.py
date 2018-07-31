from rest_framework import viewsets
from kcg.models import Triple
from kcg.serializers import TripleSerializer
from rest_framework.pagination import PageNumberPagination


class KcgViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class KcgViewSet(viewsets.ModelViewSet):
    """
    List all KCG triples.
    Provides `list` and `detail` actions.
    """
    # queryset = Triple.objects.all()
    serializer_class = TripleSerializer
    pagination_class = KcgViewSetPagination
    queryset = Triple.objects.all()

    def get_queryset_with_query_params(self, queryset, request):
        criteria = {}
        params = request.GET
        for field in ['sbj', 'rel', 'obj']:
            if field in params:
                criteria[f'{field}__name__iexact'] = params[field]
        for field in ['sbj_id', 'rel_id', 'obj_id']:
            if field in params:
                criteria[f'{field}__id__iexact'] = params[field]
        # filter
        if criteria:
            queryset = queryset.filter(**criteria)
        else:
            queryset = queryset.all()
        # order by relation confidence score
        queryset = queryset.order_by('-confidence')

        return queryset

    def get_queryset(self):
        queryset = self.get_queryset_with_query_params(self.queryset, self.request)
        return queryset
