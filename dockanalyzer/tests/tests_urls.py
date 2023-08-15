from django.test import SimpleTestCase
from django.urls import reverse, resolve
from analyzer.views import scanner_view, upload_file
from basic_views.views import *

class TestUrls(SimpleTestCase):

    def test_index_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_scanner_is_resolved(self):
        url = reverse('scanner')
        self.assertEquals(resolve(url).func, scanner_view)

    def test_upload_is_resolved(self):
        url = reverse('upload')
        self.assertEquals(resolve(url).func, upload_file)