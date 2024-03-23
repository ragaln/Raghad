from django.urls import path, re_path
#import clubs views
from clubs import views



urlpatterns = [    
    path('', views.index, name='index'),
    path('clubs/', views.clubs,name="clubs"),
    path('contact/',views.contactus,name="contactus"),
    path('clubs/<int:cId>', views.club),
    path('clubs/filter',views.filter,name="filter"),
    path('filter_clubs/', views.filter_clubs, name='filter_clubs'),

]