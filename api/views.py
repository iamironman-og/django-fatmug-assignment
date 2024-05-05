from django.utils import timezone
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        vendor = self.get_object()
        performance_data = {
            'on_time_delivery_rate': vendor.calculate_on_time_delivery_rate(),
            'quality_rating_avg': vendor.update_quality_rating_average(),
            'average_response_time': vendor.calculate_average_response_time().total_seconds(),
            'fulfillment_rate': vendor.calculate_fulfillment_rate(),
        }
        serializer = self.get_serializer(data=performance_data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = timezone.now()
        instance.save()
        # Recalculate average_response_time
        instance.vendor.calculate_average_response_time()
        return Response(self.get_serializer(instance).data)


class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = timezone.now()
        instance.save()
        # Recalculate average_response_time
        instance.vendor.calculate_average_response_time()
        return Response(self.get_serializer(instance).data)


class HistoricalPerformanceView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
