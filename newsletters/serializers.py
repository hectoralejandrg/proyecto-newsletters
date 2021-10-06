from rest_framework.serializers import ModelSerializer

from newsletters.models import Newsletters


class NewslettersSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = '__all__'