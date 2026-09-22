from django.urls import path
from .views import PortfolioView, execute_command

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioView.as_view(), name='home'),
    path('execute-command/', execute_command, name='execute_command'),
]