--
# Data Analysis Project

## Overview
This project involves data analysis and statistical testing on agricultural and weather datasets. The workflow includes data ingestion, cleaning, mapping, and applying statistical tests to extract meaningful insights.

## Project Structure
- **FieldDataProcessor**: A class to process field data by ingesting SQL data, renaming columns, applying corrections, and merging with weather data.
- **WeatherDataProcessor**: A class to process weather data, including loading data, extracting measurements, and calculating mean values.
- **Data Validation**: Includes test functions to validate the structure and integrity of the weather and field data.
- **Data Manipulation and Visualization**: Tools and libraries for data manipulation and visualization.

## Workflow
1. **Create a Null Hypothesis**: Formulate the null hypothesis for statistical testing.
2. **Import and Clean Field Data**: Import `MD_agric_df` dataset and perform data cleaning.
3. **Import Weather Data**: Load the weather dataset for analysis.
4. **Map Weather Data**: Map the weather data to the field data based on the field IDs.
5. **Calculate Means**: Calculate the mean values for both the weather station dataset and the main dataset.
6. **Perform T-Test**: Calculate parameters needed for a t-test and conduct the test.
7. **Interpret Results**: Analyze and interpret the results of the t-test.

## Key Features
- **Data Ingestion**: Efficiently ingest data from SQL databases and web CSV files.
- **Data Cleaning**: Rename columns and apply necessary corrections to the data.
- **Data Mapping**: Merge datasets based on common identifiers.
- **Statistical Analysis**: Perform t-tests to validate the null hypothesis and interpret results.
- **Logging**: Comprehensive logging for debugging and tracking the data processing steps.
- **Validation**: Ensure the integrity of the data with validation tests.

## Usage
### Field Data Processing
```python
from data_ingestion import create_db_engine, query_data, read_from_web_CSV
from field_data_processor import FieldDataProcessor

config_params = {
    'db_path': 'your_database_path',
    'sql_query': 'your_sql_query',
    'columns_to_rename': {'old_column': 'new_column'},
    'values_to_rename': {'old_value': 'new_value'},
    'weather_mapping_csv': 'path_to_weather_csv'
}

field_processor = FieldDataProcessor(config_params)
field_processor.process()
```

### Weather Data Processing
```python
from weather_data_processor import WeatherDataProcessor

weather_config_params = {
    'weather_csv_path': 'path_to_weather_csv',
    'regex_patterns': {'pattern_key': 'regex_pattern'}
}

weather_processor = WeatherDataProcessor(weather_config_params)
weather_processor.process()
```

### Data Validation
```python
import pytest
from validate_data import *

# Run tests
pytest.main()
```

### Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Plotting example
plt.plot(data['Column1'], data['Column2'])
plt.title('Plot Title')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```


## Contact
For any questions or inquiries, please reach out to `clintonbeye@gmail.com`.

Happy Analyzing! 🚀✨

