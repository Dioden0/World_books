from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre


def index(request):
    return HttpResponse("Главная страница мир книг")


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status_exact=2).count()
    num_authors = Author.objects.count()

    return render(request, 'base_generic.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instaces_available,
                           'num_authors': num_authors,
                           'num_visits': num_visits},
                  )

