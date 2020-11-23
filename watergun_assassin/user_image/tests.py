from django.test import TestCase
from django.urls import reverse

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

