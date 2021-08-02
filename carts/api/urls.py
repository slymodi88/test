from django.urls import path, include
from rest_framework.routers import DefaultRouter

from carts.api import views
from carts.api.views import CartApi

router = DefaultRouter()
router.register('', views.CartApi, basename='cart')
urlpatterns = router.urls
urlpatterns += [
    path('detail/', CartApi.as_view({'get': 'detail'})),
    path('add/', CartApi.as_view({'post': 'add_product'}))

]


