import django
print(django.get_version())

##To install --> python -m pip install Django
##To initiate a venv --> python -m venv venv_name
##To activate a venv --> venv/Scripts/Activate


##Starting a Django project --> django-admin startproject project_name
##Para rodar o projeto --> manage.py runserver


"""
Basics Knowledges: 


1. Settings.py:

É um arquivo python que irá conter as configurações que iremos editar no desenvolvimento do projeto, dentro dele, há uma lista chamada
INSTALLED_APPS que contem os apps que fazem o projeto

é perceptível que o Django pré-instala alguns apps comuns, como admin, authentication, sessions e app para manusear static files. Quando
criarmos novos apps, temos que incluí-los nessa lista, para Django saber que existem

Mais afundo em settings.py há um dicionário nomeado DATABASES, Por padrão, Django irá setar uma banco de dados SQLite


2. urls.py:

Aqui estão as declarações de url para o projeto, ou, "table of contents" para o projeto Django. É aqui que o Django tentará dar match com 
algum url. Por padrão, o admin app já tem uma rota pré-setada


3. MIGRATING THE DATABASE:
Quando iniciamos o server, Django nos mostra um erro, dizendo que há unapplied migrations

uma migration é uma mudança no bando de dados pendente, vimos que Django nos dá alguns apps pré-setados, por exemplo, o admin interface usa o banco
de dados, logo, as migrações precisam ser aplicadas ao SQLite Database

Sempre que fazemos alguma mudança ao modelo da database, devemos aplicar essas mudanças rodando python manage.py migrate. Após aplicar as migrações, quando rodamos
o server, os erros se vão


4. Django Apps:
Os apps são submódulos de um projeto, que contém código para uma parte/feature específica. Os apps têm de ser auto-suficiente e na teoria, pode ser pegado e colocado
em outro projeto sem nenhuma modificação. Um Django project refere-se à todo código base e suas partes. A pasta Django Project contém a manage.py e outros módulos que incluem
settings.py

Apps são o que tornam os projetos Django tão escalonáveis. Desde que são totalmente auto-suficientes, eles não se quebram a partir do momento que mais e mais features são
adicionadas à um projeto.

##COMO CRIAR UM APP
## APENAS RODAR O COMANDO --> python manage.py startapp myappname
##É necessário adicionar a existência do app ao root, é necessário ser adicionado à lista e INSTALLED_APPS nas settings.py do projeto


5. Django Views:
São os quebradores de informações em um app, ou seja, decide toda a informação que vai ser mandada para o template e mostrada. Simplificando, as views são classes ou funções que
processam a request e mandam de volta a response

Uma view function deve:
1.Checar se o usuário está logado
2.Dar request da informação do perfil na database
3.Formatar as informações em um template
4.Mandar de volta a página como um arquivo html para o cliente visualizar no browser

Para isso, o Django utiliza o protocolo http, tanto as requests e responses são baseadas nesse protocolo
!Toda view é responsável por retornar um obejto Response. O objeto pode ser elementos HTML, um redirect, error, xml, imagens, ou qualquer coisa que possa ser mostrada na web


6. Using View to send HTML Page:
Django irá olhar em cada app dentro de INSTALLED_APPS por diretórios chamados templates. A melhor prática para estruturar essa pasta é utilizar o método namespace, isso é,
colocar nossas html pages dentro de um diretório que contém o mesmo nome do nosso app

ex:
ex:
myapp/  
└── templates/  
    └── myapp/  
      └── mytemplate.html
      
Com essa organização formada, podemos aplicar a lógica para nossa view function em views.py:
ex:

from django.template import loader
from django.shortcuts import render

def home(request):
    template = loader.get_template("app/home.html")
    return render(request, template)
    
    
7. Wiring up a View:
Na internet, toda página necessita de sua própria URL. Em Django, podemos usar algo chamado URLConf, para a configuração dos urls. Esse módulo é um set de padrãos que Django
irá tentar dar match com o URL requisitado para achar a View correta

A URLConf é localizada em um arquivo chamado urls.py dentro do diretório do app. No topo do urls.py nos importamos o objeto path from django.urls e importamos views from .
e adicionamos rotas

a urls.py vai ficar assim:

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('profile/', views.profile, name="profile")
]

Nota-se que após as importações, há uma lista urlpatterns, que contém as rotas para cada view Function. Cada rota é provida de um objeto path() que contém 3 args:
1. A rota URL como string
2. O nome da função view
3. Nome opcional para referir-se a view

#Quando navegamos para uma URL sem nenhuma rota adicional '', a home() view vai ser chamada. se formos para o url com o final /profile, a view profile()

Para o Django ficar sabendo que a URLConf existe, deve ser inserido dentro das URLSConf do projeto, também chamado urls.py

Por padrão, a urls.py do projeto está assim:

from django.contrib import admin
from django.urls import path
urlpatterns = [
    path("admin/", admin.site.urls),
]

Para incluir as URLConf dos apps, primeiro importamos from django.urls import include, depois adicionamos um path() para urlpatterns:

from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(myapp.urls))
]









"""