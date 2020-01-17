from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader
from p_library.models import Book


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    biblio_data = {"title": "мою библиотеку", "books_count": books_count}
    return HttpResponse(template.render(biblio_data))