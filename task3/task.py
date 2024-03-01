import csv
import numpy as np

def task(csv_content: str) -> float:
    # Load CSV content directly into a NumPy array
    data = np.genfromtxt(csv_content.splitlines(), delimiter=';', dtype=int)

    # Get the dimensions of the matrix
    row_count, col_count = data.shape

    total_entropy = 0
    for row in range(row_count):
        for col in range(col_count):
            value = data[row, col]
            if value != 0:
                # Compute probability
                probability = value / (row_count - 1)
                # Update total entropy
                total_entropy -= probability * np.log2(probability)

    # Round the total entropy to one decimal place
    return round(total_entropy, 1)

csv_path = "./task3.csv"

# Read the content of the CSV file directly
with open(csv_path, 'r') as csvfile:
    csv_content = csvfile.read()

result = task(csv_content)
print(result)
