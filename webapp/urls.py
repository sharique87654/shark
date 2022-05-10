from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index , name='home'),
    path('about' , views.about , name='about'),
    path('contact' , views.contact , name='contact'),
    path('login' , views.login , name= 'login'),
    path('signup' , views.signup , name= 'signup'),
    path('logout' , views.logout , name= 'logout'),
    path('homelog' , views.homelog , name= 'homelog'),
    path('info' , views.info , name= 'info')



]
