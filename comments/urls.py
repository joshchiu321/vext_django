from django.urls import path
from .views import comment_view,most_commented_stations,most_commented_stations_page


urlpatterns = [
    path('list_comment', comment_view, name='comment_view'),

    path('most-commented-stations/', most_commented_stations_page, name='most_commented_stations_page'),
    path('data/most-commented-stations-data/', most_commented_stations, name='most_commented_stations_data'),
]
