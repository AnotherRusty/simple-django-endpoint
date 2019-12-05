from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class TestStudentSpecifiesCommuteDistance(TestCase):
    def test_successfully(self):
        examples = [
            {"username" : "joe", "miles": 42},
            {"username": "betty", "miles": 456789}
        ]

        for example in examples:
            user = User.objects.create_user(example['username'])

            self.client.force_login(user)

            self.client.post(
                reverse('mileage_tracker:set_commute'),
                {"miles": example['miles']}
            )

            self.assertEqual(user.distancetowork.miles, example['miles'])