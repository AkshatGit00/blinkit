# Blinkit LLD System

This is a Low-Level Design (LLD) implementation of a **Blinkit-like grocery delivery system** in Python. It models essential components such as Users, Products, Warehouses, Inventory, Orders, and Payments.

---

## 📦 Features

- ✅ User and Address management
- 🛒 Cart system to hold product category and quantity
- 🏬 Multiple Warehouses with associated inventory
- 📂 Product categorization and stock management
- 🧾 Order processing with payment handling
- 💸 Supports multiple payment modes (e.g., UPI, COD)
- 📄 Invoice generation
- 🔄 Inventory update based on orders

---

## 🏗️ Modules Overview

### 1. **User**
- Maintains user details and delivery address.
- Each user has a cart and a list of placed orders.

### 2. **Product and Category**
- `ProductCategory`: Represents a category with price and name.
- `Product`: Basic product with ID and name.

### 3. **Inventory**
- Contains a mapping of category → list of products.
- Handles product addition/removal.

### 4. **Warehouse**
- Has a unique ID, address, and inventory.
- Can process product addition/removal.

### 5. **Cart**
- Maintains user-selected category and quantity.

### 6. **Order**
- Created by the user, associated with a warehouse.
- Handles inventory update, payment processing, and invoice generation.

### 7. **Invoice**
- Generates a detailed bill with tax calculations (default 10%).

### 8. **Payment**
- Payment abstraction allows for multiple modes (e.g., UPI, COD).
- Sample classes: `UPIPaymentMode`, `CODPaymentMode`

---

## 🧪 Sample Flow

1. **Create Users** with delivery addresses.
2. **Add Products** to Warehouses via Inventory.
3. **Add Items to Cart** by selecting categories and quantities.
4. **Create an Order** and checkout.
5. **Make Payment** → If successful, order is completed and cart is cleared.
6. **Invoice** is printed with price, quantity, and tax.

---

## ✅ Example Usage

```python
# User adds products to cart
user_cart.add_item(category_id="FRUITS", count=3)

# User places an order
order = Order(user, warehouse)
order.check_out()

# Generates invoice
order.generate_invoice()

📁 Project Structure
blinkit/
├── models/
│   ├── user.py
│   ├── warehouse.py
│   ├── inventory.py
│   ├── order.py
│   ├── payment.py
│   ├── invoice.py
├── services/
│   ├── order_service.py
│   ├── warehouse_service.py
├── main.py


🛠️ How to Run
python main.py

