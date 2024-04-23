from django.db.models import Q, Count
from django.shortcuts import render, redirect
from .models import Club

def clubs(request):
    all_clubs = Club.objects.select_related('sport').all()
    context = {'clubs': all_clubs}
    return render(request, 'clubsmodule/clubList.html', context)

def club(request, cId):
    try:
        targetClub = Club.objects.select_related('sport').get(id=cId)
    except Club.DoesNotExist:
        return redirect('/clubs')
    context = {'club': targetClub}
    return render(request, 'clubsmodule/club.html', context)

def index(request):
    return render(request, 'clubsmodule/index.html')

def contactus(request):
    return render(request, 'clubsmodule/contact.html')

def filter(request):
    return render(request, 'clubsmodule/filter.html')



def filter_clubs(request):
    name_query = request.GET.get('name', '')
    sport_query = request.GET.get('sport', '')
    order_query = request.GET.get('order', 'name')  # Assume we want to allow ordering

    # Building the initial query with Q objects
    query = Q()
    if name_query:
        query &= Q(name__icontains=name_query)
    if sport_query:
        query &= Q(sport__name=sport_query)
    
    clubs = Club.objects.filter(query).order_by(order_query)  # Ordering by the 'order' parameter


    context = {'clubs': clubs}
    return render(request, 'clubsmodule/clubList.html', context)

