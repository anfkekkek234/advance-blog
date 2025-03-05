from django.test import TestCase
from datetime import datetime
from ..models import Post,Category
from django.contrib.auth import get_user_model
from accounts.models import User,Profile

class TestPostMosel(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email="test@gmail.com",password="a/mdadmsm")
        self.profile = Profile.objects.create(
            user = self.user,
            first_name="ali",
            last_name = "nrnfnf",
            description= "dnnsdn",
        )
        
        
    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = 'rfrf',
            status = True,
            category = None,
            published_date = datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title,'test')