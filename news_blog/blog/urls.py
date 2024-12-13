from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsView.as_view()),
    path('<int:pk>/', views.Post_DetailView.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    #path('', views.get_weather)
]