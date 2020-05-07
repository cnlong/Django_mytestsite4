from django.urls import path,re_path
from booktest import views

urlpatterns = [
    path('static_test', views.static_test),
    path('index', views.index),
    path('upload_pic', views.upload_pic),
    path('upload_handle', views.upload_handle),
    # path('show_areas<int:pindex>', views.show_area),
    re_path(r'^show_areas(?P<pindex>\d*)$', views.show_area),
    path('areas', views.areas),
    path('prov', views.prov),
    re_path(r'^city(\d+)$', views.city),
    re_path(r'^dis(\d+)$', views.dis),
    path('set_session', views.set_session),
    path('get_session', views.get_session),
]
