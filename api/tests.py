# tests/test_purchase_order.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vendor, PurchaseOrder
from .serializers import PurchaseOrderSerializer

class PurchaseOrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name="Test Vendor", contact_details="Contact", address="Address", vendor_code="V001")

    def test_create_purchase_order(self):
        url = reverse('purchaseorder-list')
        data = {
            'po_number': 'PO001',
            'vendor': self.vendor.id,
            'order_date': '2024-04-30T12:00:00Z',
            'delivery_date': '2024-05-05T12:00:00Z',
            'items': 'Item1, Item2',
            'quantity': 10,
            'status': 'pending',
            'issue_date': '2024-04-30T12:00:00Z'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 1)
        self.assertEqual(PurchaseOrder.objects.get().po_number, 'PO001')

    def test_retrieve_purchase_order(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number='PO002',
            vendor=self.vendor,
            order_date='2024-05-01T12:00:00Z',
            delivery_date='2024-05-06T12:00:00Z',
            items='Item1, Item2',
            quantity=20,
            status='pending',
            issue_date='2024-05-01T12:00:00Z'
        )
        url = reverse('purchaseorder-detail', args=[purchase_order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = PurchaseOrderSerializer(purchase_order)
        self.assertEqual(response.data, serializer.data)

    def test_update_purchase_order(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number='PO003',
            vendor=self.vendor,
            order_date='2024-05-02T12:00:00Z',
            delivery_date='2024-05-07T12:00:00Z',
            items='Item1, Item2',
            quantity=30,
            status='pending',
            issue_date='2024-05-02T12:00:00Z'
        )
        url = reverse('purchaseorder-detail', args=[purchase_order.id])
        data = {'quantity': 40}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PurchaseOrder.objects.get(id=purchase_order.id).quantity, 40)

    def test_delete_purchase_order(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number='PO004',
            vendor=self.vendor,
            order_date='2024-05-03T12:00:00Z',
            delivery_date='2024-05-08T12:00:00Z',
            items='Item1, Item2',
            quantity=50,
            status='pending',
            issue_date='2024-05-03T12:00:00Z'
        )
        url = reverse('purchaseorder-detail', args=[purchase_order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PurchaseOrder.objects.count(), 0)
