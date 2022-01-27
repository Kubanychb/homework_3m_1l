from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.title




class BookComment(models.Model):
    book = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="book_comment")
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.book.title


class ExpertRecommendation(models.Model):
    books = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="expert+")
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True, null=True)
    information = models.CharField(max_length=100, null=True)
    activity = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.books.title