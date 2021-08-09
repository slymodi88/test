from rest_framework.routers import DefaultRouter

from orders.api import views

router = DefaultRouter()
router.register('', views.OrderApi, basename='order')
urlpatterns = router.urls


