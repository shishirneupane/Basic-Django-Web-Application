from django.test import TestCase
from .models import *


# Create your tests here.


class Test(TestCase):

    # def Test_ReleaseDate(self):
    #     prod = Movies.objects.create(movie_title="budget", movie_description="Management", release_date=2020-01-01)
    #     self.assertTrue(prod.TestReleaseDate())

    # def test_product_category(self):
    #     product_category = Product.objects.create(product_name="budget sheet", product_category="Management", product_rate=100.000)
    #     if product_category.product_category == "Management":
    #         self.assertTrue(product_category.TestProductCategory())
    #     elif product_category.product_category == "Science":
    #         self.assertFalse(product_category.TestProductCategory())

    # def test_not_same_productName_and_productCategory(self):
    #     name_validation = Product.objects.create(product_name="Calculator", product_category="Extra",
    #                                              product_rate=300.0000)
    #     self.assertTrue(name_validation.TestProductNameAndCategory())

    def test_dESC(self):
        desc = Movies.objects.create(movie_title="chartpaper", release_date="2002-06-02",
                                      movie_description = "hi there whats up jhcv dcb d b ."
                                      )
        self.assertTrue(desc.TestMovieDescription())
    
    def test_title(self):
        desc = Movies.objects.create(movie_title="Lotlot", release_date="2002-06-02",
                                      movie_description = "hi there whats up jhcv dcb d b ."
                                      )
        self.assertTrue(desc.TestTitle())
     
    
     