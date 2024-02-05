from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormLinks
from .models import Links
from django.shortcuts import redirect
import instaloader
from instaloader.exceptions import ProfileNotExistsException

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
                     
                     #Capturar o valor do link_avatar
                     link_avatar = form.cleaned_data['link_avatar']
                     
                     
                     # Definir um valor padrão para o link_avatar
              
                     
                     link_avatar_default = 'xxpaelxx'
                     
                     # Verificar se o link_avatar é válido
                     
                     if not link_avatar:
                            link_avatar = link_avatar_default
                     
                     
                     #Atualizar o perfil_name com o valor do link_avatar
                     profile_name = link_avatar
                     
                     
                     #Baixar a avatar usando instadloader
                     dp = instaloader.Instaloader()
                     try:
                        dp.download_profile(profile_name, profile_pic_only=True)    
                     except ProfileNotExistsException:
                            print(f"Erro ao baixar avatar: {e}")
                            profile_name = link_avatar_default
                            dp.download_profile(profile_name, profile_pic_only=True)
                            
                     link_obj.save()
                     return HttpResponse(f"Seu link foi criado e é: http://127.0.0.1:8000/{link_encurtado}  || Link do avatar : {link_avatar} ||" )
              except Exception as e:
                     print(f"Erro: {e}")
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
