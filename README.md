
# TEXT TO SQL GENERATOR


This repository contains a Text-to-SQL model application that ussing Google Gemini Pro and Streamlit.

It fetches data from a Snowflake database. The application allows users to input natural language queries, which are then converted into SQL queries and executed against a Snowflake database. The results are displayed in a user-friendly interface powered by Streamlit.

# Features

 - Natural Language to SQL Conversion: Converts user input from plain English to SQL queries.

 - Google API Integration: Utilizes Google APIs for enhanced processing capabilities.

 - Snowflake Data Fetching: Connects to a Snowflake data warehouse to execute SQL queries and fetch results.
 - Streamlit Interface: Provides an intuitive and interactive user interface for input and result display.
## Run Locally

Clone the project

```bash
  git clone https://github.com/AayushhGoyal/text_tosql.git
```

Go to the project directory

```bash
  cd text_tosql
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

SNOWFLAKE_USER=AYUSHG28
SNOWFLAKE_PASSWORD=Ayush@2003
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_ROLE=ACCOUNTADMIN
SNOWFLAKE_DATABASE=FINANCIAL__ECONOMIC_ESSENTIALS
SNOWFLAKE_ACCOUNT=bxotize-ht12968
GOOGLE_API_KEY="AIzaSyDey7S32FUaJ-4OYuV7RJzLD7lbKwVf8iA"


## Demo

Here's a demo video

https://drive.google.com/file/d/102hOEz_h3VX4CFotcFni9rHZw88wOq9b/view?usp=sharing


In this table you can access
 - C_CUSTKEY
 - C_NAME
 - C_ADDRESS
 - C_NATIONKEY
 - C_PHONE
 - C_ACCTBAL
 - C_MKTSEGMENT
 - C_COMMEN