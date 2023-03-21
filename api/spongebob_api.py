# ========================================================================== #

# ========================================================================== #
# Importing neccessary libraries
from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from datetime import datetime
from flask_restx import Api, Namespace, Resource, reqparse, inputs, fields

# ========================================================================== #
# Give value to all the variables to access to mysql database

host = ''  # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
user = ''  # e.g. 'my-db-user'
passw = '' # e.g. 'my-db-password'
database = ''  # e.g. 'my-database'

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = host

api = Api(app, version = '1.0',
    title = 'Pablo Ostos API for Spongebob DB',
    description = """
        Obtaining data from H&M datasets
        """,
    contact = "p.ostos@student.ie.edu",
    endpoint = "/api/v1")

# ========================================================================== #
# functions for connection
def connect():
    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
    conn = db.connect()
    return conn

def disconnect(conn):
    conn.close()

# ========================================================================== #
# CUSTOMERS
# ========================================================================== #
# Creating new namespace for customers
customers = Namespace('customers',
    description = 'All operations related to customers',
    path='/api/v1')
api.add_namespace(customers)

# Endpoint to return all users
@customers.route("/customers")
class get_all_users(Resource):

    def get(self):
        conn = connect()
        select = """
            SELECT *
            FROM customer
            LIMIT 10;"""
        result = conn.execute(text(select)).mappings().all()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

# ========================================================================== #
# Endpoint to return a specific customer information
@customers.route("/customers/<string:id>")
@customers.doc(params = {'id': 'The ID of the user'})
class select_user(Resource):

    @api.response(404, "CUSTOMER not found")
    def get(self, id):
        id = str(id)
        conn = connect()
        select = """
            SELECT *
            FROM customers
            WHERE customer_id = '{0}';""".format(id)

        result = conn.execute(text(select)).mappings().all()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})
# ========================================================================== #


# ========================================================================== #
# ARTICLES
# ========================================================================== #
# Creating new namespace for articles
articles = Namespace('articles',
    description = 'All articles',
    path='/api/v2')
api.add_namespace(articles)

# Endpoint to return all articles
@articles.route("/articles")
class get_all_articles(Resource):

    def get(self):
        conn = connect()
        select = """
            SELECT *
            FROM articles
            LIMIT 10;"""
        result = conn.execute(text(select)).mappings().all()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})
# ========================================================================== #
# Endpoint to return information of one article
@articles.route("/articles/<string:id>")
@articles.doc(params = {'id': 'The ID of the article'})
class select_user(Resource):

    @api.response(404, "ARTICLE not found")
    def get(self, id):
        id = str(id)
        conn = connect()
        select = """
            SELECT *
            FROM articles
            WHERE article_id = '{0}'""".format(id)
        result = conn.execute(text(select)).mappings().all()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

# ========================================================================== #
# TRANSACTIONS
# ========================================================================== #
# Creating new namespace for transactions
transactions = Namespace('transactions',
    description = 'All operations related to transactions',
    path='/api/v3')
api.add_namespace(transactions)

# Endpoint to return all transactions
@transactions.route("/transactions")
class get_all_transactions(Resource):

    def get(self):
        conn = connect()
        select = """
            SELECT *
            FROM transactions
            LIMIT 10;"""
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})
# ========================================================================== #
# Endpoint to return information on a single transaction id
@transactions.route("/transactions/<string:id>")
@transactions.doc(params = {'id': 'The ID of the transaction'})
class select_transaction(Resource):

    @api.response(404, "TRANSACTION not found")
    def get(self, id):
        id = str(id)
        conn = connect()
        select = """
            SELECT *
            FROM transactions
            WHERE transaction_id = '{0}';""".format(id)
        
        
        result = conn.execute(text(select)).mappings().all()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})
# ========================================================================== #

# ========================================================================== #
if __name__ == '__main__':
    app.run(debug = True)