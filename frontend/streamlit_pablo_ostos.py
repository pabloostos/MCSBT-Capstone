from sqlalchemy import create_engine, engine, text
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import requests

# ===================================================
@st.experimental_memo # @st.cache_data
def load_data(response_json):
    try:
        data = pd.json_normalize(response_json, "result")
    except Exception as e:
        print(e)
    return data 

# ===================================================
#Loading dataframes
server_string = ""
# ===================================================
# CUSTOMERS
customers_df = requests.get(f"{server_string}/api/v1/customers").json()
customers_df = load_data(customers_df)

# ===================================================
# ARTICLES
articles_df = requests.get(f"{server_string}/api/v2/articles").json()
articles_df = load_data(articles_df)
# ===================================================
# TRANSACTIONS
transactions_df = requests.get(f"{server_string}/api/v3/transactions").json()
transactions_df = load_data(transactions_df)

# ===================================================
# Creating a title for the App: 
# ===================================================
st.title("H&M Key Performance Indicators")
st.subheader("Capstone Project Pablo Ostos Bollmann")

st.sidebar.write("FILTERS")

# ===================================================
# Customer Dataframe: 
# ===================================================
st.title("Customer Dataframe")

# Sidebar filter for Club Member Status
status_df = customers_df["club_member_status"].unique()

status_lst = status_df


status_filtered_lst = st.sidebar.multiselect(
    label = "CLUB MEMBER STATUS",
    options = status_lst,
    default = status_lst,
    key = "multiselect_status"
)    


# Sidebar slider filter for age
age_df = customers_df["age"].unique()

age_filtered_lst = st.sidebar.slider(
    'Select a range of ages',
    0, 100, (20, 80))




# Apply filters to customer dataframe
customers_df = customers_df[(customers_df['age']>=age_filtered_lst[0]) & (customers_df['age']<=age_filtered_lst[1])]
customers_df = customers_df[customers_df['club_member_status'].isin(status_filtered_lst)]
num_status = customers_df["club_member_status"].nunique()
num_customers = len(customers_df["customer_id"])

member_status = customers_df.groupby('club_member_status').count()
member_status = member_status[['customer_id']]
member_status.rename(columns={'customer_id': 'count'}, inplace=True)
member_status['percentage'] = (member_status['count'] / num_customers) * 100

st.dataframe(customers_df)
st.caption("Customer age count")
st.bar_chart(customers_df.groupby('age')['customer_id'].count())

fig_status = px.pie(member_status, values='percentage', names=member_status.index,
            title='Club Member Status Percentages')
st.plotly_chart(fig_status, use_container_width=True)


#KPIs:
# ===================================================
st.subheader("Customers KPIs")
num_customers = len(customers_df["customer_id"])#.nunique()
avg_age = np.mean(customers_df["age"])
num_status = customers_df["club_member_status"].nunique()

kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric(
    label = "Number of different customers",
    value = num_customers,
    delta = num_customers,
)

kpi2.metric(
    label = "Number of different genders",
    value = num_status,
    delta = num_status,
)
        
kpi3.metric(
    label = "Average age",
    value = round(avg_age, 2),
    delta = -10 + avg_age,)


# ===================================================
# Transactions Dataframe: 
# ===================================================
st.title("Transactions Dataframe")

# Sidebar filter for Channel
channel_lst = transactions_df["sales_channel_id"].unique()

channel_filtered_lst = st.sidebar.multiselect(
    label = "Channel ID",
    options = channel_lst,
    default = channel_lst,
    key = "multiselect_channel"
)    

transactions_df = transactions_df[transactions_df["sales_channel_id"].isin(channel_filtered_lst)]

st.dataframe(transactions_df)
st.caption("Number of transactions by channel id")
st.bar_chart(transactions_df.groupby(["sales_channel_id"])["customer_id"].count())

# Number of transactions by age
st.caption("Number of transactions by age")
merged_df = pd.merge(transactions_df, customers_df, on  =["customer_id"])
st.bar_chart(merged_df["age"].value_counts())

total_sales_channel_1 = len(transactions_df[transactions_df['sales_channel_id'] == 1])
total_sales_channel_2 = len(transactions_df[transactions_df['sales_channel_id'] == 2])

percentage_channel_1 = (total_sales_channel_1 / len(transactions_df['sales_channel_id'])) * 100
percentage_channel_2 = (total_sales_channel_2 / len(transactions_df['sales_channel_id'])) * 100

sales_channel_df = pd.DataFrame()
sales_channel_df['channel'] = channel_lst
sales_channel_df['percentage'] = [percentage_channel_1, percentage_channel_2]

fig_channel = px.pie(sales_channel_df, values='percentage', names='channel',
            title='Sales Channel Percentage')
st.plotly_chart(fig_channel, use_container_width=True)
#Transactions KPIs:
# ===================================================
st.subheader("Transactions KPIs")
sum_prices = sum(transactions_df['price'])
mean_prices = sum(transactions_df['price'])/len(transactions_df['price'])
transactions_sales_sum = transactions_df.groupby('sales_channel_id').sum()
transactions_sales_sum = transactions_sales_sum[['price']] 

kpi1, kpi2 = st.columns(2)

kpi1.metric(
    label = "Sum of all prices",
    value = sum_prices,
    delta = sum_prices,
)

kpi2.metric(
    label = "Average of prices",
    value = mean_prices,
    delta = mean_prices,
)


# ===================================================
# Articles Dataframe: 
# ===================================================
st.title("Articles Dataframe")

# Sidebar filter for Club Member Status
article_group_lst = articles_df["index_group_name"].unique()
article_colors_lst = articles_df['perceived_colour_value_name'].unique()
article_product_lst = articles_df['product_group_name'].unique()

article_group_filtered_lst = st.sidebar.multiselect(
    label = "Article Group",
    options = article_group_lst,
    default = article_group_lst,
    key = "multiselect_article_group"
) 

article_color_filtered_lst = st.sidebar.multiselect(
    label = "Article Color",
    options = article_colors_lst,
    default = article_colors_lst,
    key = "multiselect_color"
) 

article_product_filtered_lst = st.sidebar.multiselect(
    label = "Article Product",
    options = article_product_lst,
    default = article_product_lst,
    key = "multiselect_product"
)

articles_df = articles_df[articles_df["index_group_name"].isin(article_group_filtered_lst)]
articles_df = articles_df[articles_df["perceived_colour_value_name"].isin(article_color_filtered_lst)]
articles_df = articles_df[articles_df["product_group_name"].isin(article_product_filtered_lst)]

st.dataframe(articles_df)

st.caption("Number of articles per index group")
st.bar_chart(articles_df.groupby(["index_group_name"])["article_id"].count())
st.caption("Number of articles per color value")
st.bar_chart(articles_df.groupby(["perceived_colour_value_name"])["article_id"].count())
st.caption("Number of articles per product")
st.bar_chart(articles_df.groupby(["product_group_name"])["article_id"].count())

#Articles KPIs:
# ===================================================
st.subheader("Articles KPIs")
num_product_type = articles_df["product_type_no"].nunique()
num_garment_groups = articles_df["garment_group_name"].nunique()
num_colour_groups = articles_df["colour_group_name"].nunique()

kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric(
    label = "Number of product types",
    value = num_product_type,
    delta = num_product_type,
)

kpi2.metric(
    label = "Number of garment groups",
    value = num_garment_groups,
    delta = num_garment_groups,
)

kpi3.metric(
    label = "Number of color groups",
    value = num_colour_groups,
    delta = num_colour_groups,
)
