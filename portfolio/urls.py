from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns =[
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail')
]