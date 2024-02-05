from django.db import models

class Links(models.Model):
       link_redirecionado = models.URLField()
       link_encurtado = models.CharField(max_length= 20)
       link_avatar = models.CharField(max_length= 20)
       visualizacoes = models.PositiveIntegerField(default=0)
       origem = models.CharField(max_length=255, blank=True, null=True)

       def __str__(self) -> str:
              return self.link_encurtado
