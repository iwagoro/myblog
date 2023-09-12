
from .models import Post
from django.shortcuts import render,get_object_or_404
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #今日以前に公開された記事を取得し、公開日時の昇順で並び替える
    return render(request,'blog/post_list.html',{'posts':posts}) #requestはユーザーが要求する全ての情報を持っているオブジェクト、{}はテンプレートに渡すコンテキスト(辞書型変数)

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})