from django.contrib import admin
from snippets.models import Snippet

#adminサイトでSnippetテーブルを設定できるように登録する
admin.site.register(Snippet)
