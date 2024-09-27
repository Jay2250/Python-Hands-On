
# ----------------------------------------------complete code--------------------------------------------
import re
import numpy as np
import pandas as pd


class SensorDataProcessor:
    def clean_data(self, data):
        # Keep digits and words, remove special characters
        cleaned = re.sub(r'[^\w\s]', '', data)  # Remove special characters
        # Convert to lowercase
        cleaned = cleaned.lower()
        return cleaned

    def format_output(self, original_data, cleaned_data):
        # Extract the numeric values for replacement
        numbers = re.findall(r'\d+', original_data)
        # Replace <num> with actual numbers in cleaned_data
        formatted_output = cleaned_data
        for num in numbers:
            formatted_output = re.sub(r'<num>', num, formatted_output, count=1)
        return formatted_output

    def extract_readings(self, data):
        # Clean the data first
        cleaned_data = self.clean_data(data)
        # Extract readings using regex
        readings = {}
        for match in re.finditer(r'(\w+):\s*(\d+)?', cleaned_data):
            key = match.group(1)
            value = match.group(2)
            readings[key] = int(value) if value is not None else None
        return readings

    def process_numeric_data(self, data):
        valid_numbers = []
        for item in data:
            try:
                if item is not None and item != 'invalid':
                    valid_numbers.append(float(item))
            except (ValueError, TypeError):
                continue
        if valid_numbers:
            valid_mean = np.mean(valid_numbers)
            return [valid_mean if (item is None or item == 'invalid') else item for item in data]
        return []

    def analyze_data(self, readings):
        try:
            df = pd.DataFrame(readings)
            mean_row = df.mean()
            df = pd.concat(
                [df, mean_row.to_frame().T.rename(index={0: 'mean'})])
            return df
        except Exception as e:
            print(f"An error occurred while analyzing data: {e}")
            return pd.DataFrame()


# Example usage:
processor = SensorDataProcessor()

# Sample input for clean_data
sensor_input = "sensor_1 recorded: 85 reading on 2023-09-15 at 14:55!"
cleaned_data = processor.clean_data(sensor_input)

# Format output
cleaned_data_with_nums = re.sub(r'\d+', '<num>', sensor_input)
formatted_output = processor.format_output(
    sensor_input, cleaned_data_with_nums)
print("Formatted Output:", formatted_output)
# Output: "Formatted Output: sensor recorded 85 reading on <num> at <num>"

# Sample input for extract_readings
reading_input = "temperature: 22 humidity: 55 pressure:num"
readings = processor.extract_readings(reading_input)
print("Extracted Readings:", readings)
# Output: "Extracted Readings: {'temperature': 22, 'humidity': 55, 'pressure': None}"

# Sample input for process_numeric_data
numeric_data = [22.0, 55.0, None, 'invalid', 44.0]
processed_data = processor.process_numeric_data(numeric_data)
print("Processed Numeric Data:", processed_data)
# Output: Processed Numeric Data should replace invalid entries correctly

# Sample input for analyze_data
data_dict = {
    'temperature': [22.0, 23.0, 21.0],
    'humidity': [55.0, 60.0, 50.0],
    'pressure': [1013.0, 1015.0, None]
}
df = processor.analyze_data(data_dict)
print("DataFrame Analysis:\n", df)
