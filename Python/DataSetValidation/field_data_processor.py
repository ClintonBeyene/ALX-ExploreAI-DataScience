### START FUNCTION
import pandas as pd
from DataSetValidation.data_ingestion import create_db_engine, query_data, read_from_web_CSV
import logging

class FieldDataProcessor:

    def __init__(self, config_params, logging_level="INFO"):
        """
        Initializes the FieldDataProcessor with configuration parameters and sets up logging.

        Parameters:
        - config_params (dict): A dictionary containing configuration parameters such as db_path, sql_query, columns_to_rename, values_to_rename, and weather_mapping_csv.
        - logging_level (str, optional): The logging level to use. Defaults to "INFO".
        """
        self.db_path = config_params['db_path']
        self.sql_query = config_params['sql_query']
        self.columns_to_rename = config_params['columns_to_rename']
        self.values_to_rename = config_params['values_to_rename']
        self.weather_map_data = config_params['weather_mapping_csv']

        self.initialize_logging(logging_level)

        self.df = None
        self.engine = None
        self.weather_data = None

    def initialize_logging(self, logging_level):
        """
        Sets up logging for this instance of FieldDataProcessor.

        Parameters:
        - logging_level (str): The logging level to use. Can be "DEBUG", "INFO", or "NONE" to disable logging.
        """
        logger_name = __name__ + ".FieldDataProcessor"
        self.logger = logging.getLogger(logger_name)
        self.logger.propagate = False  # Prevents log messages from being propagated to the root logger

        if logging_level.upper() == "DEBUG":
            log_level = logging.DEBUG
        elif logging_level.upper() == "INFO":
            log_level = logging.INFO
        elif logging_level.upper() == "NONE":  # Option to disable logging
            self.logger.disabled = True
            return
        else:
            log_level = logging.INFO  # Default to INFO

        self.logger.setLevel(log_level)

        if not self.logger.handlers:
            ch = logging.StreamHandler()  # Create console handler
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def ingest_sql_data(self):
        """
        Ingests data from a SQL database using the provided SQL query.

        Returns:
        - pd.DataFrame: The DataFrame containing the ingested data.
        """
        self.engine = create_db_engine(self.db_path)
        self.df = query_data(self.engine, self.sql_query)
        self.logger.info("Successfully loaded data.")
        return self.df

    def rename_columns(self):
        """
        Renames columns in the DataFrame as specified in the configuration.
        """
        column1, column2 = list(self.columns_to_rename.keys())[0], list(self.columns_to_rename.values())[0]

        temp_name = "__temp_name_for_swap__"
        while temp_name in self.df.columns:
            temp_name += "_"

        self.df = self.df.rename(columns={column1: temp_name, column2: column1})
        self.df = self.df.rename(columns={temp_name: column2})

        self.logger.info(f"Swapped columns: {column1} with {column2}")

    def apply_corrections(self, column_name='Crop_type', abs_column='Elevation'):
        """
        Applies corrections to the DataFrame, such as converting elevation to absolute values and renaming crop types.

        Parameters:
        - column_name (str, optional): The column to apply value renaming to. Defaults to 'Crop_type'.
        - abs_column (str, optional): The column to convert to absolute values. Defaults to 'Elevation'.
        """
        self.df[abs_column] = self.df[abs_column].abs()
        self.df[column_name] = self.df[column_name].apply(lambda crop: self.values_to_rename.get(crop, crop))
        self.logger.info(f"Applied corrections to '{abs_column}' and '{column_name}' columns.")

    def weather_station_mapping(self):
        """
        Reads weather data from a web CSV and stores it in the `weather_data` attribute.
        """
        self.weather_data = read_from_web_CSV(self.weather_map_data)
        self.logger.info("Weather data read successfully from the web.")
        return self.weather_data

    def merge_weather_data(self):
        """
        Merges the weather data with the main DataFrame on the 'Field_ID' column.
        """
        if self.weather_data is not None and 'Field_ID' in self.weather_data.columns:
            self.df = pd.merge(self.df, self.weather_data, on='Field_ID', how='left')
            self.logger.info("Merged weather data with main DataFrame.")
        else:
            self.logger.warning("Weather data not available or missing 'Field_ID' column.")

    def process(self):
        """
        Executes the entire data processing pipeline: ingesting SQL data, renaming columns, applying corrections, mapping weather data, and merging weather data.
        """
        self.ingest_sql_data()
        self.rename_columns()
        self.apply_corrections()
        self.weather_station_mapping()
        self.merge_weather_data()
        
### END FUNCTION