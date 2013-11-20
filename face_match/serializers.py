from rest_framework import serializers



# Serializer here
# Maybe we don't need serialization at all
#class AccessTokenSerializer(serializers.Serializer):
    #token = serializers.CharField(max_length=500) #There isn't a defined size for the tokens

#class AccessTokenSerializer(serializers.Serializer):
class IdSerializer(serializers.Serializer):
    id = serializer.IntegerField()
