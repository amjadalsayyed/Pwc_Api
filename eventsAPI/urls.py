from django.urls import path
from eventsAPI import views 

urlpatterns = [
    path('list/<str:country>/', views.get_events_in_country),
    path('weather/<str:eventid>/', views.get_event_wehather),
    path('flights/<str:eventid>/<str:user_airport_code>/', views.get_flight_list),
]