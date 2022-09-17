from django.test import TestCase
from ..forms import UserProfileForm


class TestProfileForm(TestCase):

    def test_profile_form_is_valid(self):
        form = UserProfileForm(data={
            'user': 'User',
            'default_phone_number': 'Phone Number',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postal Code',
            'default_county': 'County, State or Locality',
        })
        self.assertTrue(form.is_valid())

    def test_profile_form_is_not_valid(self):
        form = UserProfileForm()
        self.assertFalse(form.is_valid())
