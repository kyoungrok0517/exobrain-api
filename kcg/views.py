from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from kcg.models import Triple
from kcg.serializers import TripleSerializer

@csrf_exempt
def triple_list(request):
    """
    List all KCG triples.
    """
    if request.method == 'GET':
        triples = Triple.objects.all()
        serializer = TripleSerializer(triples, many=True)
        return JsonResponse(serializer.data, safe=False)
