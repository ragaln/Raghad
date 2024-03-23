from django.shortcuts import redirect, render

# Create your views here.
# it is about qasim sports clubs

def __getClubs():
    return [
        {'id': 1, 'name': 'Al-Qasim Football Club', 'sport': 'Football', 'location': 'Qasim Stadium', 'image': 'images/football.jpg'},
        {'id': 2, 'name': 'Al-Qasim Tennis Club', 'sport': 'Tennis', 'location': 'Qasim Tennis Courts', 'image': 'images/tennis.jpg'},
        {'id': 3, 'name': 'Al-Qasim Basketball Club', 'sport': 'Basketball', 'location': 'Qasim Sports Arena', 'image': 'images/basketball.jpg'}
    ]



def index(request):
    # This view returns the index page for Qasim Sports Clubs
	return render(request, 'clubsmodule/index.html')

def clubs(request):
    # This view returns the clubs list page for Qasim Sports Clubs
    all_clubs = __getClubs()
    context = {'clubs': all_clubs}
    return render(request, 'clubsmodule/clubList.html', context)
def contactus(request):
    # This view returns the contact us page 
    return render(request, 'clubsmodule/contact.html')

def club(request, cId):
    # This view returns the details of a specific club for Qasim Sports Clubs
    
    club1 = {'id':12344321, 'name':'Football Club', 'location':'Stadium A'}
    club2 = {'id':56788765, 'name':'Tennis Club', 'location':'Court B'}
    
    targetClub = None
    if club1['id'] == cId: targetClub = club1
    if club2['id'] == cId: targetClub = club2
    
    if targetClub == None: return redirect('/clubs')
    
    context = {'club':targetClub} # 'club' is the variable name accessible by the template
    return render(request, 'clubsmodule/club.html', context)

def filter(request):
    return render(request, 'clubsmodule/filter.html')

def filter_clubs(request):
    clubs = __getClubs()
    name_query = request.GET.get('name', '')
    sport_query = request.GET.get('sport', '')

    if name_query:
        clubs = [club for club in clubs if name_query.lower() in club['name'].lower()]
    if sport_query:
        clubs = [club for club in clubs if club['sport'] == sport_query]

    context = {'clubs': clubs}
    return render(request, 'clubsmodule/clubList.html', context)
