from django.db.models import Q, Count
from django.shortcuts import render, redirect

from .forms import ClubForm
from .models import Club, Sport
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clubs')  
    else:
        form = ClubForm()
    return render(request, 'clubsmodule/clubForm.html', {
        'title': 'Add Club', 'button_text': 'Add', 'form': form
    })
@csrf_exempt
def update_club(request, cId):
    club = Club.objects.get(id=cId)
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            if 'image' in request.FILES:
                if club.image:
                    default_storage.delete(club.image.path)
            form.save()
            return redirect('club_details', cId=club.id)
    else:
        form = ClubForm(instance=club)
    return render(request, 'clubsmodule/clubForm.html', {
        'club': club, 'title': 'Update Club', 'button_text': 'Update', 'form': form
    })
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
    order_query = request.GET.get('order', 'name') 
    # Building the initial query with Q objects
    query = Q()
    if name_query:
        query &= Q(name__icontains=name_query)
    if sport_query:
        query &= Q(sport__name=sport_query)
    
    clubs = Club.objects.filter(query).order_by(order_query) 


    context = {'clubs': clubs}
    return render(request, 'clubsmodule/clubList.html', context)

