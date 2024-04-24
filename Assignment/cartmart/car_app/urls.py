from django.urls import path
from car_app.views import AddCreateView,CarDetailsView

urlpatterns = [
    path('add_car/', AddCreateView.as_view(), name='add_car' ),
    path('car_details/<int:pk>/', CarDetailsView.as_view(), name='car_details' )
]