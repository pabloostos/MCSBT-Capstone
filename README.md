# 𝐌𝐂𝐒𝐁𝐓-𝐂𝐚𝐩𝐬𝐭𝐨𝐧𝐞 𝟐𝐧𝐝 𝐓𝐞𝐫𝐦 𝟐𝟎𝟐𝟑𝐇&𝐌

𝐊𝐏𝐈 𝐚𝐧𝐚𝐥𝐲𝐬𝐢𝐬

## 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧

- Student: Pablo Ostos Bollmann
- Email: p.ostos@gmail.com
- Master: MCSBT (IE)
- Professor: Gustavo Martin Vela

## 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐝𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧

This Capstone Project is an individual practice that allows students to apply the technical contents learnt over the term, integrating them to solve a real business challenge. The project will consist of the development of a data application deployed in a public cloud infrastructure that is accessible to real users to see and evaluate the result. The final project will be saved in the student's GitHub profile.

The architecture components that will be used are representative of most existing applications and webs, making it possible to extrapolate them to fit with a vast majority of needs. The components include:

- Frontend: This includes the web page and design of the user interface that will be used to interact with the data.
- Backend: This includes the specific logic of the service provided by the site, as well as any algorithms that will be implemented to serve in the frontend.
- Database: This is used to store the relevant information.
- Code Repository: The project code will be stored in a public repository on GitHub.
- API: An API will be created to access the data via other programs.

The project also allows for various flavors and variations from both a functional and technical point of view.
This project also puts the student in the shoes of a software engineer working on a development project for a customer where they will have to make the technical and technology decisions on how to solve the challenge.

## 𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬

- Python 3.9
- Flask 2.1.1
- SQLite 3
- HTML/CSS/JavaScript
- Bootstrap 5

## 𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐝𝐞𝐭𝐚𝐢𝐥𝐬

### 𝐀𝐏𝐈

- **Imports necessary libraries**, including Flask, SQLAlchemy, datetime, and Flask-RESTX.
- Defines variables for the host, user, password, and database to access a MySQL database.
- Creates a **Flask application** and sets the configuration for the SQLALCHEMY_DATABASE_URI to the host variable.
- Creates an **API** using the Flask-RESTX library with the specified version, title, description, contact information, and endpoint.
- The **connect()** function creates a MySQL database engine with the variables for user, password, host, and database. It also sets a connect timeout of 10 seconds. The function then creates a connection to the database engine and returns the connection object.
- The **disconnect()** function takes a connection object as an argument and closes the connection.
- Creates a Flask-RESTX namespace for **customers** and adds it to the API. It defines two endpoints within the customers namespace:
  - **"/customers"**, returns information for customers from the MySQL database. When a GET request is made to this endpoint, the function get_all_users() is called, which creates a database connection using the connect() function and executes a SELECT query to retrieve the customer data. It then converts the result to a list of dictionaries and returns it as a JSON object.
  - **"/customers/<string:id>"**, returns information for a specific customer identified by id. When a GET request is made to this endpoint, the function select_user() is called. This function takes in the id parameter from the URL, creates a database connection using the connect() function, and executes a SELECT query to retrieve the customer data for the given id. It also checks for a 404 error if the customer is not found. It then converts the result to a list of dictionaries and returns it as a JSON object.
- Creates a Flask-RESTX namespace for **articles** and adds it to the API. It defines two endpoints within the articles namespace:
  - **"/articles"**, returns information for the first 10 articles from the MySQL database. When a GET request is made to this endpoint, the function get_all_articles() is called, which creates a database connection using the connect() function and executes a SELECT query to retrieve the article data. It then converts the result to a list of dictionaries and returns it as a JSON object.
  - **"/articles/<string:id>"**, returns information for a specific article identified by id. When a GET request is made to this endpoint, the function select_user() is called. This function takes in the id parameter from the URL, creates a database connection using the connect() function, and executes a SELECT query to retrieve the article data for the given id. It also checks for a 404 error if the article is not found. It then converts the result to a list of dictionaries and returns it as a JSON object.
- Sets up the endpoints for the **transactions** API. It creates a new namespace for transactions and adds it to the API. There are two endpoint routes defined:
  - The first route returns a list of **all transactions** in the database. It sends a SELECT query to the database and returns the result as a JSON object.
  - The second route returns information on a **single transaction**, specified by the transaction ID. It sends a SELECT query to the database and returns the result as a JSON object. If the transaction is not found, it returns a 404 response.

### 𝐅𝐫𝐨𝐧𝐭𝐞𝐧𝐝

- **"load_data()":** Function to **load data** from a JSON response obtained from an API call. It uses the pd.json_normalize function from the Pandas library to convert the JSON data into a Pandas DataFrame.
- Uses the requests library to make API calls to your server and retrieving data in JSON format. Loads the data for customers, articles, and transactions into their respective dataframes, for further analysis and visualization.
- **𝐒𝐓𝐑𝐄𝐀𝐌𝐋𝐈𝐓:**
  - _𝐅𝐈𝐋𝐓𝐄𝐑𝐒:_
    - Club member status
    - Customer age
    - Transaction Channel ID
    - Article group
    - Article color
    - Article product
  - _𝐃𝐀𝐓𝐀𝐅𝐑𝐀𝐌𝐄𝐒:_
    - Customer dataframe applying filters
    - Transactions dataframe applying filters
    - Articles dataframe applying filters
  - _𝐏𝐋𝐎𝐓𝐒:_
    - Customer age count (bar chart)
    - Club Member Status Percentages (pie chart)
    - Number of transactions by channel id (bar chart)
    - Number of transactions by age (bar chart)
    - Sales Channel Percentages (pie chart)
    - Number of articles per index group (bar chart)
    - Number of articles per color value (bar chart)
    - Number of articles per product (bar chart)
  - _𝐊𝐏𝐈𝐬:_
    - Number of different customers
    - Number of different genders
    - Average age
    - Sum of all prices
    - Average of prices
    - Number of product types
    - Number of garment groups
    - Number of color groups
