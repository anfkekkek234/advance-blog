from django.urls import include, path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path('go-to-maktabkhooneh/<int:pk>/',views.RedirectToMaktab.as_view(),name='redirect-to-maktabkhooneh'),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path(
        "post/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
