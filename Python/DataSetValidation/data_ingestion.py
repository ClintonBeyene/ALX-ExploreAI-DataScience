"""
data_ingestion.py 

This module contains function to ingest and process data from various sources, including SQLite database and csv files.
The primary purpose is to combine data from multiple tables and external databases to create a comprehensive dataset for analysis.

Functions:
- create_db_engine: Create SQLite engine.
- query_data: Query the data from a SQLite database.
- read_from_web_CSV: Loads data from a CSV file.
"""

from sqlalchemy import create_engine, text
import logging
import pandas as pd

# Name our logger so we know that logs from this module come from the data_ingestion module
logger = logging.getLogger('data_ingestion')
# Set a basic logging message up that prints out a timestamp, the name of our logger, and the message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
db_path = 'sqlite:///Maji_Ndogo_farm_survey_small.db'

sql_query = """
SELECT *
FROM geographic_features
LEFT JOIN weather_features USING (Field_ID)
LEFT JOIN soil_and_crop_features USING (Field_ID)
LEFT JOIN farm_management_features USING (Field_ID)
"""

weather_data_URL = "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/Weather_station_data.csv"
weather_mapping_data_URL = "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/Weather_data_field_mapping.csv"

### START FUNCTION

def create_db_engine(db_path):
    """
    Create an SQLite database engine.
    
    Args: 
        db_path (str): Path to the SQLite database.
        
    Returns: 
        salalchemy.engine.base.Engine: The created SQLite engine.
        
    Raises:
        ImportError: If SQLAlchemy is not installed.
        Exception: If the database engine creation fails.
    """
    try:
        engine = create_engine(db_path)
        # Test connection
        with engine.connect() as conn:
            pass
        # test if the database engine was created successfully
        logger.info("Database engine created successfully.")
        return engine # Return the engine object if it all works well
    except ImportError: #If we get an ImportError, inform the user SQLAlchemy is not installed
        logger.error("SQLAlchemy is required to use this function. Please install it first.")
        raise e
    except Exception as e:# If we fail to create an engine inform the user
        logger.error(f"Failed to create database engine. Error: {e}")
        raise e
    
def query_data(engine, sql_query):
    """
    Execute the sqlquery in the database and return the result as a DataFrame.
    
    Args:
        engine (sqlalchemy.engine.base.Engine): The database engine.
        sql_query (str): The SQL query to execute.

    Returns:
        pandas.DataFrame: The result of the SQL query.

    Raises:
        ValueError: If the query returns an empty DataFrame.
        Exception: If an error occurs while querying the database.
    """
    try:
        with engine.connect() as connection:
            df = pd.read_sql_query(text(sql_query), connection)
        if df.empty:
            # Log a message or handle the empty DataFrame scenario as needed
            msg = "The query returned an empty DataFrame."
            logger.error(msg)
            raise ValueError(msg)
        logger.info("Query executed successfully.")
        return df
    except ValueError as e: 
        logger.error(f"SQL query failed. Error: {e}")
        raise e
    except Exception as e:
        logger.error(f"An error occurred while querying the database. Error: {e}")
        raise e
    
def read_from_web_CSV(URL):
    """
    Read a CSV file from web URL into a DataFrame.
    
    Args: 
        URL (str): The URL of the CSV File.
        
    Returns:
        pandas.DataFrame: The DataFrame containging the CSV data.
        
    Raises:
        pd.errors.EmptyDataError: If the URL does not point to a valid CSV file.
        Exception: If an error occurs while reading the CSV file.
    """
    try:
        df = pd.read_csv(URL)
        logger.info("CSV file read successfully from the web.")
        return df
    except pd.errors.EmptyDataError as e:
        logger.error("The URL does not point to a valid CSV file. Please check the URL and try again.")
        raise e
    except Exception as e:
        logger.error(f"Failed to read CSV from the web. Error: {e}")
        raise e
    
### END FUNCTION