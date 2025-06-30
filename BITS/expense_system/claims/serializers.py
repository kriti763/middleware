from rest_framework import serializers
from .models import Centre, ExpenseClaim, ClaimItem

class ClaimItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimItem
        fields = '__all__'

class ExpenseClaimSerializer(serializers.ModelSerializer):
    items = ClaimItemSerializer(many=True, required=False)

    class Meta:
        model = ExpenseClaim
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        claim = ExpenseClaim.objects.create(**validated_data)
        for item_data in items_data:
            ClaimItem.objects.create(claim=claim, **item_data)
        return claim

class CentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centre
        fields = '__all__'
