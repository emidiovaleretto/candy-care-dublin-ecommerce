from django.test import TestCase

class TestViewHomeIndex(TestCase):

    def test_simple_index_must_return_200(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)


    def test_load_index_template(self):
        self.assertTemplateUsed(template_name='index.html')

    
    def test_page_not_found_must_return_404(self):
        response = self.client.get('/home')
        self.assertEqual(404, response.status_code)