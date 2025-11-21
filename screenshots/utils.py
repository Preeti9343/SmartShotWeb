import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_screenshots_data():
    csv_path = os.path.join(BASE_DIR, 'extracted_text.csv')
    df = pd.read_csv(csv_path)

    data = []
    for _, row in df.iterrows():
        filename = row['filename'].strip()
        data.append({
            "filename": filename,
            "extracted_text": str(row['extracted_text']),
            "image_url": f"screenshots/{filename}"
        })
    return data
