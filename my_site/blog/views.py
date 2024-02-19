from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse

from .models import Post, Author

from django.views.generic import DetailView, ListView

class AuthorView(DetailView):
    template_name = "author.html"
    model = Author
    context_object_name = "author"
    slug_field = 'slug'
    slug_url_kwarg = 'author_slug'
    



class StartingPageView(ListView):
    template_name = "index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

""" def starting_page(request):
    latest_posts= Post.objects.all().order_by("-date")[:3]

    return render(request, 'blog/index.html', {
        "post": latest_posts}) """


class AllPostsView(ListView):
    template_name = "all-posts.html"
    model = Post
    context_object_name = "all_posts"

""" def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {
        "all_posts" : all_posts
    }) """

class SinglePostView(DetailView):
    template_name = "post-detail.html"
    model = Post
    # DetailView automatically handles slug, if urls.py has it.
    def get_context_data(self, **kwargs): # for the tag field on header
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
    

""" def post_detail(request, slug):
    idendified_post = Post.objects.get(slug=slug)
    return render(request, 'blog/post-detail.html', {
        "post" : idendified_post,
        "post_tags" : idendified_post.tags.all()
    })  """