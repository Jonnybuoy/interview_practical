from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import get_routes, get_accounts, deposits_view, withdrawals_view, transaction_view

urlpatterns = [
    path('', get_routes),
    path('accounts/', get_accounts),
    path('deposits/', deposits_view),
    path('withdrawals/', withdrawals_view),
    path('transactions/', transaction_view),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]
