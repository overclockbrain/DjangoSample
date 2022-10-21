from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from snippets.models import Snippet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404
from snippets.forms import SnippetForm

# Create your views here.
def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}
    return render(request,"snippets/top.html",context)

# @はデコレータといい修飾されている関数(今回はsnippet_new)の前後に自身の処理、今回はログイン処理を
# 追加できる便利なもの
@login_required
def snippet_new(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save() #commitの確定
            return redirect(snippet_detail,snippet_id=snippet.pk)
    else:
        form = SnippetForm()
    return render(request,"snippets/snippet_new.html",{"form":form})

def snippet_edit(request,snippet_id):
    snippet = get_object_or_404(Snippet,pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden("このスニペットの編集は許可されていません。")

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect("snippet_detail",snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    return render(request,"snippets/snippet_edit.html",{"form":form})

def snippet_detail(request,snippet_id):
    snippet = get_object_or_404(Snippet,pk=snippet_id) 
    return render(request,"snippets/snippet_detail.html",{"snippet":snippet})