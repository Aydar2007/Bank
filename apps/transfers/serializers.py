from rest_framework import serializers

from .models import Transfers

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfers
        fields = ('id', 'who_transfer', 'who_get','is_completed', 'created', 'how_much')