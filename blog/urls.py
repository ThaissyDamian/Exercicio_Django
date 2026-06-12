from django.urls import path
from blog.views import PostView, PostDetail

urlpatterns = [
    path("home/", PostView.as_view(), name="home"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
]