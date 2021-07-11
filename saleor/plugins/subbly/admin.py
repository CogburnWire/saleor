from django.contrib import admin

from .models import SubblySubscription


@admin.register(SubblySubscription)
class SubblySubscriptionAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "subscription_id", "invite_code", "created")
