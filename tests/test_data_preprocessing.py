import re
import pandas as pd

# Sample data
data = [
    """Under armour Goretex
    Size 40,41,42,43
    Price 3500 birr
    📌አድራሻ-ሜክሲኮ ኮሜርስ ጀርባ መዚድ ፕላዛ የመጀመሪያ ደረጃ እንደወጡ 101 የቢሮ ቁጥር ያገኙናል or call 0920238243
    [EthioBrand](https://t.me/ethio_brand_collection) ✅""",
    """🥳ለጥምቀት እንዲሁም ለተለያዩ በዓላት ወይም ፕሮግራም የሚሆኑ ፥
    White Sandals  
    Size 40,41,42,43,44
    Price 1900 birr
    📌አድራሻ-ሜክሲኮ ኮሜርስ ጀርባ መዚድ ፕላዛ የመጀመሪያ ደረጃ እንደወጡ 101 የቢሮ ቁጥር ያገኙናል or call 0920238243
    [EthioBrand](https://t.me/ethio_brand_collection) ✅""",
    # Add more data entries here...
]

# Preprocessor function
def data_preprocessor(data_list):
    cleaned_data = []
    for item in data_list:
        # Remove English words
        item = re.sub(r'\b[a-zA-Z]+\b', '', item)
        
        # Remove links
        item = re.sub(r'https?:\/\/\S+', '', item)
        
        # Remove emojis and special characters
        item = re.sub(r'[^\w\s።፣፥፦፤፨፡፠]', '', item)
        
        # Remove unnecessary spaces
        item = re.sub(r'\s+', ' ', item).strip()
        
        # Add to cleaned data if not NaN or empty
        if item and item.lower() != 'nan':
            cleaned_data.append(item)
    
    return cleaned_data

# Preprocess the data
cleaned_data = data_preprocessor(data)

# Convert to DataFrame for better visualization or further processing
df = pd.DataFrame({'Cleaned Text': cleaned_data})

# Save to a CSV file
df.to_csv('cleaned_data.csv', index=False)

# Print the cleaned data
print(df)
