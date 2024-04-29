import pandas as pd
import json
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Asigură-te că toate pachetele necesare sunt descărcate
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('words')

# Inițializare lemmatizer
lemmatizer = WordNetLemmatizer()

# Obținerea listei de cuvinte valide din limba engleză
english_vocab = set(words.words())

# Funcția pentru curățarea textului avansată
def curata_text_avansat(text):
    if pd.isna(text):
        return ""  # Returnează un string gol dacă textul este NaN

    # Elimină HTML tags
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text(separator=" ")

    # Transformă textul în minuscule
    text = text.lower()

    # Tokenizare
    tokens = word_tokenize(text)

    # Elimină caracterele non-alfabetice și cifrele
    tokens = [word for word in tokens if word.isalpha()]

    # Elimină stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if not word in stop_words]

    # Lemmatizare
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Filtrează cuvintele care nu sunt în dicționarul limbii engleze
    tokens = [word for word in tokens if word in english_vocab]

    return ' '.join(tokens)

# Citirea datelor din fișierul CSV
file_path = 'scraped_furniture_pages15.csv'
df = pd.read_csv(file_path)

# Aplicarea funcției de curățare pe coloana de conținut și crearea unei noi coloane
df['texte_curatate'] = df['page_content'].apply(curata_text_avansat)

# Crearea unui dicționar pentru stocarea indexului și textului curățat
data_to_json = []
fail = 0
succes = 0

for index, row in df.iterrows():
    content = row['texte_curatate']
    if content and "error" not in content.lower() and "httpsconnectionpool" not in content.lower() and "httpconnectionpool" not in content.lower():
        data_to_json.append({"Index": succes, "Content": content})
        succes += 1
    else:
        fail += 1

# Salvarea datelor în format JSON
with open('texte_curatate_avansat_v2.json', 'w', encoding='utf-8') as f:
    json.dump(data_to_json, f, ensure_ascii=False, indent=4)

print(f"fail = {fail}")
print(f"succes = {succes}")
