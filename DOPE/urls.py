from django.urls import include, path
from engine import views
from engine import urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]