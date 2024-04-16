from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import Film
from django.template import loader
from zai.forms import FilmForm
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Użytkownicy': reverse('ListaUzytkownikow', request=request, format=format),
        'Wszystkie filmy': reverse('ListaFilmow', request=request, format=format),
        'Informacje dodatkowe': reverse('InformacjeDodatkowe', request=request, format=format),
        'Wszystkie oceny': reverse('Recenzje', request=request, format=format),
        'Wszyscy aktorzy': reverse('Aktorzy', request=request, format=format),
    })


def wszystkie(request):
    template = loader.get_template("filmy/wszystkie.html")
    wszystkie_filmy = Film.objects.all()
    context = {'wszystkie_filmy': wszystkie_filmy, }
    return HttpResponse(template.render(context, request))


def szczegoly(request, film_id):
    template = loader.get_template("filmy/szczegoly.html")
    film = Film.objects.get(id=film_id)
    context = {'film': film}
    return HttpResponse(template.render(context, request))


def nowy(request):
    nowyform = FilmForm(request.POST or None)
    if nowyform.is_valid():
        nowyform.save()
        return redirect(wszystkie)
    return render(request, 'filmy/c.html', {'nowyform': nowyform})


def edycja(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    form = FilmForm(request.POST or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'filmy/u.html', {'form': form})


def usun(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method == "POST":
        film.delete()
        return redirect(wszystkie)
    return render(request, 'filmy/usun.html', {'film': film})
