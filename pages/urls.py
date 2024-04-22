from django.urls import path
from pages.views import HomeView, AboutView, AdmissionView, ApplyOnlineView, ContactView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('admission/', AdmissionView.as_view(), name='admission'),
    path('apply_online/', ApplyOnlineView.as_view(), name='apply_online'),
    path('contact/', ContactView.as_view(), name='contact'),
]
