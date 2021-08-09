from django.urls import path, include
from rest_framework.routers import DefaultRouter

from carts.api import views
from carts.api.views import CartApi

router = DefaultRouter()
router.register('', views.CartApi, basename='cart')
urlpatterns = router.urls
# urlpatterns += [
#     path('details/', CartApi.as_view({'get': 'details'})),
#     path('add/', CartApi.as_view({'post': 'add_product'}))
#
# ]


