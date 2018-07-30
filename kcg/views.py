from rest_framework import viewsets
from kcg.models import Triple
from kcg.serializers import TripleSerializer

class KcgViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all KCG triples. 
    Provides `list` and `detail` actions.
    """
    queryset = Triple.objects.all()
    serializer_class = TripleSerializer

# @csrf_exempt
# def triple_list(request):
#     """
#     List all KCG triples.
#     """
#     if request.method == 'GET':
#         triples = Triple.objects.all()
#         serializer = TripleSerializer(triples, many=True)
#         return JsonResponse(serializer.data, safe=False)
