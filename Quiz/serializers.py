
# # import serializer from rest_framework
# from rest_framework import serializers
 
# # import model from models.py
# from .models import QuesModel
 
# # Create a model serializer
# class GeeksSerializer(serializers.HyperlinkedModelSerializer):
#     # specify model and fields
#     class Meta:
#         model = QuesModel
#         fields = ('title', 'description')



from rest_framework import serializers

from Quiz.models import Person, Species

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('name', 'birth_year', 'eye_color', 'species')


class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Species
       fields = ('name', 'classification', 'language')