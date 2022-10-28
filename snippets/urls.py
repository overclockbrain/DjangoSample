from urllib.parse import urlparse
from django.urls import URLPattern, path
from snippets import views

urlpatterns = [
    path("new/",views.snippet_new,name="snippet_new"),
    path("<int:snippet_id>/",views.snippet_detail,name="snippet_detail"),
    path("<int:snippet_id>/edit/",views.snippet_edit,name="snippet_edit"),
]