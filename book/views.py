from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models


def book(request):
    return HttpResponse('book')


def book_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})


def book_detail(request, pk):
    book = get_object_or_404(models.Post, pk=pk)
    return render(request, 'book_detail.html', {'book': book})
