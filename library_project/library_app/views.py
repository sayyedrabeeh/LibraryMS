from django.shortcuts import render,redirect
from .models import Book,BorrowRecord
from datetime import datetime
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    books = Book.objects.all()
    return render(request,'home.html',{"books":books})

@login_required
def borrow_book(request,book_id):
    book= Book.objects.get(id=book_id)
    if book.is_availible:
          BorrowRecord.objects.create(user=request.user,book=book)
          book.is_availible = False
          book.save()
    return redirect('home')

@login_required
def return_book(request,record_id):
    record = BorrowRecord.objects.get(id=record_id)
    record.return_date = datetime.now()
    record.book.is_availible = True
    record.book.save()
    record.save()
    return redirect('home')

@login_required
def my_books(request):
     records=BorrowRecord.objects.filter(user=request.user)
     return render(request,'my_books.html',{'records':records})


@staff_member_required
def add_book(request):
     if request.method == 'POST':
           title = request.POST.get('title')
           author = request.POST['author']
           image = request.FILES.get('image')
           print("image",image) 
           Book.objects.create(title=title, author=author, image=image)
           return redirect('home')
     return render(request, 'add_book.html')

@staff_member_required
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
