from django.db.models import fields
from rest_framework import serializers
from .models import Events


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('coin_id', 'target_price', 'alert_trigger_count',
                  'owner', 'active', 'created_at', 'updated_at')
        read_only_fields = ['owner', 'active', 'alert_trigger_count']
