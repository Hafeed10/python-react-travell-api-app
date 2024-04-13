from rest_framework.serializers import ModelSerializer
from places.models import Place, Gallery 
from rest_framework import serializers






class GallerySerializer(ModelSerializer):  
    class Meta:
        model = Gallery
        fields = ('id', 'name', 'image')

class PlaceSerializer(ModelSerializer):  
    category =  serializers.SerializerMethodField()
    gallery =  serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('id', 'name', 'place_field', 'category', 'gallery')

    def get_category(self, instance):
        return instance.category.name 

    def get_gallery(self, instance):
        images = instance.gallery.all()
        serializer = GallerySerializer(images, many=True)
        return serializer.data

class PlaceDetailSerializer(ModelSerializer): 
    class Meta:
        model = Place
        fields = ('id', 'name', 'place_field', 'description', 'category', 'gallery')


