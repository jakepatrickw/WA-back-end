from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

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
