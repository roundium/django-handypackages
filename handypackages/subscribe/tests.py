from django.test import TestCase

from .models import Subscribe


class TestModels(TestCase):
    def setUp(self):
        self.subscribe_email = Subscribe.objects.create(
            email="1234@mail.com",
        )

    def test_email_subscribe_model(self):
        self.assertEqual(
            str(self.subscribe_email),
            "1234@mail.com",
            "__str__ of Subscribe email is not Working!",
        )

        main_dict = {
            "email": self.subscribe_email.email,
            "id": self.subscribe_email.id,
            "create_time": str(self.subscribe_email.create_time),
        }
        hash_code = self.subscribe_email.generate_hash
        result_dict = Subscribe.unsign_hash(hash_code)

        self.assertEqual(
            result_dict,
            main_dict,
            "unsign hash code does not work!",
        )

        result = Subscribe.unsign_hash(hash_code + "dmsklmd")
        self.assertEqual(
            result,
            False,
            "unsign hash code does not work!",
        )
