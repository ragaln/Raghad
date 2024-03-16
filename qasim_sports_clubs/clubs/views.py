from django.shortcuts import redirect, render

# Create your views here.
# it is about qasim sports clubs




def index(request):
    # This view returns the index page for Qasim Sports Clubs
	return render(request, 'clubsmodule/index.html')

def clubs(request):
    # This view returns the clubs list page for Qasim Sports Clubs
    return render(request, 'clubsmodule/clubList.html')
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
