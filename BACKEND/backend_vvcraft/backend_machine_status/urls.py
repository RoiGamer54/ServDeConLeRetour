from django.urls import path
from .views import MachineStatusView

urlpatterns = [
    path('api/machine/status/', MachineStatusView, name='machine_status'),
]
