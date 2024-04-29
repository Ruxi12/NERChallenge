**README.md**
**Descriere a codului**

În main.py, am creat o funcție pentru a extrage și stoca textul de pe paginile web ale magazinelor de mobilă, folosind bibliotecile requests și BeautifulSoup, apoi am salvat rezultatele într-un fișier CSV, menționând succesul și eșecurile extragerilor.

In analyse_text.py am curățat și prelucrat textul dintr-un fișier CSV conținând conținutul paginilor web, folosind tehnici de procesare a limbajului natural (NLP) cum ar fi eliminarea semnelor de punctuație, transformarea în litere mici, eliminarea stopwords-urilor și lemmatizarea, pentru a obține texte mai relevante din punct de vedere semantic. 
Apoi, am salvat aceste texte curățate într-un fișier JSON, contorizând cazurile de succes și eșec în prelucrarea textelor.

In notebook-ul Jupyter am utilizat modelul pre-antrenat BERT pentru clasificarea tokenurilor. 
Notebook-ul conține următoarele elemente principale:

Setare și Listarea Fișierelor de Date: Inițializează mediul cu bibliotecile necesare pentru manipularea datelor și listarea fișierelor din directorul de intrare, util pentru proiectele desfășurate pe platforma Kaggle.
Importul Bibliotecilor NLP: Importă librăriile esențiale pentru NLP, inclusiv PyTorch și Transformers, pentru a folosi modele BERT în clasificarea tokenurilor. De asemenea, sunt setate variabile de mediu pentru a gestiona avertizările legate de paralelismul tokenizerului.
Funcție de Încărcare a Datelor: Include o funcție pentru citirea datelor dintr-un fișier JSON, extrăgând textele și anotațiile asociate, pregătindu-le pentru procesarea ulterioară.
Funcție de Codificare a Datelor: Procesează și codifică textele pentru compatibilitate cu modelul BERT, pregătind tokenii și etichetele corespunzătoare pentru fiecare token în parte, esențial pentru antrenarea corectă a modelului.
Funcția Principală și Antrenarea Modelului: Orchestrează încărcarea și codificarea datelor, inițializează și configurează modelul BERT pentru clasificarea tokenurilor, setează parametrii de antrenament și execută antrenamentul modelului pe setul de date pregătit. La final, salvează modelul antrenat.
