from rest_framework import serializers

#Id serializer
class IdSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def restore_object(self,attrs, instance=None):
        """
        Create or update a new Id instance, given dictionary
        or deserialized field values
        """
        if instance:
            instance.id = attrs.get('id', instance.id)

            return instance


        return Id(**attrs)
