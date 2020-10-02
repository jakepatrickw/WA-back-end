from django.test import TestCase
from django.urls import reverse
#test
class UserProfileTest(TestCase):
    def test_valid_payload(self):
        url = reverse('user_profile')
        catch_phrase = 'fake phrase'
        biography = 'user input describing player'
        user_id = '1'
        data = {'catch_phrase':catch_phrase,'biography':biography,'user_id':user_id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
    
    def test_no_biography(self):
        url = reverse('user_profile')
        catch_phrase = 'fake phrase'
        user_id = '2'
        data = {'catch_phrase':catch_phrase, 'biography':'', 'user_id':user_id}
        try:
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 200)
        except:
            self.assertEqual(response.status_code, 400)

    def test_no_catchphrase(self):
        url = reverse('user_profile')
        biography = 'user input describing player'
        user_id = '1'
        data = {'catch_phrase':'', 'biography':biography, 'user_id':user_id}
        try:
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 200)
        except:
            self.assertEqual(response.status_code, 400)
    
    def test_no_user_id(self):
        url = reverse('user_profile')
        biography = 'user input describing player'
        catch_phrase = 'fake phrase'
        data = {'catch_phrase':catch_phrase, 'user_id':'', 'biography':biography}
        try:
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, 200)
        except:
            self.assertEqual(response.status_code, 400)
