from django.test import TestCase
from django.shortcuts import reverse


class LandingPageView(TestCase):

    def test_get(self):
        # TODO some sort of test
        response = self.client.get(reverse("landing_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')
