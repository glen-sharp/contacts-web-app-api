from .serializers import ContactSerializer

from django.test import TestCase, Client
import json


class ContactsTestClass(TestCase):
    def setUp(self):
        """
        Adding mock data to test DB
        """
        serializer = ContactSerializer(
            data={
                "forename": "Jane",
                "surname": "Doe",
                "address": "Bristol",
                "phone_number": 60840833434,
            },
        )
        serializer.is_valid()
        serializer.save()
        self.client = Client()
        pass

    def test_get_contacts(self):
        """
        Testing get contacts response
        """
        response = self.client.get("/contact_details/")
        expected_response = {"contact_array": [{
            "id": 1,
            "forename": "Jane",
            "surname": "Doe",
            "address": "Bristol",
            "phone_number": 60840833434,
        }]}
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), expected_response)

    def test_add_contact(self):
        """
        Testing add contact endpoint
        """
        body = {
            "forename": "John",
            "surname": "Smith",
            "address": "London",
            "phone_number": 40578048504,
        }
        response = self.client.post(
            "/add_contact/",
            json.dumps(body),
            content_type="application/json",
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), {"message": "Contact added"})

    def test_bad_request_add_contact(self):
        """
        Testing bad request for adding contact
        "forename" field incorrect
        """
        body = {
            "fore_name": "John",
            "surname": "Smith",
            "address": "London",
            "phone_number": 40578048504,
        }
        response = self.client.post(
            "/add_contact/",
            json.dumps(body),
            content_type="application/json",
        )
        self.assertEquals(response.status_code, 400)
        self.assertEquals(json.loads(response.content), {"message": "Bad request"})

    def test_delete_contact(self):
        """
        Testing delete contact
        """
        response = self.client.delete("/delete_contact/?id=1")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), {"message": "id=1 successfully deleted"})
