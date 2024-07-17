from .models import Singer, Song
from rest_framework import serializers

class SingerSerializer(serializers.ModelSerializer):
    # songs = serializers.StringRelatedField(many=True, read_only=True)
    # songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    songs = serializers.HyperlinkedRelatedField(many=True, read_only=True, \
            view_name = 'song-detail') #here view_name must be Modelname-detail
    # songs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='duration')
    songs = serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songs']

class SongSerializer(serializers.ModelSerializer):
    singer = serializers.StringRelatedField()
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']

'''
Summary of Differences
HyperlinkedRelatedField:

Used for representing relationships between models.
Provides a hyperlink to the related model's detail view.
Commonly used for foreign key and many-to-many relationships.
HyperlinkedIdentityField:

Used for representing the identity of the resource itself.
Provides a hyperlink to the resource's own detail view.
Commonly used to link to the current resource's detail view.
'''