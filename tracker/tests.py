# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile,Neighborhood,Posts
# # Create your tests here.


class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Profile(first_name = 'James', last_name ='Muriuki', bio ='james@moringaschool.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.james.create_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


class NeighborhoodTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Neighborhood(name = 'James', location ='Muriki', country ='KE',health='+25402555552', police='+25402555552',fire='+25402555552', pic='hnm')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Neighborhood))

    # Testing Save Method
    def test_save_method(self):
        self.james.create_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) > 0)


class PostsTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.post= Posts(post = 'musical')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Posts))

    def test_save_method(self):
        self.post.save_post()
        posts  = Posts.objects.all()
        self.assertTrue(len(posts)>0)
