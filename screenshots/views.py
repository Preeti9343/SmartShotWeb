from django.shortcuts import render
from .utils import load_screenshots_data
from rapidfuzz import fuzz, process

# Load data once
screenshots_data = load_screenshots_data()

def search_screenshots(request):
    query = request.GET.get('q')
    results = []

    if query:
        choices = {item['filename']: item['extracted_text'] for item in screenshots_data}

        # Fuzzy search
        matches = process.extract(query, choices, limit=5, scorer=fuzz.token_sort_ratio)

        for text, score, filename in matches:
            for item in screenshots_data:
                if item['filename'] == filename:
                    results.append({
                        "filename": filename,
                        "image_url": f"screenshots/{filename}",
                        "score": score
                    })
                    break

    return render(request, 'screenshots/search.html', {'results': results, 'query': query})
