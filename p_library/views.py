# coding: utf-8 
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader
from p_library.models import Book


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)



# def index(request):
#     template = loader.get_template('index.html')
#     books_count = Book.objects.all().count()
#     books = Book.objects.all()
#     biblio_data = {
#         "title": "мою библиотеку",
#         "books_count": books_count,
#         "books": books,
#     }
#     return HttpResponse(template.render(biblio_data))


def index(request):
    list_from_1_to_100 = list(range(1,100))
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "digits": list_from_1_to_100
    }
    return HttpResponse(template.render(biblio_data))