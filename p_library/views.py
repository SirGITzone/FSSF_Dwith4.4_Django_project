# coding: utf-8 
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from p_library.models import Book, PublishingHouse


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
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def publishing_house(request):
    template = loader.get_template('publishing_house.html')
    publishing_houses = PublishingHouse.objects.all()
    data = {
        "publishing_houses": publishing_houses,
    }
    return HttpResponse(template.render(data, request))