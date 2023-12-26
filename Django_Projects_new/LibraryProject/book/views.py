from django.shortcuts import render, HttpResponse ,  redirect
from .models import Book
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def welcome(request):
    books = Book.objects.all()
    return render(request, "home.html", {"all_books": books})

def create_book(request):
    if request.method == "GET":
        return render(request, "createbook.html")
    elif request.method == "POST":
        
        data = request.POST
        if not data.get("id"):
            Book.objects.create(title=data.get("title"), author=data.get("auth"),
                            pulication_date=data.get("pub_date"), price=data.get("prc"))
        else:
            book_obj = Book.objects.get(id=data.get("id"))
            book_obj.title = data.get("title")
            book_obj.author = data.get("auth")
            book_obj.pulication_date = data.get("pub_date")
            book_obj.price = data.get("prc")
            book_obj.save()

        return redirect("home")
    
    

def edit_book(request, bid):
    try:
        book_obj = Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    else:
        return render(request, "createbook.html", {"book": book_obj})
    
def delete_book(request, bid):
    try:
        book_obj = Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    else:
        #hard delete book_obj.delete() #hard delete
        if request.POST.get("type_of_delete") == "HardDelete":
            book_obj.delete()
        else:
            book_obj.isdeleted = True # soft delete
            book_obj.save()
        return redirect("home")
    
def show_deleted_books(request):
    deleted_books = Book.objects.filter(isdeleted=True)
    return render(request, "deleted_books.html", {"deleted_books": deleted_books})

def restore_book(request, bid):
    try:
        book_obj = Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    else:
        #hard delete book_obj.delete() #hard delete
        book_obj.isdeleted = False # soft delete
        book_obj.save()
        return redirect("home")