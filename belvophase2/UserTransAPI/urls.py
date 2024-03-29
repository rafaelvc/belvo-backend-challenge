from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('usertransadd/', views.transactions_bulk_create),
    path('userbalance/',  views.user_transactions_balance),
    path('userbalancebycategory/',  views.user_transactions_category)
]
