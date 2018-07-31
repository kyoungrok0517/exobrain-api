from rest_framework import viewsets
from kcg.models import Triple
from kcg.serializers import TripleSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
import ujson as json

@csrf_exempt
def triple_list(request):
    """
    List all KCG triples.
    """
    def get_triples_with_criteria(request, criteria):
        _filter = {}
        for field in ['sbj', 'rel', 'obj']:
            if field in criteria:
                _filter[f'{field}__name__iexact'] = criteria[field]
        for field in ['sbj_id', 'rel_id', 'obj_id']:
            if field in criteria:
                _filter[f'{field}__id__iexact'] = criteria[field]

        # filter
        triples = None
        if _filter:
            triples = Triple.objects.filter(**_filter)
        else:
            triples = Triple.objects.all()

        return triples

    if request.method == 'GET':
        triples = get_triples_with_criteria(request, request.GET)
        # paginate
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        paginated = Paginator(triples, limit).get_page(page)
        serializer = TripleSerializer(paginated, many=True)
        return HttpResponse(json.dumps(serializer.data, ensure_ascii=False),
                            content_type="application/json; charset=utf-8")


# class KcgViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     List all KCG triples.
#     Provides `list` and `detail` actions.
#     """
#     queryset = Triple.objects.all()
#     serializer_class = TripleSerializer
