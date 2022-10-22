def add_cart(shopping_cart, order_detail):
    if shopping_cart.check_duplicate_item(order_detail):
        shopping_cart.cart_list.append(order_detail)