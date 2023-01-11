from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('', views.getData),
    # path('add/', views.postData),
    # path('edit/<int:id>', views.updateData),
    # path('remove/<int:id>', views.deleteData),
    path('register/', views.RegisterAPI.as_view()),
    path('logout/', views.Logout.as_view()),
    path('token', views.MyTokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('token/verify', TokenVerifyView.as_view())
]
