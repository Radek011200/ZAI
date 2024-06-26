"""
URL configuration for zai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import wszystkie, szczegoly, nowy, edycja, usun
# from film.views import FilmList, FilmRetrieve, FilmCreateList
from main.views import api_root
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    path("graphql", jwt_cookie(GraphQLView.as_view(graphiql=True))),
    path('admin/', admin.site.urls),
    path('wszystkie/', wszystkie),
    path('szczegoly/<int:film_id>/', szczegoly),
    path('nowy/', nowy),
    path('edycja/<int:film_id>/', edycja),
    path('usun/<int:film_id>/', usun),
    path('filmy/', include('film.urls')),
    path('', api_root)
]
