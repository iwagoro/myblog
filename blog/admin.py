from django.contrib import admin
from .models import Post            #カレントディレクトリからモデルをインポート
# Register your models here.

admin.site.register(Post)           #モデルをサイトに登録し、adminページで見れるようにする