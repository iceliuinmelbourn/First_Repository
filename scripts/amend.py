def update_item(shopping_cart,order_item,item_no):
        #load order info from order item and fill into the stamp_item's attributes
        order_item.load_item(shopping_cart.cart_list[item_no])
        #get user input new weight, only weight can be updated
        weight = float(input('please enter the new weight in numeric you want to update in kg: the limit is: {}  '.format(order_item.weight_limit)))
        if not order_item.get_weight(weight):
            print('enter valid weight')
            return False
        #re-generate the price and order_detail
        order_item.generate_order_detail()
        #print out the updated order_detail and asking for confirm
        print('the updated order detail is: {}'.format(order_item.order_detail))
        confirm_flg=input('Are you sure you want to update? y/n')
        if confirm_flg.lower() == 'y':
            #update the cart_list if user confirm by y
            shopping_cart.cart_list[item_no] = order_item.order_detail 
            print('Order has been updated.')
            return True
        else:
            print('Amend has been cancelled.')
            return False