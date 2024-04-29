import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_page(url):
    try:
        response = requests.get(url, timeout=15, verify=False)  # Mărit timeout-ul și dezactivat verificarea SSL
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text(), True
        else:
            return f"Error: Response status {response.status_code}", False
    except requests.RequestException as e:
        return f"Error: {str(e)}", False

file_path = 'furniture stores pages.csv'
df = pd.read_csv(file_path)
contents = []
success_count = 0
failure_count = 0

for index, url in enumerate(df['max(page)']):
    time.sleep(1)  # Pauză între cereri pentru a reduce riscul de a fi blocat
    content, success = scrape_page(url)
    contents.append(content)
    print(f"Index: {index}, URL: {url[:50]}, Content snippet: {' '.join(content[:200].strip().split())}")  # Afișează indexul și un fragment din conținut
    if success:
        success_count += 1
    else:
        failure_count += 1


print(f"Successfully scraped {success_count} websites.")
print(f"Failed to scrape {failure_count} websites.")
df['page_content'] = contents
output_path = 'scraped_furniture_pages15_.csv'
import csv
df.to_csv(output_path, index=False, escapechar='\\', quoting=csv.QUOTE_ALL)
m