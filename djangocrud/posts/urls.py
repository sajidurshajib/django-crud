from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatters = [
    path('', views.PostAPI.as_view()),
    path('catagories/', views.CatagoryAPI.as_view()),
    path('catagories/<int:pk>', views.CatagoryDetailAPI.as_view()),
    path('tags/', views.TagAPI.as_view()),
    path('tags/<int:pk>', views.TagDetailAPI.as_view())
]

urlpatterns = format_suffix_patterns(urlpatters)
