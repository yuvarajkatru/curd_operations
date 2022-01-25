import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import ebook
from .serializers import EbookSerializer


# initialize the APIClient app
client = Client()

class GetAllEbooksTest(TestCase):
    """ Test module for GET all ebooks API """

    def setUp(self):
        ebook.objects.create(
            title='best cricket player', author="yuvi", genre='Fantasy', review='super', favorite='quick shots')
        ebook.objects.create(
            title='best cricket player', author="yuvi", genre='Fantasy', review='super', favorite='quick shots')
        ebook.objects.create(
            title='best cricket player', author="yuvi", genre='Fantasy', review='super', favorite='quick shots')
        ebook.objects.create(
            title='best cricket player', author="yuvi", genre='Fantasy', review='super', favorite='quick shots')

    def test_get_all_ebooks(self):
        # get API response
        response = client.get(reverse('get_post_ebook'))
        # get data from db
        ebooks = ebook.objects.all()
        serializer = EbookSerializer(ebooks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleEbookTest(TestCase):
    """ Test module for GET single Ebook API """

    def setUp(self):
        self.allrounder = ebook.objects.create(
            title='best cricket allrounder', author="yuvi", genre='Fantasy', review='super', favorite='quick shots')
        self.batsmen = ebook.objects.create(
            title='best cricket batsmen', author="virat", genre='Fantasy', review='super', favorite='quick shots')
        self.fielder = ebook.objects.create(
            title='best cricket fielder', author="raina", genre='Fantasy', review='super', favorite='quick shots')
        self.bowler = ebook.objects.create(
            title='best cricket bowler', author="praveen", genre='Fantasy', review='super', favorite='swing')

    def test_get_valid_single_ebook(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': self.batsmen.pk}))
        ebook = ebook.objects.get(pk=self.batsmen.pk)
        serializer = EbookSerializer(ebook)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_ebook(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
