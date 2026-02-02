from models.address import Address
from models.inventory import Inventory
from models.order import Order
from models.product import Product
from models.productCategory import ProductCategory
from models.user import User
from models.warehouse import WareHouse
from services.orderService import OrderService
from services.userService import UserService
from services.wareHouseService import WareHouseService
from strategy.ware_house_strategy.nearestWareHouseSelectionStrategy import NearestWareHouseSelectionStrategy


def main():
    
    orderService = OrderService()
    userService = UserService()
    wareHouseService = WareHouseService()

    #create user
    user1:User = userService.add_user("USER_1", "Akshat", Address("Bengaluru", "Karnataka", 560034))
    user2:User = userService.add_user("USER_2", "Aryan", Address("Gwalior", "Madhya Pradesh", 474012))
    print("users", userService.get_all_users())

    #create warehouses
    inventory1 = Inventory()
    wareHouse1 = WareHouse("W_1", Address("Bengaluru", "Karnataka", 560034), inventory1)
    print(wareHouseService.add_ware_house(wareHouse1))
    print(wareHouseService.add_ware_house(wareHouse1))

    inventory2 = Inventory()
    wareHouse2 = WareHouse("W_2", Address("Gwalior", "Madhya Pradesh", 474012), inventory2)
    print(wareHouseService.add_ware_house(wareHouse2))

    #create product categories
    inventory1.add_category("C_1", "Coca Cola Cold Drink", 100.00)
    inventory1.add_category("C_2", "Lux small Soap", 55.00)

    inventory2.add_category("C_1", "Sprite Cold Drink", 110.00)
    inventory2.add_category("C_2", "Dove medium Soap", 60.00)

    #create products
    product1 = Product("Coca Cola")
    product2 = Product("Coca Cola")
    product3 = Product("Lux")
    inventory1.add_product(product1, "C_1")
    inventory1.add_product(product2, "C_1")
    inventory1.add_product(product3, "C_2")

    product4 = Product("Sprite")
    product5 = Product("Sprite")
    product6 = Product("Dove")
    inventory2.add_product(product4, "C_1")
    inventory2.add_product(product5, "C_1")
    inventory2.add_product(product6, "C_2")

    print("inventory1", inventory1.product_category_list)
    print("inventory2", inventory2.product_category_list)

    print("--------product list from inventory1---------")
    for category_id, category in inventory1.product_category_list.items():
        print(f"category_id: {category_id}, category_name: {category.category_name}, stock: {category.get_product_count()}")

    print("--------product list from inventory2---------")
    for category_id, category in inventory2.product_category_list.items():
        print(f"category_id: {category_id}, category_name: {category.category_name}, stock: {category.get_product_count()}")

    # order flow
    nearest_warehouse:WareHouse = wareHouseService.select_ware_house(NearestWareHouseSelectionStrategy())
    print("nearest warehouse", nearest_warehouse)

    print("---------Inventory Items------------")
    inventory = nearest_warehouse.inventory
    for category_id, category in inventory.product_category_list.items():
        print(f"category_id: {category_id}, category_name: {category.category_name}, stock: {category.get_product_count()}")

    print("--------add item to cart---------")
    print(user1.user_cart_details.add_item_in_cart("C_1", 2, inventory))

    print("-----------place order----------------")
    order:Order = orderService.create_order("Order_1", user1, nearest_warehouse)
    print("order", order)

    print("-----------checkout--------------")
    print(order.check_out())

    print("---------Inventory Items------------")
    inventory = nearest_warehouse.inventory
    for category_id, category in inventory.product_category_list.items():
        print(f"category_id: {category_id}, category_name: {category.category_name}, stock: {category.get_product_count()}")

    print("-----------Invoice------------")
    order.generate_invoice()

if __name__=="__main__":
    main()