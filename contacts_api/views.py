from rest_framework.decorators import api_view
from rest_framework.response import Response
from jsonschema import validate, ValidationError
from rest_framework import status
import logging

from .models import Contact
from .serializers import ContactSerializer
from .payload_schema import schema

logger = logging.getLogger("root")

# If required, log level can be parameterised via environment variable
logging.getLogger().setLevel("INFO")


@api_view(["GET"])
def contact_details(request):
    # Using in-build Django model methods to retrieve contacts
    contacts = Contact.objects.all()

    # Serialized into array of objects
    serializer = ContactSerializer(contacts, many=True)
    return Response({"contact_array": serializer.data})


@api_view(["POST"])
def add_contact(request):
    serializer = ContactSerializer(data=request.data)
    # Using mandatory in-built Django field validation for adding table entry
    if serializer.is_valid():
        try:
            # in-build field validation does not validate datatypes, therefore using
            # jsonschema library to validate the contents
            validate(instance=request.data, schema=schema)
        except ValidationError:
            logger.info("Payload validation failed")
            return Response(
                {"message": "Bad request"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Saves input contect to DB
        serializer.save()
        logger.info("New contact added")
        return Response({"message": "Contact added"})
    return Response(
        {"message": "Bad request"},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["DELETE"])
def delete_contact(request):
    id = request.query_params.get("id")
    # If ID query param is not provided, return 400 error
    if not id:
        logger.info("ID field not included as query parameter")
        return Response(
            {"message": "Bad request"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    # Call static method to delete entry from table
    ContactSerializer.delete(id)
    logger.info(f"id={id} deleted")
    return Response({"message": f"id={id} successfully deleted"})
