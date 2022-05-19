from rest_framework import serializers

from .models import Anime

#Which fields are displayed upon user request (in views)
#Deals with micro-changes passing from the source up to the user
#(ex: source = integer --> applies transformation into % --> displays it to user as %)
class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' #returns all fields; could be exclusive of certain fields for instance (as a tuple); ex: anime and score only or in this case all fields
        model = Anime #which model is impacted by the filter above^
