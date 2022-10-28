from urllib import request, response
from django.test import TestCase,Client,RequestFactory
from django.http import HttpRequest

from django.urls import resolve
from snippets.views import top, snippet_new, snippet_edit,snippet_detail
from django.contrib.auth import get_user_model
from snippets.models import Snippet

UserModel = get_user_model()

# トップページに作成した投稿が表示されるかテストする
class TopPageRenderSnippetsTest(TestCase):
    # テストユーザーを作成する関数
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.snippet = Snippet.objects.create(
            title = "title1",
            code="print('hello')",
            description = "description1",
            created_by = self.user,
        )
    
    # テストデータとして与えたタイトルを正しく返すかテストする関数
    def test_should_return_snippet_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response,self.snippet.title)

    # テストデータとして与えたUserNameを正しく返すかテストする関数
    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)

class TopPageTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertContains(response, "Djangoスニペット",status_code=200)

    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response,"snippets/top.html")

class CreateSnippetTest(TestCase):
    # テストユーザーを作成する関数
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="secret",
        )
        self.client.force_login(self.user)

    def test_render_creation_form(self):
        response = self.client.get("/snippets/new/")
        self.assertContains(response,"スニペットの登録",status_code=200)

    def test_create_snippet(self):
        data = {"title":"タイトル","code":"コード","description":"解説"}
        self.client.post("/snippets/new/",data)
        snippet = Snippet.objects.get(title="タイトル")
        self.assertEqual("コード",snippet.code)
        self.assertEqual("解説",snippet.description)

class SnippetDetailTest(TestCase):
    # テストユーザーを作成する関数
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="secret",
        )
        self.snippet = Snippet.objects.create(
            title = "タイトル",
            code="コード",
            description = "解説",
            created_by = self.user,
        )

    def test_should_resolve_snippet_template(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertTemplateUsed(response,"snippets/snippet_detail.html")

    def test_top_page_returns_200_and_expected_heading(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertContains(response, self.snippet.title ,status_code=200)

class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve("/snippets/1/edit/")
        self.assertEqual(snippet_edit,found.func)