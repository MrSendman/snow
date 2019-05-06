from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin
from django.core.paginator import Paginator


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'blog/index.html', context={'posts':page })


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'



def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})
