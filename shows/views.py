from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse


def shows_all(request):
    shows = models.TVShow.objects.all()
    return render(request, 'shows_list.html', {'shows': shows})


def shows_detail(request, id):
    show = get_object_or_404(models.TVShow, id=id)
    return render(request, 'shows_detail.html', {'show': show})


def add_show(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Show created')
    else:
        form = forms.ShowForm()
    return render(request, 'add_shows.html', {'form': form})
