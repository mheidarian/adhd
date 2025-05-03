from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_list, name='test_list'),
    path('<int:pk>/', views.test_detail, name='test_detail'),
    path('<int:pk>/take/', views.take_test, name='take_test'),
    path('result/<int:result_id>/', views.test_result, name='test_result'),
    path('guide/', views.test_guide, name='test_guide'),
] 