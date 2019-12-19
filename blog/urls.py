from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns =[
    path('blog', views.blog, name='blog'),
    # path('blog/<int:pk>/<slug:slug>/', views.civil_law_detail, name='civil_law_detail'),
    # path('blog/<int:pk>/<slug:slug>/', views.criminal_law_detail, name='criminal_law_detail'),
    # path('blog/<int:pk>/<slug:slug>/', views.family_law_detail, name='family_law_detail'),
    # path('blog/<int:pk>/<slug:slug>/', views.writs_detail, name='writs_detail'),
    # path('blog/<int:pk>/<slug:slug>/', views.labour_laws_detail, name='labour_laws_detail'),
    # path('blog/<int:pk>/<slug:slug>/', views.service_matters_detail, name='service_matters_detail'),
    # path('blog/<int:pk>/<slug:slug>/', views.consumer_matters_detail, name='consumer_matters_detail'),
    # path('blog/<int:pk>/<slug:slug>/', views.immigrations_detail, name='immigrations_detail'),
    # path('blog/<int:pk>/<slug:slug>/', views.consultants_detail, name='consultants_detail'),
    path('blog/<int:pk>/<slug:slug>/', views.popular_blog_detail, name='popular_blog_detail'),
    path('blog/<int:pk>/<slug:slug>/', views.latest_blog_detail, name='latest_blog_detail'),
    path('blog/<int:pk>/<slug:slug>/', views.detail_page, name='detail_page'),
]