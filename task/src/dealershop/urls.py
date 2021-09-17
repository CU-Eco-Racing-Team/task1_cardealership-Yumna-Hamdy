from django.urls import path, include
from . import views


urlpatterns = [
    path('views/Add_Dealer', views.Add_Dealer, name='Add_Dealer'),
    path('views/Edit_Dealer/<int:SSN>', views.Edit_Dealer, name='Edit_Dealer'),
    path('views/Promote_Dealer/<int:SSN>', views.Promote_Dealer, name='Promote_Dealer'),
    path('views/Add_Car/<int:SSN>/<str:Name>', views.Add_Car, name='Add_Car'),
    path('views/Add_Industry', views.Add_Industry, name='Add_Industry'),
    path('views/Add_Customer/<int:id>', views.Add_Customer, name='Add_Customer'),
    path('views/Sell_Car/<int:id>/<int:SSN>', views.Sell_Car, name='Sell_Car'),
]