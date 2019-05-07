from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GameResultList, GameResultDetail, UserAPI


urlpatterns = [
    path('results/', GameResultList.as_view()),
    path('result/<int:pk>/', GameResultDetail.as_view()),
    path('user/', UserAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
