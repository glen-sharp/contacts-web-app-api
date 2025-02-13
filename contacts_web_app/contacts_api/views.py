from rest_framework.decorators import api_view
from rest_framework.response import Response
from jsonschema import validate, ValidationError
from rest_framework import status


from .models import Contact
from .serializers import ContactSerializer
from .payload_schema import schema


@api_view(["GET"])
def contact_details(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        try:
            validate(instance=request.data, schema=schema)
        except ValidationError:
            return Response(
                {"msg": "Bad request"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response({"msg": "Success"})
    return Response(
        {"msg": "Bad request"},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["DELETE"])
def delete_contact(request):
    id = request.query_params.get("id")
    ContactSerializer.delete(id)
    return Response({"msg": "Success"})
