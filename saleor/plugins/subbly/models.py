import uuid

from django.db import models


class SubblySubscription(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    subscription_id = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True)
    invite_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return format(self.email)
