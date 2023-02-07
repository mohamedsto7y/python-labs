from django.urls import path
from . import views

urlpatterns = [
    #path('login/',views.login1,name='login'),
    path('login/',views.Loginview.as_view(),name='login'),
    path('logout/', views.logout1, name='logout'),
    path('register/', views.register1, name='register'),
    path('list/', views.List.as_view(), name='list'),

]


