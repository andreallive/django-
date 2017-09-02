from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=1000)
    contenido=models.TextField()
    fecha_creaciacion=models .DateTimeField(default=timezone.now)
    fecha_publicacion=models.DateTimeField(blank=True , null=True )
    autor=models.ForeignKey('auth.User')

    def __str__(self):
        return self.titulo

    def publicar(self):
        self.fecha_publicacion=timezone.now()
        self.save()
