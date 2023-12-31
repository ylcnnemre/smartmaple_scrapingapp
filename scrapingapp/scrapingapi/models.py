from django.db import models
from django.utils import timezone
# Create your models here.
class KitapYurdu(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    site = models.CharField(max_length=50)
    numberof_pages = models.CharField(max_length=10)
    isbn = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    book_cover = models.CharField(max_length=20)
    paper_type = models.CharField(max_length=20)
    created = models.DateTimeField(default=timezone.now()+timezone.timedelta(hours=3))
    class Meta:
        db_table = 'kitapyurdu'
    def __str__(self):
        return self.name
    



class KitapSepeti(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    site = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    numberof_pages = models.CharField(max_length=10)
    isbn = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    book_cover = models.CharField(max_length=20)
    paper_type = models.CharField(max_length=20)
    created = models.DateTimeField(default=timezone.now()+timezone.timedelta(hours=3) )
    class Meta:
        db_table = 'kitapsepeti'
    def __str__(self):
        return self.name
    
