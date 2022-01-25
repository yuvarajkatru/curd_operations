from django.test import TestCase
from .models import ebook


class EbookTest(TestCase):
    """ Test module for Ebook model """

    def setUp(self):
        Puppy.objects.create(
            Title='best cricket player', Author="yuvi", Genre='Fantasy', Review='super', Favorite='quick shots')
        Puppy.objects.create(
            Title='best score in cricket ', Author="virat", Genre='Fantasy', Review='Number One player', Favorite='runmachine')

    def test_puppy_breed(self):
        yuvi_ebook = ebook.objects.get(name='best cricket player')
        virat_ebook = ebook.objects.get(name='best score in cricket')
        self.assertEqual(
            yuvi_ebook.get_Author(), "best cricket player yuvi Favorite quick shots.")
        self.assertEqual(
            virat_ebook.get_Author(), "best score in cricket virat Favorite runmachine.")
