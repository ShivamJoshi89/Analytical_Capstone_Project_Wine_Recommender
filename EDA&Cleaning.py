import pandas as pd  # For data manipulation and analysis


df = pd.read_csv('wine_data_with_images.csv', on_bad_lines='skip')

print(df.columns)

print(df.info())

# Check for duplicate product links
duplicates = df[df.duplicated("Product Link", keep=False)]  # Keep all duplicates

# Print the total number of duplicates
total_duplicates = len(duplicates)
print(f"Total number of duplicate product links: {total_duplicates}")

# Drop duplicates (keep the first occurrence)
df_cleaned = df.drop_duplicates("Product Link", keep="first")

# Save the cleaned data to a new CSV file
cleaned_csv_path = 'cleaned_wine_data.csv'
df_cleaned.to_csv(cleaned_csv_path, index=False)
print(f"✅ Cleaned data saved to '{cleaned_csv_path}'.")

# Verify that duplicates have been removed
remaining_duplicates = df_cleaned[df_cleaned.duplicated("Product Link", keep=False)]
print(f"Total number of duplicates after cleaning: {len(remaining_duplicates)}")

print(df.shape) #Shape Of the Dataset