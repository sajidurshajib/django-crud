from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ProductAPI.as_view()),
    path('<int:pk>', views.ProductAPIDetail.as_view()),
    path('all/', views.custom_msg)

]


urlpatterns = format_suffix_patterns(urlpatterns)
