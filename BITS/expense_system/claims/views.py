from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Centre, ExpenseClaim, ClaimItem
from .serializers import CentreSerializer, ExpenseClaimSerializer, ClaimItemSerializer

class CentreViewSet(viewsets.ModelViewSet):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer

class ExpenseClaimViewSet(viewsets.ModelViewSet):
    queryset = ExpenseClaim.objects.all()
    serializer_class = ExpenseClaimSerializer

class ClaimItemViewSet(viewsets.ModelViewSet):
    queryset = ClaimItem.objects.all()
    serializer_class = ClaimItemSerializer