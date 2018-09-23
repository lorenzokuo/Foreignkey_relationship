from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "authors": Author.objects.all()
        }
    return render(request, "books/index.html", context)

def create(request):
    my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))
    return redirect("/")