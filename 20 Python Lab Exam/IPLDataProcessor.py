# code me se comments mat hatana, 4 marks comments ke hai
from typing import List, Dict
import pandas as pd
import numpy as np
import re



class IPLDataProcessor:

    def clean_data(self, data: str) -> str:
        # Remove special characters (except spaces)
        cleaned_data = re.sub(r'[^a-zA-Z0-9\s]', '', data)
        # Convert to lowercase
        cleaned_data = cleaned_data.lower()
        # Replace sequences of digits with "<NUM>"
        cleaned_data = re.sub(r'\d+', '<NUM>', cleaned_data)
        return cleaned_data

    def extract_player_stats(self, data: str) -> Dict[str, str]:
        stats = {
            'runs': None,
            'wickets': None,
            'strike rate': None
        }

        # Extract runs
        run_match = re.search(r'(\d+)\s+runs', data)
        if run_match:
            stats['runs'] = run_match.group(1)

        # Extract wickets
        wicket_match = re.search(r'(\d+)\s+wickets', data)
        if wicket_match:
            stats['wickets'] = wicket_match.group(1)

        # Extract strike rate
        strike_rate_match = re.search(r'strike rate of\s+(\d+\.?\d*)', data)
        if strike_rate_match:
            stats['strike rate'] = strike_rate_match.group(1)

        return stats

    def process_numeric_data(self, data: List[float]) -> np.ndarray:
        valid_numbers = []

        # Filter valid float values
        for value in data:
            try:
                if value is not None:
                    valid_numbers.append(float(value))
            except (ValueError, TypeError):
                continue

        # Calculate average of valid numbers
        if valid_numbers:
            average = np.mean(valid_numbers)
        else:
            average = 0

        # Replace invalid entries with the average
        processed_data = [
            float(value) if isinstance(value, (float, int)) else average
            for value in data
        ]

        return np.array(processed_data)

    def analyze_player_performance(self, stats: Dict[str, List[float]]) -> pd.DataFrame:
        # Create DataFrame from stats
        df = pd.DataFrame(stats)

        # Calculate mean for each column
        mean_values = df.mean().to_frame().T
        mean_values.index = [len(df)]  # Set the index of the mean row
        df = pd.concat([df, mean_values], ignore_index=True)

        return df


processor = IPLDataProcessor()

# Example data
raw_data = "Virat Kohli scored 97 runs off 58 balls in the match on 2024-09-15!"
cleaned_data = processor.clean_data(raw_data)
print(cleaned_data)

player_stats = processor.extract_player_stats(cleaned_data)
print(player_stats)

numeric_data = [150.5, 78.1, None, "error", 64.2]
processed_numeric_data = processor.process_numeric_data(numeric_data)
print(processed_numeric_data)

stats_dict = {
    'runs': [50, 78, 64],
    'wickets': [2, 1, 3],
    'strike rate': [140.5, 150.2, 135.6]
}
performance_df = processor.analyze_player_performance(stats_dict)
print(performance_df)



class IPLDataProcessor:
    def clean_data(self, data):
        pattern = r'[^\w\s]'  # remove all special characters
        clean_data = re.sub(pattern, '', data)

        # convert to lowercase
        clean = clean_data.lower()

        # replace any number with <num>
        pattern1 = r'[\d]+'
        new_data = re.sub(pattern1, 'num', clean)
        return new_data

    def extract_player_stats(self, data: str) -> dict[str, str]:
        stat = {
            'runs': None,
            'wickets': None,
            'strike rate': None
        }

        # Extract runs
        pat = r'(\d+)\s+runs'
        run_match = re.search(pat, data)
        if run_match:
            stat['runs'] = run_match.group(1)

        # Extract wickets
        pat1 = r'(\d+)\s+wickets'
        wicket_match = re.search(pat1, data)
        if wicket_match:
            stat['wickets'] = wicket_match.group(1)

        # Extract strike rate
        pat2 = r'strike rate of\s+(\d+\.?\d*)'
        strike_rate_match = re.search(pat2, data)
        if strike_rate_match:
            stat['strike rate'] = strike_rate_match.group(1)

        return stat

    def process_numeric_data(self, data: list[float]):
        valid = []

        # Filter
        for i in data:
            try:
                if i is not None:
                    valid.append(float(i))
            except (ValueError, TypeError) as e:
                continue

        # Calculate average of valid numbers
        if valid:
            avg = np.mean(valid)
        else:
            avg = 0

        # Replace invalid entries with the average
        process_data = [
            float(i) if isinstance(i, (float, int)) else avg
            for i in data
        ]

        return np.array(process_data)

    def analyze_player_performance(self, stats: dict[str, list[float]]):
            # create DataFrame
            df = pd.DataFrame(stats)

            # calculate mean for each col
            mean_value = df.mean().to_frame().T
            mean_value.index = [len(df)]
            df = pd.concat([df, mean_value], ignore_index=True)

            return df


ipl = IPLDataProcessor()
# sample input
data = "Virat Kohli scored 97 runs off 58 balls in the match on 2024-09-15!"
cleaned_data = ipl.clean_data(data)
print("\n")
print(cleaned_data)

print('================================================')
print('\n')

data1 = "virat kohli scored 145 runs with a strike rate of 89"
player_stat = ipl.extract_player_stats(data1)
print(player_stat)

print('\n')
print('================================================')
print('\n')
numeric_data = [150.5, 78.1, None, "error", 64.2]
update_numeric_data = ipl.process_numeric_data(numeric_data)
print(update_numeric_data)


print('\n')
print('================================================')
print('\n')

stats_dict = {
    'runs': [50, 78, 64],
    'wickets': [2, 1, 3],
    'strike rate': [140.5, 150.2, 135.6]
}
performanced_df = ipl.analyze_player_performance(stats_dict)
print(performanced_df)


def clean_data(self, data):
        pattern = r'[^\w\s]'  # remove all special characters
        clean_data = re.sub(pattern, '', data)

        # convert to lowercase
        clean = clean_data.lower()

        # replace any number with <num>
        pattern1 = r'[\d]+'
        new_data = re.sub(pattern1, 'num', clean)
        return new_data




def extract_player_stats(self, data: str) -> dict[str, str]:
        stat = {
            'runs': None,
            'wickets': None,
            'strike rate': None
        }

        # Extract runs
        pat = r'(\d+)\s+runs'
        run_match = re.search(pat, data)
        if run_match:
            stat['runs'] = run_match.group(1)

        # Extract wickets
        pat1 = r'(\d+)\s+wickets'
        wicket_match = re.search(pat1, data)
        if wicket_match:
            stat['wickets'] = wicket_match.group(1)

        # Extract strike rate
        pat2 = r'strike rate of\s+(\d+\.?\d*)'
        strike_rate_match = re.search(pat2, data)
        if strike_rate_match:
            stat['strike rate'] = strike_rate_match.group(1)

        return stat

