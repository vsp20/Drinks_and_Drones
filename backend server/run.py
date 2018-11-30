import configparser
from flask import Flask, render_template, request
import mysql.connector
import queries
import geopy.distance
import conf
from datetime import datetime, timedelta
import json
from flask_cors import CORS


# Read configuration from file.
config = configparser.ConfigParser()
config.read('config.ini')

# Set up application server.
app = Flask(__name__)
CORS(app)

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


# intended to be used for when we add something new to the db and want to get the auto-incremented id back
def sql_execute_return_new_id(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    id = cursor.lastrowid()
    db.commit()
    cursor.close()
    db.close()
    return id


# this is for the demo
@app.route('/products', methods=['GET'])
def getProducts():
    result = {"coffee":{"name":"coffee","id":"1"},"orange juice":{"name":"orange juice","id":"2"},"strawberry smoothie":{"name":"strawberry smoothie","id":"3"}}
    return json.dumps(result)


# this is what should have been used had the connection to the db worked
@app.route('/', methods=['GET', 'POST'])
def response_with_data():
    
    print(request.form)
    if "add-to-cart" in request.form:
        productID = str(request.form["product"])
        status = 0
        customerID = str(request.form["customerID"])
        order = sql_query(queries.get_order_id)
        if order <= 0:
            # if they don't currently have an order, make a new order for them
            order = sql_execute_return_new_id(queries.insert_into_order)
            sql_execute(queries.insert_into_purchased)
        sql_execute(queries.insert_into_includes)
        cart = sql_query(queries.get_cart)
        return cart

    elif "checkout" in request.form:
        customerID = str(request.form["customerID"])
        dest_long = float(request.form["destLongitude"])
        dest_lat = float(request.form["destLatitude"])
        status = 0
        order = sql_query(queries.get_order_id)
        if order <= 0:
            return "error: checking out without an order"
        else:
            order_prods = sql_query(queries.get_order_products)

            prods = {} # hold the products in the order and how many of them are wanted

            for row in order_prods:
                prod_id = row[0]
                if prod_id in prods:
                    prods[prod_id] += 1
                else:
                    prods[prod_id] = 1

            # check for avalibility of products in cart
            for prod in prods:
                ingred_avalibilities = sql_execute_return_new_id(queries.get_product_availability_by_id)
                for ingredrow in ingred_avalibilities:
                    avalibility = ingredrow[0]
                    if prods[prod] > avalibility:
                        return "error: there isn't enough of product id=" + str(prod_id)

            order_type = sql_query(queries.get_order_type)
            if order_type[0][0] == "delivery_order":
                # Delivery order. We need to deal with drones
                drones = sql_query(queries.get_free_drones_and_capacities)

                # fint the total weight of the order
                weights = sql_query(queries.get_order_weights)
                weight = 0
                for row in weights:
                    weight += row[0]

                # select a drone that is availible and can carry the order
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

                    # calculate the time to destination
                    time_to_dest = geopy.distance.vincenty((conf.store_lat, conf.store_long), (dest_lat, dest_long)).km * conf.drone_speed
                    est_delivery_time = datetime.now() + timedelta(seconds=(time_to_dest+conf.prep_time)) 
                    sql_execute(queries.update_dest_and_time)
            sql_execute(queries.set_order_to_purchased)

            # update ingredient quantities based on what was just purchased
            for prod in prods:
                ingred_ids_amnts = sql_query(queries.get_product_ingreds_id_and_amount)
                for row in ingred_ids_amnts:
                    ingred_id = row[0]
                    amount = row[1]
                    newamount = amount - prods[prod]
                    sql_execute(queries.update_ingreds_by_id)
            
            # update customer's num_orders
            new_num_orders = sql_query(queries.get_customer_num_orders)[0][0] + 1
            sql_execute(queries.update_num_orders)

            # returns information from the order
            return sql_query(queries.get_all_from_order)

    elif "get-all-products" in request.form:
        return sql_query(queries.get_all_products)
    
    elif "login" in request.form:
        # return customer's information if they are in database
        customerID = str(request.form["ID"])
        hashed_password = str(request.form["password"])

        cust_info = sql_execute_return_new_id(queries.get_customer_from_id_and_pswrd)
        if cust_info <= 0:
            return "username and password do not match"
        return cust_info

    elif "create-new-account" in request.form:
        customerID = str(request.form["ID"])
        name = str(request.form["name"])
        dob = str(request.form["dob"])
        hashed_password = str(request.form["password"])

        id_taken = sql_query(queries.in_use_cust_id)
        if id_taken <= 0:
            # if the id isn't already taken
            sql_execute(queries.insert_into_customer)
            return "success"
        else:
            return "error: ID already in use"

if __name__ == '__main__':
    app.run(**config['app'])