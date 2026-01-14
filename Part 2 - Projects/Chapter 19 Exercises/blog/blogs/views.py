from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm


# Create your views here.
def index(request):
    """The home page for learning log."""
    return render(request, "blogs/index.xhtml")


def blogs(request):
    """Show all blogs on the page."""
    blogs = Blog.objects.order_by("name")
    context = {"blogs": blogs}
    return render(request, "blogs/blogs.xhtml", context)


def blog(request, blog_id):
    """Show a blog on the page, along with all its posts."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.all()

    context = {"blog": blog, "posts": posts}
    return render(request, "blogs/blog.xhtml", context)


def new_blog(request):
    """Page to create a new blog."""
    if request.method != "POST":
        # No data submitted; display a new form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blogs")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "blogs/new_blog.xhtml", context)


@login_required
def new_post(request, blog_id):
    """Create a new blog post."""
    blog = Blog.objects.get(id=blog_id)

    if request.method != "POST":
        # No data submitted; display a new form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.owner = request.user
            new_post.save()
            return redirect("blogs:blog", blog_id=blog_id)

    # Display a blank or invalid form.
    context = {"blog": blog, "form": form}
    return render(request, "blogs/new_post.xhtml", context)


@login_required
def edit_post(request, post_id):
    """Edit an existing blog post."""
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog

    # Make sure the post belongs to the current user.
    if post.owner != request.user:
        raise Http404

    if request.method != "POST":
        # Initial request; pre-fill the form with entry.
        form = BlogPostForm(instance=post)
    else:
        # Post data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blog", blog_id=blog.id)

    # Return a blank or invalid form.
    context = {"post": post, "blog": blog, "form": form}
    return render(request, "blogs/edit_post.xhtml", context)
