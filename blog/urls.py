from django.urls import path
from blog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('test/', views.tested),
    path('art/', views.art, name='art'),
    path('contact/', views.contact, name='contact'),
    path('^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    path('about/', views.about, name='about'),
    path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    path('category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    # path('search/', views.search, name='search'),
]
