from django.urls import path
from .views import StudentList, StudentDetail

urlpatterns = [
    path('', StudentList.as_view()),
    path('<int:pk>/', StudentDetail.as_view()),
]
