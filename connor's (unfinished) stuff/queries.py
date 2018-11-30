get_order_id = "select customer_order.id from customer, customer_order, purchased where customer.id={customerID} and customer_order.status={status} and customer.id=purchased.customerID and customer_order.id=purchased.orderid"
insert_into_order = "insert into customer_order (status) values ({status})"
insert_into_purchased = "insert into purchased (customerID, orderID) values ({customer_ID},{order_ID})"
insert_into_includes = "insert into includes (orderID, productID) values ({order}, {productID})"
get_cart = "select product.name, product.price, product.weight from product, includes where product.ID = includes.product_ID and indludes.order_ID={order}"
get_free_drones_and_capacities = "select drone.id, drone.capacity from drone where drone.availibility=1"
get_order_weights = "select product.weight from product, includes where includes.orderID={order} and includes.productID=product.ID"
get_product_availability_by_id = "select ingredient.amount from contains, ingredient where contains.productID={prod_ID} and contains.ingredientID=ingredient.ID"
get_order_products = "select productID from includes where orderID={order}"
get_order_type = "select type from customer_order where orderID={order}"
set_drone_to_busy = "update drone set drone.status=1 where drone.id={drone_id}"
set_order_to_purchased = "update customer_order set customer_order.status=1 where customer_order.id={order}"
insert_into_delivers = "insert into delivers (droneID, orderID) values ({drone_id}, {order})"
get_product_ingreds_id_and_amount = "select ID, amount from contains where productID={prod_ID}"
update_ingreds_by_id = "update ingredient set amount={newamount} where ID={ingred_ID}"
update_dest_and_time = "update customer_order set customer_order.destlong={dest_long}, customer_order.destlat{dest_lat}, customer_order.time={time_to_dest} where customer_order.id={order}"
get_all_products = "select product.id, product.name, product.price, product.calories, product.weight, allergen.name from product, contains, has, allergen where product.ID=contains.productID and contains.ingredientID=has.ingredientID and has.allergenID=allergen.ID"
get_all_from_order = "select * from customer_order where customer_order.id={order}"
get_customer_from_id_and_pswrd = "select ID, name, num_orders, DOB from customer where ID={cust_ID} and password={hashed_password}"
get_customer_num_orders = "select num_orders from customer where ID={customerID}"
update_num_orders = "update customer set num_orders={new_num_orders} where ID={customerID}"
in_use_cust_id = "select 1 from customer where ID={customerID}"
insert_into_customer = "insert into customer (ID, name, num_orders, DOB) values ({customerID}, {name}, 0, {dob})"