import uuid

from django.db import models


class SubblySubscription(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    subscription_id = models.CharField(max_length=255)
    invite_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["subscription_id"], name="unique_subscription"
            ),
            models.UniqueConstraint(fields=["email"], name="unique_email",),
        ]

    def __str__(self):
        return format(self.email)
