from django.test import TestCase
from django.urls import reverse

class UserCreationTest(TestCase):
    
    def test_valid_payload(self):
        url = reverse('create_user')
        username = 'admin'
        password = 'fakepassword'
        email = 'email@company.com'
        data = {'username' : username, 'password' : password, 'email' : email}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_only_email(self):
        url = reverse('create_user')
        email = 'email@company'
        data = {'username' : '', 'password' : '', 'email' : email}
        try:
            response = self.client.post(url, data)
            print(response.json())
        except:
            self.assertEqual(response.status_code, 400)

    def test_no_email(self):
        url = reverse('create_user')
        username = 'newname'
        password = 'fakepassword'
        data = {'username' : username, 'password' : password}
        try:
            response = self.client.post(url, data)
            print(response)
        except:
            self.assertEqual(response.status_code, 400)
        
    def test_no_password(self):
        url = reverse('create_user')
        username = 'newname'
        email = 'email@company.com'
        data = {'username':username, 'email':email}
        try:
            response = self.client.post(url, data)
            print(response)
        except:
            self.assertEqual(response.status_code, 400)
    
    def test_read_user(self):
        url = reverse('read_user')
        username = 'admin'
        data = {'username' : username}
        response = self.client.get(url, data)
        print(response)
        self.assertEqual(response.status_code, 200)
        
    def test_user_read_no_data(self):
        url = reverse('read_user')
        username = ''
        data = {'username': username}
        try:
            response = self.client.get(url, data)
            print(response)
        except:
            self.assertEqual(response.status_code, 400)

    def test_update_username(self):
        url = reverse('update_username')
        old_username = 'admin'
        new_username = 'BIGadmin'
        data = {'old_username' : old_username, 'new_username' : new_username} 
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)    
