import pytesseract
from PIL import Image
import os
import pandas as pd

# Tesseract path (agar alag jagah install hua hai to update karo)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Screenshot images folder
screenshots_folder = os.path.join("static", "screenshots")

data = []

# OCR loop
for filename in os.listdir(screenshots_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(screenshots_folder, filename)
        try:
            text = pytesseract.image_to_string(Image.open(img_path))
        except Exception as e:
            text = f"Error extracting text: {e}"
        data.append({"filename": filename, "extracted_text": text.strip()})

# Save CSV
df = pd.DataFrame(data)
df.to_csv("extracted_text.csv", index=False)

print("✅ extracted_text.csv created successfully!")
