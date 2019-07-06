from django.conf.urls import url

from alameda_api.health_checks.views import liveness, readiness

urlpatterns = [
    url(r'^live/$', liveness),
    url(r'^ready/$', readiness),
]
