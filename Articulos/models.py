from django.db import models

# Create your models here.

class Articulo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField( )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
    
    def Article(self):
        cadena = "{0} created: {1}"
        return cadena.format(self.title, self.created)

    def __str__(self):
        return self.Article()
