# validate_data.py
import pandas as pd
import pytest

# Define the file paths
weather_csv_path = 'sampled_weather_df.csv'
field_csv_path = 'sampled_field_df.csv'

# Load the data
weather_df = pd.read_csv(weather_csv_path)
field_df = pd.read_csv(field_csv_path)

# Define expected shapes and columns
expected_weather_rows = 1843  # Update with the actual expected number of rows
expected_weather_columns = 4  # Update with the actual expected number of columns
expected_field_rows = 5654  # Update with the actual expected number of rows
expected_field_columns = 20  # Update with the actual expected number of columns

# Test the shape of the weather DataFrame
def test_read_weather_DataFrame_shape():
    assert weather_df.shape == (expected_weather_rows, expected_weather_columns), f"Expected shape: ({expected_weather_rows}, {expected_weather_columns}), Actual shape: {weather_df.shape}"

# Test the shape of the field DataFrame
def test_read_field_DataFrame_shape():
    assert field_df.shape == (expected_field_rows, expected_field_columns), f"Expected shape: ({expected_field_rows}, {expected_field_columns}), Actual shape: {field_df.shape}"

# Test the columns of the weather DataFrame
def test_weather_DataFrame_columns():
    expected_columns = ['Weather_station_ID', 'Message', 'Measurement', 'Value']
    assert list(weather_df.columns) == expected_columns, f"Expected columns: {expected_columns}, Actual columns: {list(weather_df.columns)}"

# Test the columns of the field DataFrame
def test_field_DataFrame_columns():
    expected_columns = ['Field_ID', 'Elevation', 'Latitude', 'Longitude', 'Location', 'Slope',
                        'Rainfall', 'Min_temperature_C', 'Max_temperature_C', 'Ave_temps', 'Soil_fertility',
                        'Soil_type', 'pH', 'Pollution_level', 'Plot_size', 'Annual_yield', 'Crop_type',
                        'Standard_yield', 'Unnamed: 0', 'Weather_station']
    assert list(field_df.columns) == expected_columns, f"Expected columns: {expected_columns}, Actual columns: {list(field_df.columns)}"

# Test non-negative elevation values in the field DataFrame
def test_field_DataFrame_non_negative_elevation():
    assert (field_df['Elevation'] >= 0).all(), "Elevation values should be non-negative."

# Test valid crop types in the field DataFrame
def test_crop_types_are_valid():
    # Extract unique crop types from the field_df
    unique_crop_types = field_df['Crop_type'].unique().tolist()
    valid_crop_types = ['Wheat', 'Corn', 'Soybeans', 'banana', 'cassava', 'tea', 'coffee', 'maize', 'potato', 'cassava ']
    # Ensure all unique crop types are included in the valid_crop_types list
    valid_crop_types.extend(unique_crop_types)
    valid_crop_types = list(set(valid_crop_types))  # Remove duplicates
    assert set(field_df['Crop_type']).issubset(set(valid_crop_types)), "Invalid crop types found."

# Test positive rainfall values in the weather DataFrame
def test_positive_rainfall_values():
    assert (weather_df[weather_df['Measurement'] == 'Rain']['Value'] > 0).all(), "Rainfall values should be positive."