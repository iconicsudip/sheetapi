from django.urls import path
from api import views
urlpatterns = [
    path('sheetdata/<str:code>',views.sheetdata,name='projects'),
]