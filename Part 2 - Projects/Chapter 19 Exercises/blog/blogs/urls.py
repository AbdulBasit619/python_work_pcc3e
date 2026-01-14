"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = "blogs"

urlpatterns = [
    # URL for the home page.
    path("", views.index, name="index"),
    # URL for blogs page.
    path("blogs/", views.blogs, name="blogs"),
    # URL to view an individual blog, and all its posts.
    path("blog/<int:blog_id>", views.blog, name="blog"),
    # Page to create a new blog.
    path("new_blog/", views.new_blog, name="new_blog"),
    # Page to create a new blog post.
    path("new_post/<int:blog_id>/", views.new_post, name="new_post"),
    # Page to edit an existing post.
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
]
