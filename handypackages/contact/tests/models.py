from django.test import TestCase

from handypackages.contact.models import Contact


class ContactModelTests(TestCase):
    def setUp(self):
        self.first_contact = Contact.objects.create(
            name="mohammad",
            email="k2527806@gmail.com",
            phone="+985122228888",
            message="i love you"
        )

    def test_text_phrase_model_methods(self):
        self.assertEqual(str(self.first_contact), "k2527806@gmail.com",
                         "__str__ Of Contact Model Have an Issue!")
        self.assertEqual(self.first_contact.__unicode__(), "k2527806@gmail.com",
                         "__unicode__ Of Contact Model Have an Issue!")
