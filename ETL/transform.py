import csv
from datetime import datetime
import os

def transform_data(input_file, output_file):
    # Check if the file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

            # Read input file and prepare to write output
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ['domain']  # Add a new 'domain' column
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                try:
                    # Convert 'signup_date' to 'YYYY-MM-DD'
                    row['signup_date'] = datetime.strptime(row['signup_date'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

                    # Extract the domain from the email
                    if '@' in row['email']:
                        row['domain'] = row['email'].split('@')[1]
                    else:
                        row['domain'] = None  # Handle cases where email is invalid

                    # Write the transformed row to the output file
                    writer.writerow(row)
                except Exception as e:
                    print(f"Warning: Skipping row due to error: {row}. Details: {e}")

    except Exception as e:
        print(f"Error: Failed to process the file. Details: {e}")
        return

    print(f"Transformed data saved to '{output_file}'.")

if __name__ == "__main__":
    # Define input and output file paths
    input_file = "data/data.csv"           # Path to the input file
    output_file = "data/transformed.csv"  # Path to the output file
    transform_data(input_file, output_file)
