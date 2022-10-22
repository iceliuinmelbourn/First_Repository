from datetime import datetime
import pandas as pd
sales_history_path = 'sales_history.csv'

def checkout(shopping_cart):
    shopping_cart.calc_total_price()
    checkout_statement = ''
	#generate the invoice information
    checkout_statement += '-------------------------Invoice----------------------------\n'
    for i,item in enumerate(shopping_cart.cart_list):
        item_list = item.split(';')
        item_detail = 'Item No: '+ str(i+1).ljust(3)+ 'Item type: '+item_list[0].ljust(10)+'Weight :' \
            +item_list[1].rjust(6)+'  Destination: '+ item_list[3].ljust(20) + 'Unit price: $ '+ item_list[4] + '\n'
        checkout_statement += item_detail 
    checkout_statement += '\n'
    checkout_statement += 'Total Cost: '+ str(shopping_cart.total_price) +'\n'
    checkout_statement += '-----------------------End Invoice--------------------------\n\n'
	#generate post stamp
    for i,item in enumerate(shopping_cart.cart_list):
        item_list = item.split(';')
        checkout_statement += '---------------------Purchase Stamps------------------------\n'
        item_detail = item_list[0]+'\n' + 'Destination: '+ item_list[3].ljust(20) + 'Weight :' \
            +item_list[1].ljust(10) + '\n'
        checkout_statement += item_detail 
        checkout_statement += '------------------------------------------------------------\n\n'
    print(checkout_statement)
    checkout_dttm = datetime.now()
	#write into invoice txt file
    file_name = checkout_dttm.strftime('%Y-%m-%d %H_%M_%S')+'.txt'
    with open(file_name,'w') as f:
        f.write(checkout_statement)
    print('Invoice file: {} has generated'.format(file_name))
    #get last sales_id and plus 1 as new sales_id
    sales_history = pd.read_csv(sales_history_path,header=0)
    max_sale_id = sales_history['sale_id'].max()
    new_sale_id = str(int(max_sale_id)+1)
	#add order information into sales_history dataset
    content = []
    for i,item in enumerate(shopping_cart.cart_list):
            item_list = item.split(';')
            content.append([new_sale_id,checkout_dttm.strftime('%Y/%#m/%#d %#H:%#M:%#S'),item_list[0],\
                                item_list[1].lower().replace('kg',''), item_list[3],item_list[2], item_list[-1]]) 
    sale_history_df = pd.DataFrame(content).set_index(0)
    sale_history_df.to_csv(sales_history_path,mode='a',header=False)
    print('Sales history has been added into file')
    
    