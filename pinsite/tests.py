from django.core.urlresolvers import resolve
from django.test import TestCase
from django.test import TestCase, RequestFactory
from pins.models import Category
from pins.views import home, category


class ViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page_view(self):
        request = self.factory.get('/')
        response = home(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('HomePage.html')

    def test_category_list_view(self):
        Category.objects.create(title='Amsterdam in the 50s',slug='amsterdam-in-the-50s')
        request = self.factory.get('/')
        response = category(request, slug='amsterdam-in-the-50s')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('Category.html')










