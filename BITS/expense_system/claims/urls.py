from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CentreViewSet, ExpenseClaimViewSet, ClaimItemViewSet

router = DefaultRouter()
router.register(r'centres', CentreViewSet)
router.register(r'expense-claims', ExpenseClaimViewSet)
router.register(r'claim-items', ClaimItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Additional paths can be added here if needed
]