from rest_framework import serializers
from kcg.models import Triple

class TripleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Triple
        fields = ('uid', 'sbj', 'rel', 'obj', 'confidence', 'source', 'context')
