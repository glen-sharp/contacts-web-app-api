from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

    @staticmethod
    def delete(id):
        Contact.objects.filter(id=id).delete()
