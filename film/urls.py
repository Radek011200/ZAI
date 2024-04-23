from .views import FilmCreateList, FilmRetrieveUpdateDestroy,  ExtraInfoCreateList, ExtraInfoRetrieveUpdateDestroy, \
    OcenaCreateList, OcenaRetrieveUpdateDestroy, AktorCreateList, AktorRetrieveUpdateDestroy, \
    UserCreateList, UserRetrieveUpdateDestroy, statRezyserLiczbaFilmow, statFilmyLiczbaOcen, statFilmyBezOcen, \
    statFilmyKategorieDobrySlaby, statFilmyGwiazdkiMaxMin
from django.urls import path

urlpatterns = [
    path('filmy/', FilmCreateList.as_view(), name= 'ListaFilmow'),
    path('filmy/<int:pk>/', FilmRetrieveUpdateDestroy.as_view(), name= 'FilmRetrieveUpdateDestroy'),
    path('extrainfo/', ExtraInfoCreateList.as_view(), name='InformacjeDodatkowe'),
    path('extrainfo/<int:pk>/',ExtraInfoRetrieveUpdateDestroy.as_view(), name='ExtraInfoRetrieveUpdateDestroy'),
    path('ocena/', OcenaCreateList.as_view(), name='Recenzje'),
    path('ocena/<int:pk>/',OcenaRetrieveUpdateDestroy.as_view(), name='OcenaRetrieveUpdateDestroy'),
    path('aktor/', AktorCreateList.as_view(), name='Aktorzy'),
    path('aktor/<int:pk>/', AktorRetrieveUpdateDestroy.as_view(), name='AktorRetrieveUpdateDestroy'),
    path('user/', UserCreateList.as_view(), name='ListaUzytkownikow'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='UserRetrieveUpdateDestroy'),
    path('statRezyserLiczbaFilmow/', statRezyserLiczbaFilmow.as_view(), name='statRezyserLiczbaFilmow'),
    path('statFilmyLiczbaOcen/', statFilmyLiczbaOcen.as_view(), name='statFilmyLiczbaOcen'),
    path('statFilmyBezOcen/', statFilmyBezOcen.as_view(), name='statFilmyBezOcen'),
    path('statFilmyDobrySlaby/', statFilmyKategorieDobrySlaby.as_view(), name='statFilmyKategorieDobrySlaby'),
    path('statFilmyGwiazdkiMaxMin/', statFilmyGwiazdkiMaxMin.as_view(), name='statFilmyGwiazdkiMaxMin'),

]