from googlesearch import search
import csv

# Define your search query
query = "site:business.site"

# Perform the search
# Note: The actual implementation here doesn't enforce country-based filtering.
# You would typically need to use the Google Custom Search JSON API with the `cr` parameter for country restrictions.
search_results = search(query, verify_ssl=False)

# Write search results to a CSV file
with open('search_results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['URL'])  # Write header
    for url in search_results:
        writer.writerow([url])

print("Search results have been written to search_results.csv")