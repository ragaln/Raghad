from django.urls import path, re_path
#import clubs views
from clubs import views



urlpatterns = [    
    path('', views.index, name='index'),
    path('clubs', views.clubs),
    path('clubs/<int:cId>', views.club)
]