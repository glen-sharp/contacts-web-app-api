from rest_framework.decorators import api_view
from rest_framework.response import Response
from jsonschema import validate, ValidationError
from rest_framework import status
import logging

from .models import Contact
from .serializers import ContactSerializer
from .payload_schema import schema

logger = logging.getLogger("root")


@api_view(["GET"])
def contact_details(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response({"contact_array": serializer.data})


@api_view(["POST"])
def add_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        try:
            validate(instance=request.data, schema=schema)
        except ValidationError:
            return Response(
                {"message": "Bad request"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response({"message": "Contact added"})
    return Response(
        {"message": "Bad request"},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["DELETE"])
def delete_contact(request):
    id = request.query_params.get("id")
    if not id:
        return Response(
            {"message": "Bad request"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    ContactSerializer.delete(id)
    return Response({"message": f"id={id} successfully deleted"})
