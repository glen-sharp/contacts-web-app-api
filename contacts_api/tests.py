from .serializers import ContactSerializer

from django.test import TestCase, Client

client = Client()


class ContactsTestClass(TestCase, ContactSerializer):
    def setUp(self):
        pass

    def test_get_contact(self):
        response = client.get("/contact_details/")
        print(response.status_code)
        print(response.content)

        # self.assertEquals(1, 1)
