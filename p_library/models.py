from django.db import models

# Create your models here.


from django.db import models  
  
  
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class PublishingHouse(models.Model):  
    apellation = models.CharField(max_length=100) 

    def __str__(self):
        return self.apellation 

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(null = True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE, blank=True, null=True, related_name='books')
    # В переменной publishing_house указано, что наличие связи необязательно, так как издательств у нас изначально нет и мы будем добавлять их

    def __str__(self):
        return self.title




