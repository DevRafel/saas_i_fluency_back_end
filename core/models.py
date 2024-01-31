from django.db import models

class Links(models.Model):
       link_redirecionado = models.URLField()
       link_encurtado = models.CharField(max_length= 8)

       def __str__(self) -> str:
              return self.link_encurtado

# Foi passa do dia todo tentado fazer um contador de clicks para saber quantas pessoas assesou o link mais não consegui essa merda fica dando erro toda hora merda