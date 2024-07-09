from dotenv import load_dotenv
import streamlit as st
import os
import snowflake.connector
import google.generativeai as genai

# Load environment variables
load_dotenv()
SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')
SNOWFLAKE_ROLE = os.getenv('SNOWFLAKE_ROLE')

# Function to connect to Snowflake
def connect_to_snowflake():
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            database='SNOWFLAKE_SAMPLE_DATA',
            warehouse=SNOWFLAKE_WAREHOUSE,
            schema = 'TPCH_SF1',
            role=SNOWFLAKE_ROLE
            
        )
        return conn
    except snowflake.connector.errors.Error as e:
        st.error(f"Error connecting to Snowflake: {str(e)}")
        return None

# Function to execute a query in Snowflake
def execute_snowflake_query(query):
    conn = connect_to_snowflake()
    print (conn)
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return result
        except snowflake.connector.errors.ProgrammingError as e:
            st.error(f"Error executing query: {str(e)}")
        finally:
            conn.close()
    return None

# Configure API key for Google Gemini
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    st.error("API key not found. Please check your environment variables.")
else:
    genai.configure(api_key=api_key)

# Function to load Google Gemini model and provide the query as the response
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content([prompt, question])
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# Streamlit UI setup
st.set_page_config(page_title="I can retrieve Any SQL query")
st.header("Gemini app to retrieve SQL data")

question = st.text_input("Input:", key="input")
submit = st.button("Submit")

if submit:
    prompt = """
    You are an expert in converting English questions to SQL queries! The SQL database is named CUSTOMER and has the following columns: C_CUSTKEY C_NAME C_ADDRESS C_NATIONKEY C_PHONE C_ACCTBAL C_MKTSEGMENT C_COMMENT.

    Example 1: How many entries of records are present?
    SQL command: SELECT COUNT(*) FROM CUSTOMER;

    Example 2: What is the name of the student who has scored the highest marks?
    SQL command: SELECT NAME FROM STUDENT WHERE MARKS = (SELECT MAX(MARKS) FROM CUSTOMER);
    
    The SQL code should not have ``` at the beginning or end and should not contain the word 'sql' in the output.
    """

    response = get_gemini_response(question, prompt)
    if response:
        st.text(f"Generated SQL Query: {response}")
        data = execute_snowflake_query(response)
        if data:
            st.subheader("The response is:")
            for row in data:
                st.text(row)
        else:
            st.error("No data found or error executing the SQL query.")
