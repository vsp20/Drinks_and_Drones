import configparser
from flask import Flask, render_template, request
import mysql.connector
import queries
import geopy.distance
import conf
from datetime import datetime, timedelta


# Read configuration from file.
config = configparser.ConfigParser()
config.read('config.ini')

# Set up application server.
app = Flask(__name__)

# Create a function for fetching data from the database.
def sql_query(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


def sql_execute(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def sql_execute_return_new_id(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    id = cursor.lastrowid()
    db.commit()
    cursor.close()
    db.close()
    return id

# For this example you can select a handler function by
# uncommenting one of the @app.route decorators.

#@app.route('/')
#def basic_response():
#    return "It works!" #example

#@app.route('/')
#def template_response():
#    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def response_with_data():
    
    print(request.form)
    if "add-to-cart" in request.form:
        productID = str(request.form["product"])
        status = 0
        customerID = str(request.form["customerID"])
        order = sql_query(queries.get_order_id)
        if order <= 0:
            order = sql_execute_return_new_id(queries.insert_into_order)
            sql_execute(queries.insert_into_purchased)
        sql_execute(queries.insert_into_includes)
        cart = sql_query(queries.get_cart)
        #template_data['shoppingcart'] = cart
        #return render_template('viewcart.html', template_data=template_data)
        return cart

    elif "checkout" in request.form:
        customerID = str(request.form["customerID"])
        dest_long = float(request.form["destLongitude"])
        dest_lat = float(request.form["destLatitude"])
        status = 0
        order = sql_query(queries.get_order_id)
        if order > 0:
            return "error: checking out without an order"
        else:
            # check if its a valid purchase and stuff
            order_prods = sql_query(queries.get_order_products)

            prods = {}

            for row in order_prods:
                prod_id = row[0]
                if prod_id in prods:
                    prods[prod_id] += 1
                else:
                    prods[prod_id] = 1

            for prod in prods:
                ingred_avalibilities = sql_execute_return_new_id(queries.get_product_availability_by_id)
                for ingredrow in ingred_avalibilities:
                    avalibility = ingredrow[0]
                    if prods[prod] > avalibility:
                        return "error: there isn't enough of product id=" + str(prod_id)
            order_type = sql_query(queries.get_order_type)
            if order_type == 0:
                # Delivery order. Need to deal with drones
                drones = sql_query(queries.get_free_drones_and_capacities)
                weights = sql_query(queries.get_order_weights)
                weight = 0
                for row in weights:
                    weight += row[0]

                sel_drone = None
                for rows in drones:
                    drone_id = rows[0]
                    drone_cap = rows[1]
                    if weight <= drone_cap:
                        sel_drone = drone_id
                        break
                if sel_drone is None:
                    return "error: No drones can take this order right now"
                else:
                    sql_execute(queries.set_drone_to_busy)
                    sql_execute(queries.insert_into_delivers)
                    time_to_dest = geopy.distance.vincenty((conf.store_lat, conf.store_long), (dest_lat, dest_long)).km * conf.drone_speed
                    est_delivery_time = datetime.now() + timedelta(seconds=time_to_dest)
                    sql_execute(queries.update_dest_and_time)
            sql_execute(queries.set_order_to_purchased)

            for prod in prods:
                ingred_ids_amnts = sql_query(queries.get_product_ingreds_id_and_amount)
                for row in ingred_ids_amnts:
                    ingred_id = row[0]
                    amount = row[1]
                    newamount = amount - prods[prod]
                    sql_execute(queries.update_ingreds_by_id)

    elif "get-all-products" in request.form:
        # just spitting back all products for now
        return sql_execute(queries.get_all_products)

if __name__ == '__main__':
    app.run(**config['app'])