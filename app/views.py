from django.views import generic
from .forms import PostCreateForm
from .models import Post, ParentCategory


class PostCreate(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = '/'  # reverse_lazy等のほうが良い。これは手抜き

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parentcategory_list'] = ParentCategory.objects.all()
        return context
