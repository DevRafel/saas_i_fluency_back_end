from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormLinks
from .models import Links
from django.shortcuts import redirect
import instaloader

# Create your views here.

def home(request):
       form = FormLinks()
       status = request.GET.get('status')
       return render(request, 'home.html', {'form': form, 'status': status})

def valida_link(request):
       form = FormLinks(request.POST)

       link_encurtado = form.data['link_encurtado']
       links = Links.objects.filter(link_encurtado = link_encurtado)
       if len(links) > 0:
              return redirect("/?status=1")

       if form.is_valid():
              try:
                     link_obj = form.save(commit=False)
                     link_obj.visualizacoes = 0                 
                     
                     origem = request.GET.get('origem', 'desconhecida')
                     link_obj.origem = origem
                     
                     link_obj.save()
                     return HttpResponse(f"Seu link foi criado e é: http://127.0.0.1:8000/{link_encurtado}" )
              except:
                     return HttpResponse("erro do sistema")
              
       return HttpResponse(f"Erro na criação do link: /{link_encurtado}")
              

def redirecionar(request, link):
       links = Links.objects.filter(link_encurtado = link)
       if len(links) == 0:
              return redirect('/')
       
       link_obj = links[0]
       link_obj.visualizacoes += 1
       link_obj.save()
       
       return redirect(link_obj.link_redirecionado)



def pegaravatar(request):
       form = FormLinks(request.POST)
       
       link_encurtado = form.data['link_encurtado']
       links = Links.objects.filter(link_encurtado = link_encurtado)
       
       profile_name = links
       
       dp = instaloader.Instaloader()

       dp.download_profile(profile_name, profile_pic_only=True)