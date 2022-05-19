from core.models import Anime
from django.shortcuts import get_object_or_404
from core.serializers import AnimeSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.forms.models import model_to_dict

#https://www.django-rest-framework.org/api-guide/viewsets/
#This is where updating the data (destroy, update, etc.) is defined; refer to documentation above^

#EX:
#http://127.0.0.1:8000/anime/?title=Spy x Family
#http://127.0.0.1:8000/anime/?title=spy x family
#http://127.0.0.1:8000/anime/?title=Naruto

#Inherits class
class AnimeViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Anime.objects.all()
        serializer = AnimeSerializer(queryset, many=True)
        #print(request.query_params.get('title'))
        title = request.query_params.get('title')

        if title is not None:
            anime = queryset.filter(
                title__iexact=title
            ).first()
            return Response(model_to_dict(anime))

        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Anime.objects.all()
        anime = get_object_or_404(queryset, pk=pk)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)