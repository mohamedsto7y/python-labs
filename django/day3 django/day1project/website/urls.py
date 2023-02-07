from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'home'),
    path('culture/', views.culture, name = 'culture'),
    path('culture/<int:tID>', views.culture_topic, name = 'culturetopic'),
    path('blogs/', views.listBlogs, name = 'list'),
    path('blogs/<int:id>', views.spBlog, name = 'sp_blog'),
    path('blogs/add', views.addBlog, name='add_blog'),
    path('blogs/<int:id>/edit', views.editBlog, name = 'edit_blog'),
    path('blogs/<int:id>/delete', views.delBlog, name = 'delete_blog'),

]


