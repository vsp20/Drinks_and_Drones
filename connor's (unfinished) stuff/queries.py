get_order_id = "select order.id from customer, order, purchased where customer.id={customerID} and order.status={status} and customer.id=purchased.customerID and order.id=purchased.orderid"
insert_into_order = "insert into order (status) values ({status})"
insert_into_purchased = "insert into purchased (customer_ID, order_ID) values ({customer_ID},{order_ID})"
insert_into_includes = "insert into includes (order_ID, product_ID) values ({order}, {productID})"
get_cart = "select product.name, product.price, product.weight from product, includes where product.ID = includes.product_ID and indludes.order_ID={order}"
get_free_drones_and_capacities = "select drone.id, drone.capacity from drone where drone.availibility=1"
get_order_weight = None
get_product_availability_by_id = None
get_order_products_and_quantities = None
get_order_type = None
set_drone_to_busy = None
set_order_to_purchased = None
insert_into_deliveries = None
remove_product_ingreds_by_prod = None
update_dest_and_time = None
get_all_products = "select * from product"