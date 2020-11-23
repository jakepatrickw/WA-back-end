import logging
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User(username='bob', email='work@place.com')
        cls.user.save()
        print(cls.user)
        print(cls.user.id)

    # def test_valid_payload(self):
    #     url = reverse('UserProfileCreate')
    #     catch_phrase = 'fake phrase'
    #     biography = 'user input describing player'
    #     user_id = 1
    #     data = {'catch_phrase':catch_phrase,'biography':biography,'user_id':user_id}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, 201)
    
    # def test_no_biography(self):
    #     url = reverse('UserProfileCreate')
    #     catch_phrase = 'fake phrase'
    #     user_id = '2'
    #     data = {'catch_phrase':catch_phrase, 'biography':'', 'user_id':user_id}
    #     try:
    #         response = self.client.post(url, data)
    #         print(response.json())
    #     except:
    #         self.assertEqual(response.status_code, 400)

    # def test_no_catchphrase(self):
    #     url = reverse('UserProfileCreate')
    #     biography = 'user input describing player'
    #     user_id = '1'
    #     data = {'catch_phrase':'', 'biography':biography, 'user_id':user_id}
    #     try:
    #         response = self.client.post(url, data)
    #         print(response.json())
    #     except:
    #         self.assertEqual(response.status_code, 400)
    
    # def test_no_user_id(self):
    #     url = reverse('UserProfileCreate')
    #     biography = 'user input describing player'
    #     catch_phrase = 'fake phrase'
    #     data = {'catch_phrase':catch_phrase, 'user_id':'', 'biography':biography}
    #     try:
    #         response = self.client.post(url, data)
    #         print(response.json())
    #     except:
    #         self.assertEqual(response.status_code, 400)
    
    # def test_read_users(self):
    #     url = reverse('UserProfileList')
    #     response = self.client.get(url)
    #     print(response)
    #     self.assertEqual(response.status_code, 200)

    def test_read_single_user(self):
        url = reverse('UserProfileLookup', kwargs={'user_id':1})
        print(url)
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)


