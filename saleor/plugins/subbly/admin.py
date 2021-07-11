from django.contrib import admin

from .models import SubblySubscription


@admin.register(SubblySubscription)
class SubblySubscriptionAdmin(admin.ModelAdmin):
    fields = ("id", "email", "subscription_id")
