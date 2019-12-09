from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class TestStudentCreatesProfile(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("jimbob")

        self.client.force_login(user)

        self.client.post(
            reverse("showcase:create-profile"),
            {
                "headline": "I like code and such you know",
                "bio": "I'm from a small town and such, ya know",
            },
        )

        self.assertEqual(user.profile.headline, "I like code and such you know")
        self.assertEqual(user.profile.bio, "I'm from a small town and such, ya know")

    def test_form_is_rendered_on_create_profile_page(self):
        user = User.objects.create_user("jimbob")
        self.client.force_login(user)

        response = self.client.get(reverse("showcase:create-profile"))

        self.assertTemplateUsed(response, "create-profile.html")
        self.assertIn('form', response.context)

    
    def test_form_errors_are_rendered_on_invalid_post(self):
        user = User.objects.create_user("jimbob")
        self.client.force_login(user)

        response = self.client.post(reverse("showcase:create-profile"))

        self.assertTemplateUsed(response, "create-profile.html")
        self.assertTrue(response.context['form'].errors)



