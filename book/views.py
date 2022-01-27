from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from . import models, forms
from django.views import generic


class BookListView(generic.ListView):
    template_name = 'post_list.html'
    queryset = models.Post.objects.all()

    def get_queryset(self):
        return models.Post.objects.filter().order_by("-id")




def book(request):
    return HttpResponse('book')


# def book_all(request):
#     post = models.Post.objects.all()
#     return render(request, 'post_list.html', {'post': post})


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        book_pk = self.kwargs.get('pk')
        return get_object_or_404(models.Post, pk=book_pk)

# def book_detail(request, pk):
#     book = get_object_or_404(models.Post, pk=pk)
#     return render(request, 'book_detail.html', {'book': book})


class BookCreateView(generic.CreateView):
    template_name = "add_book.html"
    form_class = forms.BookForm
    queryset = models.Post.objects.all()
    success_url = "/add-book/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)



# def add_book(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Book created')
#     else:
#         form = forms.BookForm()
#     return render(request, 'add_book.html', {'form': form})



class BookUpdateView(generic.UpdateView):
    template_name = 'book_update.html'
    form_class = forms.BookForm
    success_url = '/book/'

    def get_object(self, *kwargs):
        book_pk = self.kwargs.get('pk')
        return get_object_or_404(models.Post, pk=book_pk)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)


# def book_update(request, pk):
#     book_object = get_object_or_404(models.Post, pk=pk)
#     if request.method == 'POST':
#         form = forms.BookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse('Book Update Successfully')
#             return redirect(reverse("book:book_all"))
#     else:
#         form = forms.BookForm(instance=book_object)
#     return render(request, 'book_update.html', {'form': form, 'object': book_object})


class BookDeleteView(generic.DeleteView):
    template_name = 'confirm_delete_book.html'
    success_url = '/book/'

    def get_object(self, **kwargs):
        book_pk = self.kwargs.get("pk")
        return get_object_or_404(models.Post, pk=book_pk)


# def book_delete(request, pk):
#     book_object = get_object_or_404(models.Post, pk=pk)
#     book_object.delete()
#     return HttpResponse('Book Delete')

