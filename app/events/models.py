from django.db import models
from authentication.models import User

class Events(models.Model):

    coin_id = models.CharField(max_length=255)
    target_price = models.BigIntegerField()
    alert_trigger_count = models.IntegerField(default=0)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, editable=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.owner+"_"+self.coin_id+"_"+self.target_price)
