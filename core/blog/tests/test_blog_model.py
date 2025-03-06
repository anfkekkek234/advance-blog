from datetime import datetime

from django.test import TestCase

from accounts.models import Profile, User

from ..models import Post


class TestPostMosel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@gmail.com", password="a/mdadmsm"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="ali",
            last_name="nrnfnf",
            description="dnnsdn",
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title="test",
            content="rfrf",
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title, "test")
