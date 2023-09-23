from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:id>/',views.product,name="product"),
    path('sub',views.about,name="about"),
    path('shop',views.shop,name="shop"),
    path('signup',views.signup,name="register"),
    path('login',views.login,name="signin"),
    path('logout',views.logout,name="logout"),
    path('contact',views.contact,name="contact")


]