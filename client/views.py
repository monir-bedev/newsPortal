from django.urls import reverse
from django.views import generic
from django.views.generic.detail import SingleObjectMixin

from blog.forms import CommentForm
from blog.models import Post, Category

# Create your views here.

# Home page
class FrontPageTemplateView(generic.TemplateView):
    model = Post
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        latest_posts = Post.objects.all().order_by('-created_at')[:2]
        national_posts = Post.objects.filter(category__name='National')
        features = Post.objects.filter(category__name='Features')
        business = Post.objects.filter(category__name='Business')
        technology = Post.objects.filter(category__name='Technology')
        entertainment = Post.objects.filter(category__name='Entertainment')
        sports = Post.objects.filter(category__name='Sports')
        categories = Category.objects.all()[:4]

        context = {
            'national_posts': national_posts,
            'features': features,
            'categories': categories,
            'business': business,
            'technology': technology,
            'entertainment': entertainment,
            'latest_posts': latest_posts,
            'sports': sports,
        }
        return self.render_to_response(context)


class DetailPageView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'
