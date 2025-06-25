#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv("orders.csv")
data.head(10)


# In[2]:


#Handle null values
data = pd.read_csv("orders.csv", na_values = ['Not Available', 'unknown'])
data.head(10)
data['Ship Mode'].unique()


# In[3]:


#Rename the columns
data.columns=data.columns.str.lower()
data.columns=data.columns.str.replace(' ','_')
data.columns


# In[4]:


#Add new columns
data['discount']=data['list_price']*data['discount_percent']*.01
data['sale_price']= data['list_price']-data['discount']
data['profit']=data['sale_price']-data['cost_price']
data.head(5)


# In[22]:


#convert order date from object data type to datetime
data['order_date']=pd.to_datetime(data['order_date'],format="%Y-%m-%d")


# In[6]:


#drop cost price list price and discount percent columns
data.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[7]:


data.head(5)


# In[10]:


#pip install pymysql sqlalchemy pandas


# In[23]:


#load the data into mysql
 
import sqlalchemy as sal

# Replace these with your actual details
username = 'root'              # default MySQL user
password = 'Pooja@354177'     # the password you set
host = '127.0.0.1'
port = 3306
database = 'ecommerce'         # the schema you created

# Create SQLAlchemy engine for MySQL
engine = sal.create_engine("mysql+pymysql://root:Pooja%40354177@127.0.0.1:3306/ecommerce")


# In[24]:


# Replace the table if it already exists
data.to_sql(name='orders', con=engine, if_exists='append', index=False)


# In[ ]:


#SQL TABLE SCHEMA
"""CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    ship_mode VARCHAR(20),
    segment VARCHAR(20),
    country VARCHAR(20),
    city VARCHAR(20),
    state VARCHAR(20),
    postal_code VARCHAR(20),
    region VARCHAR(20),
    category VARCHAR(20),
    sub_category VARCHAR(20),
    product_id VARCHAR(50),
    quantity INT,
    discount DECIMAL(7, 2),
    sale_price DECIMAL(7, 2),
    profit DECIMAL(7, 2)
);   """


# In[27]:


# Save DataFrame to CSV
file_path = '/Users/poojavemuri/Documents/orders_cleaned.csv'
data.to_csv(file_path, index=False)

print(f"File successfully saved to: {file_path}")


# In[ ]:




