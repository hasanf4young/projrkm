from django.urls import path
from . import views

urlpatterns = [
   path('vdata/', views.vdata, name='vdata'),
   path('vtable/', views.tbdata, name='vtable'),

]

