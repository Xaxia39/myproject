from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Category, Book
from .forms import AuthorForm, CategoryForm, BookForm, SearchForm

def home(request):
    return render(request, 'myapp/home.html')

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'myapp/add_author.html', {'form': form})

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'myapp/add_category.html', {'form': form})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'myapp/add_book.html', {'form': form})

def search(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)
            return render(request, 'myapp/search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'myapp/search.html', {'form': form})
