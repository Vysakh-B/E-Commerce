from django.urls import path
from . import views

urlpatterns = [
    path('shop_men',views.men,name='men'),
    path('shop_women',views.women,name='women'),
    path('add_cart/<int:id>/',views.add_cart,name='add_cart'),
    path('cart',views.carts,name='cart'),
    path('cart/<int:id>/<str:data>/',views.change,name='change'),
    path('cart/<int:id>/',views.remove,name='remove-cart'),
    path('checkout',views.checkout,name='checkout'),
    path('thankyou',views.thankyou,name='thankyou'),
    path('profile',views.profile,name='profile'),
    path('shop-single/<int:id>/',views.single,name='shop_single'),

]