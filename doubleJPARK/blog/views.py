from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# FBV 스타일 코드임 아마 앞으로 안 쓸것 같음
# def index(request):
#    posts = Post.objects.all().order_by('-pk')
#
#    return render(
#        request,
#        'blog/index.html',
#        {
#            'posts': posts
#        }
#    )


# def single_post_page(request, pk):
#    post = Post.objects.get(pk=pk)
#
#    return render(
#        request,
#        'blog/single_post_page.html',
#        {
#            'post': post,
#        }
#    )