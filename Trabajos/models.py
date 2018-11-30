from django.db import models

# Create your models here.

class Trabajo(models.Model):
    title = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    link = models.URLField(verbose_name="Direccionar a otro sitio", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
    
    def Work(self):
        cadena = "{0}, [ created: {1} ]"
        return cadena.format(self.title, self.created)

    def __str__(self):
        return self.Work()