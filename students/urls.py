from django.urls import path
from students.views import (
    StudentListView, StudentCreateView, StudentDetailView, StudentUpdateView,
    StudentDeleteView, StudentExportView
)


urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('new/', StudentCreateView.as_view(), name='new'),
    path('<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='delete'),
    path('export/', StudentExportView.as_view(), name='export')
]
