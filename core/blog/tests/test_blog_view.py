from datetime import datetime

from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import Profile, User
from blog.models import Post


class TestBlogView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="test@gmail.com", password="a/mdadmsm"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="ali",
            last_name="nrnfnf",
            description="dnnsdn",
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="test",
            content="rfrf",
            status=True,
            category=None,
            published_date=datetime.now(),
        )

    def test_blog_url_succussful_response(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(str(response.content).find("index"))
        self.assertTemplateUsed(response, template_name="index.html")

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_blog_post_detail_annonymouse_response(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
