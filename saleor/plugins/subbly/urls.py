from django.conf.urls import url

from .views import subscription_created

urlpatterns = [
    url(r"^subscription_created", subscription_created, name="subscription-created"),
]
