from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass      
    
    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')   

class ContactViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contato')

    def TearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)          


