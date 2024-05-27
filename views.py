from django.shortcuts import render, redirect
from .models import Asset, Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

@login_required
def new_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/new_reservation.html', {'form': form})
