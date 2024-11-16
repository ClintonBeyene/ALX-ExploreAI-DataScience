### START FUNCTION
import re
import numpy as np
import pandas as pd
import logging
from DataSetValidation.data_ingestion import read_from_web_CSV

class WeatherDataProcessor:
    def __init__(self, config_params, logging_level="INFO"):
        """
        Initialize the WeatherDataProcessor with configuration parameters and logging level.

        :param config_params: Dictionary containing configuration parameters.
        :param logging_level: Logging level (default is "INFO").
        """
        self.weather_station_data = config_params['weather_csv_path']
        self.patterns = config_params['regex_patterns']
        self.weather_df = None  # Initialize weather_df as None
        self.initialize_logging(logging_level)

    def initialize_logging(self, logging_level):
        """
        Initialize the logger with the specified logging level.

        :param logging_level: Logging level (e.g., "DEBUG", "INFO", "NONE").
        """
        logger_name = __name__ + ".WeatherDataProcessor"
        self.logger = logging.getLogger(logger_name)
        self.logger.propagate = False  # Prevents log messages from being propagated to the root logger

        # Set logging level
        log_level = logging.INFO  # Default to INFO
        if logging_level.upper() == "DEBUG":
            log_level = logging.DEBUG
        elif logging_level.upper() == "NONE":  # Option to disable logging
            self.logger.disabled = True
            return

        self.logger.setLevel(log_level)

        # Only add handler if not already added to avoid duplicate messages
        if not self.logger.handlers:
            ch = logging.StreamHandler()  # Create console handler
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def weather_station_mapping(self):
        """
        Load weather station data from the web and assign it to self.weather_df.
        """
        self.weather_df = read_from_web_CSV(self.weather_station_data)
        self.logger.info("Successfully loaded weather station data from the web.")
        # Here, you can apply any initial transformations to self.weather_df if necessary.

    def extract_measurement(self, message):
        """
        Extract measurement and value from a message using regex patterns.

        :param message: The message string to extract measurements from.
        :return: A tuple (measurement, value) or (None, None) if no match is found.
        """
        for key, pattern in self.patterns.items():
            match = re.search(pattern, message)
            if match:
                self.logger.debug(f"Measurement extracted: {key}")
                return key, float(next((x for x in match.groups() if x is not None)))
        self.logger.debug("No measurement match found.")
        return None, None

    def process_messages(self):
        """
        Process messages in the DataFrame to extract measurements and values.
        """
        if self.weather_df is not None:
            result = self.weather_df['Message'].apply(self.extract_measurement)
            self.weather_df['Measurement'], self.weather_df['Value'] = zip(*result)
            self.logger.info("Messages processed and measurements extracted.")
        else:
            self.logger.warning("weather_df is not initialized, skipping message processing.")
        return self.weather_df

    def calculate_means(self):
        """
        Calculate mean values for each measurement at each weather station.

        :return: DataFrame with mean values.
        """
        if self.weather_df is not None:
            means = self.weather_df.groupby(by=['Weather_station_ID', 'Measurement'])['Value'].mean()
            self.logger.info("Mean values calculated.")
            return means.unstack()
        else:
            self.logger.warning("weather_df is not initialized, cannot calculate means.")
            return None

    def process(self):
        """
        Execute the entire data processing pipeline.
        """
        self.weather_station_mapping()  # Load and assign data to weather_df
        self.process_messages()  # Process messages to extract measurements
        self.logger.info("Data processing completed.")
### END FUNCTION