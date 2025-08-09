from django.db import models

# Create your models here.
# Mi clase es un modelo,donde voy a definir los atributos
class PostGeneral(models.Model):
    # Los tipos de atributos son CharField (caracter)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Titulo:" + self.title + "- Fecha"+str(self.created_at)