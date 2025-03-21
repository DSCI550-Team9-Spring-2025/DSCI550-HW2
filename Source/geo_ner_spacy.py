pip install spacy pandas
python -m spacy download en_core_web_sm
import pandas as pd
import spacy

# Load spaCy's pre-trained English model
nlp = spacy.load("en_core_web_sm")

# Read the finalized CSV file into a DataFrame
file_path = "finalized_df.csv"
df = pd.read_csv(file_path)

# Function to extract geo names (GPEs) using spaCy
def extract_geo_names(description):
    doc = nlp(description)
    # Extract and return GPE (Geopolitical Entity) named entities
    return [ent.text for ent in doc.ents if ent.label_ == "GPE"]

# Apply the function to the 'description' column and create a new column 'geo_names'
df['geo_names'] = df['description'].apply(lambda x: extract_geo_names(str(x)))

# Save the updated DataFrame to a new CSV file
updated_file_path = "finalized_with_geo_names.csv"
df.to_csv(updated_file_path, index=False)

# Output the first few rows to verify
print(df.head())
