from django.shortcuts import redirect, render
from .models import Club, Sport

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

    if name_query and sport_query:
        clubs = Club.objects.filter(name__icontains=name_query, sport__name=sport_query)
    elif name_query:
        clubs = Club.objects.filter(name__icontains=name_query)
    elif sport_query:
        clubs = Club.objects.filter(sport__name=sport_query)
    else:
        clubs = Club.objects.all()

    context = {'clubs': clubs}
    return render(request, 'clubsmodule/clubList.html', context)
