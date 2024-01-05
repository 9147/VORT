from django.urls import path, include
from .views import *
app_name = 'MainApp'

urlpatterns = [
    path('', home,name='home'),
    path('upload/',file_upload_view,name='file_upload'),
    path('logout/',logoutPage,name='logout'),
    path('signin/',signin,name='signin'),
    path('login/',loginMe,name='login'),
    path('addhash/',addhash,name='AddHash'),
    path('gethash/',gethash,name='GetHash')
]