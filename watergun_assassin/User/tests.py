from django.contrib.auth.models import User
from .models import UserProfile
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
import logging


class UserCreationTest(TestCase):
    
    def test_valid_payload(self):
        # factory = APIRequestFactory()
        # request = factory.post('create/', {'username':'admin', 'password':'fakepass',
        #                         'email':'email@company.com'}, format='json')
        # self.assertEqual(request.status_code, 201)
        url = reverse('CreateUser')
        username = 'admin'
        password = 'fakepassword'
        email = 'email@company.com'
        data = {'username' : username, 'password' : password, 'email' : email}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_only_email(self):
        url = reverse('CreateUser')
        email = 'email@company'
        data = {'username' : '', 'password' : '', 'email' : email}
        try:
            response = self.client.post(url, data)
            print(response.json())
        except:
            self.assertEqual(response.status_code, 400)

    def test_no_email(self):
        url = reverse('CreateUser')
        username = 'newname'
        password = 'fakepassword'
        data = {'username' : username, 'password' : password}
        try:
            response = self.client.post(url, data)
            print(response)
        except:
            self.assertEqual(response.status_code, 400)
        
    def test_no_password(self):
        url = reverse('CreateUser')
        username = 'newname'
        email = 'email@company.com'
        data = {'username':username, 'email':email}
        try:
            response = self.client.post(url, data)
            print(response)
        except:
            self.assertEqual(response.status_code, 400)
    
    def test_list_users(self):
        url = reverse('ListAllUser')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_read_single_user(self):
        url = reverse('UserLookup', kwargs={'id':1})
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)    

    def test_update_username(self):
        url = reverse('UpdateUser', kwargs={'id': 1})
        new_username = 'BIGadmin'
        data = {'username' : new_username}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)    


class UsermImageTest(TestCase):
    
    def test_valid_payload(self):
        url = reverse('UploadImage')
        picture = 'Users/jakep/Pictures/Screenshots/photo.png'
        user_id = '1'
        data = {'picture':picture, 'user_id':user_id}
        response = self.client.post(url ,data)
        self.assertEqual(response.status_code, 201)

    def test_no_user_id(self):
        url = reverse('UploadImage')
        picture = 'Users/jakep/Pictures/Screenshots/photo'
        data = {'picture':picture, 'user_id':''}
        try:
            response = self.client.post(url, data)
            print(response.json())
        except:
            self.assertEqual(response.status_code, 400)
        
    def test_no_user_image(self):
        url = reverse('UploadImage')
        user_id = '2'
        data = {'picture':'', 'user_id':user_id}
        try:
            response = self.client.post(url, data)
            print(response.json())
        except:
            self.assertEqual(response.status_code, 400)
    
    def test_image_list(self):
        url = reverse('ListImage')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_read_single_image(self):
        url = reverse('ListImage', kwargs={'user_id':1})
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_update_image(self):
        url = reverse('UpdateImage', kwargs={'user_id':1})
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)


class UserProfileTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     cls.user = User(username='bob', email='work@place.com')
    #     cls.user.save()
    #     print(cls.user)
    #     print(cls.user.id)

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
