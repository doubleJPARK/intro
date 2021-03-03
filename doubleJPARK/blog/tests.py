from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
    
    
    def navbar_test(self, soup):
        navbar = soup.nav
        self.assertIn('BLOG', navbar.text)
        self.assertIn('About_doubleJ', navbar.text)
        
        
        logo_btn = navbar.find('a', text='HOME')
        self.assertEqual(logo_btn.attrs['href'], '/')
        
        logo_btn = navbar.find('a', text='About_doubleJ')
        self.assertEqual(logo_btn.attrs['href'], '/about_me/')
        
        logo_btn = navbar.find('a', text='BLOG')
        self.assertEqual(logo_btn.attrs['href'], '/blog/')
