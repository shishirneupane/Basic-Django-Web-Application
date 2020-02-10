from django.test import TestCase,SimpleTestCase, Client
from .models import *
from .views import *
from django.urls import reverse,resolve

# Create your tests here.

class Test(TestCase): #Model testing     
    def test_dESC(self):
        desc = Movies.objects.create(movie_title="chartpaper", release_date="2002-06-02",
                                      movie_description = "hi there whats up jhcv dcb d b ."
                                      )
        use=Movies.objects.get(movie_title="chartpaper")
        self.assertEquals(use.movie_title,"chartpaper")
    
    def test_title(self):
        desc = Movies.objects.create(movie_title="Lotlot", release_date="2002-06-02",
                                      movie_description = "hi there whats up jhcv dcb d b ."
                                      )
        self.assertTrue(desc.TestTitle())


class Test_URL(SimpleTestCase): #Url testing
    def test_movie_list(self):
        url=reverse("watch:movies")
    
        self.assertEquals(resolve(url).func,movies_list)


class Test_v(SimpleTestCase):    #VIews testing
    def test_register(self):
        c=Client()
        url=reverse("watch:register")
        response=c.get(url)
        self.assertEquals(response.status_code,200)
    
    def test_login(self):   #reverse is used to show path 
        c=Client()
        url=reverse("watch:login")
        response=c.get(url)
        self.assertEquals(response.status_code,200)
