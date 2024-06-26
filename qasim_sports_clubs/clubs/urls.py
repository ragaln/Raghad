from django.urls import path, re_path
#import clubs views
from clubs import views



urlpatterns = [    
    path('', views.index, name='index'),
    path('clubs/', views.clubs,name="clubs"),
    path('contact/',views.contactus,name="contactus"),
    path('clubs/<int:cId>', views.club,name="club_details"),
    path('clubs/filter',views.filter,name="filter"),
    path('clubs/addClub',views.add_club,name="add_club"),
    path('clubs/edit_club/<int:cId>',views.update_club,name="edit_club"),
    path('filter_clubs/', views.filter_clubs, name='filter_clubs'),
    path('delete_club/<int:cId>', views.delete_club, name='delete_club'),

]