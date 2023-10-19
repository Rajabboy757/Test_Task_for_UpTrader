from django.urls import path
from trader import views


urlpatterns = [
    path('menu/<int:menu_id>/', views.show_menu, name='menu'),
]
