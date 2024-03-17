from django.urls import path
from . import views
from .views import delete_job_offer

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/<int:job_offer_id>/', delete_job_offer, name="delete_job_offer"),
]
