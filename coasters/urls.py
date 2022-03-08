from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('coasters/', views.coasters, name='coasters'),
  path('coasters/<int:id>/', views.coaster, name='coaster'),
  path('csv-upload', views.csv_upload, name='csv-upload')
]