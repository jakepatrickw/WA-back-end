from django.test import TestCase
from django.urls import reverse

class UsermImageTest(TestCase):
    
    def test_valid_payload(self):
        url = reverse('user_image')
        picture = 'Users/jakep/Pictures/Screenshots/photo'
        user_id = '1'
        data = {'picture':picture, 'user_id':user_id}
        response = self.client.post(url ,data)
        self.assertEqual(response.status_code, 200)

    def test_no_user_id(self):
        url = reverse('user_image')
        picture = 'Users/jakep/Pictures/Screenshots/photo'
        data = {'picture':picture, 'user_id':''}
        try:
            response = self.client.post(url, data)
            print(response.json())
        except:
            self.assertEqual(response.status_code, 400)
        
    def test_no_user_image(self):
        url = reverse('user_image')
        user_id = '2'
        data = {'picture':'', 'user_id':user_id}
        try:
            response = self.client.post(url, data)
            print(response.json())
        except:
            self.assertEqual(response.status_code, 400)
