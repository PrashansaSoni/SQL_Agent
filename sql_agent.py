
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_groq import ChatGroq  

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DB")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

password_encoded = quote_plus(MYSQL_PASSWORD)
mysql_uri = f"mysql+pymysql://{MYSQL_USER}:{password_encoded}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# Connect to SQL database
db = SQLDatabase.from_uri(mysql_uri, include_tables=["sales"])

# Load Groq model
llm = ChatGroq(api_key=GROQ_API_KEY, model_name="llama3-70b-8192")

# Build toolkit & agent
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent = create_sql_agent(
    llm=llm, 
    toolkit=toolkit, 
    verbose=True, 
    handle_parsing_errors=True
    )


def ask_sql_agent(question: str):
    return agent.invoke({"input": question})
