from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('newshow_page', views.newshow_page),
    path('addshow', views.addshow),
    path('showinfo/<int:showId>', views.showinfo),
    path('showedit/<int:showId>', views.display_editshow),
    path('editshow/<int:showId>', views.editshow),
    path('deleteshow/<int:showId>', views.deleteshow)
    
    
]