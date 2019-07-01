from django.http import JsonResponse
from django.views import generic
from app.forms import PostCreateForm
from app.models import Post, Category


class PostCreate(generic.CreateView):
    template_name = 'app2/post_form.html'
    model = Post
    form_class = PostCreateForm
    success_url = '/'  # reverse_lazy等のほうが良い。これは手抜き


def ajax_get_category(request):
    pk = request.GET.get('pk')
    # pkパラメータがない、もしくはpk=空文字列だった場合は全カテゴリを返しておく。
    if not pk:
        category_list = Category.objects.all()

    # pkがあれば、そのpkでカテゴリを絞り込む
    else:
        category_list = Category.objects.filter(parent__pk=pk)

    # [ {'name': 'サッカー', 'pk': '3'}, {...}, {...} ] という感じのリストになる。
    category_list = [{'pk': category.pk, 'name': category.name} for category in category_list]

    # JSONで返す。
    return JsonResponse({'categoryList': category_list})
