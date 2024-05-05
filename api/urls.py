from django.urls import path, include
from rest_framework import routers
from .views import VendorViewSet, PurchaseViewSet, HistoricalPerformanceView, AcknowledgePurchaseOrderView

router = routers.DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vendors/<int:vendor_id>/performance/', HistoricalPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:po_order>/acknowledge', AcknowledgePurchaseOrderView.as_view())

]
