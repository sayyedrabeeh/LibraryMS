from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author =models.CharField(max_length=255)
    is_availible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrow_date = models.DateField(default=datetime.now)
    return_date =  models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
    
