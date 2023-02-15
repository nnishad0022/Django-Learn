from django.urls import path
from . import views
urlpatterns = [
    path('',views.page1,name="homepage" ),
    path('two/',views.page2,name="p2" ),
    path("3/",views.html_page,name="Template"),
    path("4/",views.p2,name="Template"),
    # path("5/",views.p3,name="table"),
    path("6/", views.p6),
    path("7/",views.join,name="form"),
    ]
