import pandas as pd
from sys import argv

"""
Validate that input consists of two integers summing to 100 and separated by a space.
"""
def validate_input(user_input):
    benign_percent = int(user_input)
    if benign_percent <= 0 or benign_percent >= 100:
        raise ValueError("Percentage must be in the range 0-100")
    return benign_percent

""""
Run the sampling code. This code does NOT modify the content of each entry.
It just selects entries to include into a new dataset.
"""
def main():
    # Load the KDD dataset
    file_path = "KDDTrain+.txt"  # KDD dataset file path
    
   
    # Read the KDD dataset with the defined columns
    df = pd.read_csv(file_path)

    # Check if the dataset contains a 'class' column
    if 'class' not in df.columns:
        raise ValueError("Dataset must have a 'class' column!") 

    # Separate benign (normal) and malicious (other) data
    benign_df = df[df['class'] == 'normal']
    malicious_df = df[df['class'] != 'normal']  # Everything else is an attack

    # Get and validate user input
    user_input = argv[1]
    result = validate_input(user_input)

    # Populate variables with valid information
    benign_percent = result
    malicious_percent = 100 - benign_percent

    # Calculate number of samples based on user input percentages
    total_size = min(len(benign_df) * 100 // benign_percent, len(malicious_df) * 100 // malicious_percent)
    benign_sample_size = (benign_percent * total_size) // 100
    malicious_sample_size = (malicious_percent * total_size) // 100

    # Sample the required number of benign and malicious entries
    benign_sample = benign_df.sample(n=benign_sample_size, random_state=42)
    malicious_sample = malicious_df.sample(n=malicious_sample_size, random_state=42)

    # Concatenate and shuffle the samples
    new_dataset = pd.concat([benign_sample, malicious_sample]).sample(frac=1, random_state=42)

    # Save the new dataset in the same format as the input
    output_filename = f"KDD-{benign_percent}b-{malicious_percent}m.txt"
    
    # Save without index and header to maintain the original format
    new_dataset.to_csv(output_filename, index=False, header=False)

    # Print when complete
    print(output_filename)
if __name__ == "__main__":
    main()
