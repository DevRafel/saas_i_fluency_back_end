from django.db import models

class Links(models.Model):
       link_redirecionado = models.URLField()
       link_encurtado = models.CharField(max_length= 8)
       visualizacoes = models.PositiveIntegerField(default=0)

       def __str__(self) -> str:
              return self.link_encurtado
