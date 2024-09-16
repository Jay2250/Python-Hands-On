import re

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Task 1: Find words that start with a vowel and end with a consonant
    vowels = r'\b[aeiouAEIOU]\w*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]\b'
    task1_words = []

    # Task 2: Extract sequences of digits followed by a non-digit character
    task2_sequences = []

    # Task 3: Identify lines that start with "Note" and end with an exclamation mark
    task3_lines = []

    for line in lines:
        # Task 1: Find words that match the vowel-to-consonant rule
        task1_words.extend(re.findall(vowels, line))

        # Task 2: Find sequences of digits followed by a non-digit
        task2_sequences.extend(re.findall(r'\d+(?=\D)', line))

        # Task 3: Check if the line starts with "Note" and ends with "!"
        if re.match(r'^Note.*!$', line):
            task3_lines.append(line.strip())

    # Printing the results
    print("Task 1: Words starting with a vowel and ending with a consonant")
    print(task1_words)

    print("\nTask 2: Sequences of digits followed by a non-digit character")
    print(task2_sequences)

    print("\nTask 3: Lines starting with 'Note' and ending with an exclamation mark")
    print(task3_lines)

# Provide the path to the file here
file_path = '/mnt/data/file-9WGWj7ll7pXFd4cXpy5BkPUo'
process_file(file_path)