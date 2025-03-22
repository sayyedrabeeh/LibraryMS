from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('borrow/<int:book_id>/',views.borrow_book,name='borrow_book'),
    path('return/<int:record_id>/',views.return_book,name='return_book'),
    path('my_books/',views.my_books,name='my_books'),
    path('add-book/', views.add_book, name='add_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'), 
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]