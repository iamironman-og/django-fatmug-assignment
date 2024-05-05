Vendor and Purchase Order API Documentation
===========================================

Introduction
------------

This API allows you to manage vendors and purchase orders.

Base URL
--------

The base URL for all endpoints is ``/api/``.

Authentication
--------------

Authentication is required for certain endpoints. Use token-based authentication.

Vendor Endpoints
----------------

Create a New Vendor
~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/vendors/``
- **Method:** ``POST``
- **Description:** Create a new vendor.
- **Request Body:**
  
  .. code-block:: json
  
     {
       "name": "Vendor A",
       "contact_details": "Contact details of Vendor A",
       "address": "Address of Vendor A",
       "vendor_code": "VENDORCODE001"
     }

- **Example Response:**
  
  .. code-block:: json

     {
       "id": 1,
       "name": "Vendor A",
       "contact_details": "Contact details of Vendor A",
       "address": "Address of Vendor A",
       "vendor_code": "VENDORCODE001",
       "on_time_delivery_rate": 0,
       "quality_rating_avg": 0,
       "average_response_time": 0,
       "fulfillment_rate": 0
     }

List All Vendors
~~~~~~~~~~~~~~~~

- **URL:** ``/api/vendors/``
- **Method:** ``GET``
- **Description:** List all vendors.

Retrieve a Specific Vendor's Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/vendors/{vendor_id}/``
- **Method:** ``GET``
- **Description:** Retrieve details of a specific vendor.

Update a Vendor's Details
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/vendors/{vendor_id}/``
- **Method:** ``PUT``
- **Description:** Update details of a specific vendor.

Delete a Vendor
~~~~~~~~~~~~~~~~

- **URL:** ``/api/vendors/{vendor_id}/``
- **Method:** ``DELETE``
- **Description:** Delete a specific vendor.

Purchase Order Endpoints
------------------------

Create a Purchase Order
~~~~~~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/purchase_orders/``
- **Method:** ``POST``
- **Description:** Create a purchase order.
- **Request Body:**
  
  .. code-block:: json
  
     {
       "po_number": "PO123",
       "vendor_id": 1,
       "order_date": "2024-05-05T12:00:00Z",
       "delivery_date": "2024-05-10T12:00:00Z",
       "items": [{"name": "Item A", "quantity": 10}],
       "quantity": 10,
       "status": "pending",
       "quality_rating": null,
       "issue_date": "2024-05-05T12:00:00Z",
       "acknowledgment_date": null
     }

- **Example Response:**
  
  .. code-block:: json

     {
       "id": 1,
       "po_number": "PO123",
       "vendor_id": 1,
       "order_date": "2024-05-05T12:00:00Z",
       "delivery_date": "2024-05-10T12:00:00Z",
       "items": [{"name": "Item A", "quantity": 10}],
       "quantity": 10,
       "status": "pending",
       "quality_rating": null,
       "issue_date": "2024-05-05T12:00:00Z",
       "acknowledgment_date": null
     }

List All Purchase Orders
~~~~~~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/purchase_orders/``
- **Method:** ``GET``
- **Description:** List all purchase orders.

Retrieve a Specific Purchase Order's Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/purchase_orders/{po_id}/``
- **Method:** ``GET``
- **Description:** Retrieve details of a specific purchase order.

Update a Purchase Order
~~~~~~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/purchase_orders/{po_id}/``
- **Method:** ``PUT``
- **Description:** Update a specific purchase order.

Delete a Purchase Order
~~~~~~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/purchase_orders/{po_id}/``
- **Method:** ``DELETE``
- **Description:** Delete a specific purchase order.

Vendor's Performance Metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/vendors/{vendor_id}/performance``
- **Method:** ``GET``
- **Description:** Retrieve a vendor's performance metrics.

Vendor's Acknowledgment of Purchase Orders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL:** ``/api/purchase_orders/{po_id}/acknowledge``
- **Method:** ``POST``
- **Description:** Vendor acknowledges a purchase order.
