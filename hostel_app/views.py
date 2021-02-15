
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Reservation, Room, Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .forms import ReservForms


@login_required #Проверка на вход пользователя
def index(request):

    rooms = Room.objects.all()
    categorys = Category.objects.all()
    reservations = Reservation.objects.all()

    
    if request.method == "POST":
        form = ReservForms(request.POST)

        for cat in categorys:
          form.filter(cat.id)
          cat.reservation = form

        if form.is_valid():
          reserv = form.save(commit=False)
          reserv.client = Profile.objects.get(user = request.user)
          form.save()
          return HttpResponse("Забронированно")
        else:
          #return HttpResponse("Ошибка")
          return render(
          request,
          'index.html',
          context={'rooms':rooms, 'categorys':categorys, 'reservations':reservations},
        )     

    else:
        for cat in categorys:
          r = ReservForms()
          r.filter(cat.id)
          cat.reservation = r
        return render(
        request,
        'index.html',
        context={'rooms':rooms, 'categorys':categorys, 'reservations':reservations},
        )

@login_required #Проверка на вход пользователя
def profile(request):
    reservations = Reservation.objects.all()
    return render(
        request,
        'profile.html',
        context={'reservations':reservations},
    )

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      return render(request, 'signup.html', {'form': form,})
  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form,})


def aboutus(request):
    
    return render(
        request,
        'aboutus.html',
        context={},
    )

