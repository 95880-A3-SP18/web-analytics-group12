from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('distribution', views.distribution, name='distribution'),
    path('bedroom', views.bedroom, name='bedroom'),
    path('predictform', views.PredictForming, name='PredictForm'),  ##
    path('timeseries', views.timeseries, name='timeseries'),
    path('distance', views.distance, name='distance'),
    path('Post', views.PostView.as_view(), name='PostView'),
    path('post', views.post, name='post'),
]
