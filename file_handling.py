from collections import Counter
import re
import json
import os
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv
# Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words

STOPWORDS = {
    "the", "and", "to", "of", "a", "in", "that", "is", "it", "for",
    "on", "with", "as", "was", "at", "by", "an", "be", "this", "are",
    "or", "from", "but", "not", "have", "had", "has", "they", "you",
    "we", "our", "their", "will", "can", "would", "should", "do", "did"
}

def read_files(files_address):
    # Abrimos el archivo en modo lectura ("r"), con codificación UTF-8
    with open(files_address, "r", encoding="utf-8") as f: 
        # Leemos todas las líneas del archivo en una lista
        lines = f.readlines()
        
        # Contamos la cantidad de líneas (tamaño de la lista "lines")
        cantidad_de_lineas = len(lines)
        print(f"Cantidad de lineas en {files_address}: {cantidad_de_lineas}")
        
        # Contamos la cantidad de palabras sumando las palabras de cada línea
        cantidad_de_palabras = sum(len(line.split()) for line in lines)
        print(f"Cantidad de palabras en {files_address}: {cantidad_de_palabras}")
        
        # Unimos todas las líneas en un solo texto y lo pasamos a minúsculas
        full_text = " ".join(lines).lower()
        
        # Usamos una expresión regular para extraer solo palabras (ignorando signos de puntuación)
        palabras = re.findall(r"\b\w+\b", full_text)
        
        # Filtramos las palabras, eliminando las "stopwords" (palabras vacías como "the", "and", "to", etc.)
        palabras_filtradas = [p for p in palabras if p not in STOPWORDS]
        
        # Contamos la frecuencia de cada palabra filtrada con Counter
        counter = Counter(palabras_filtradas)
        
        # Obtenemos las 3 palabras más comunes
        top_3 = counter.most_common(3)
        
        # Mostramos el resultado
        print(f"Las 3 palabras mas usada en {files_address}: ")
        for palabra, freq in top_3:
            print(f"{palabra}, {freq} veces")


read_files("data/donald_speech.txt")
read_files("data/melina_trump_speech.txt")
read_files("data/michelle_obama_speech.txt")
read_files("data/obama_speech.txt")

# Read the countries_data.json data le in data directory, 
# create a function that finds the ten most spoken languages
def most_spoken_langauges(filename, top_n=10): 
    with open(filename, "r", encoding="utf-8") as f: 
        countries = json.load(f)
        all_languages = []
        for country in countries: 
            all_languages.extend(country.get("languages", []))
        counter = Counter(all_languages)
        return [(count, lang) for lang, count in counter.most_common(top_n)]

print(most_spoken_langauges("data/countries_data.json", top_n=10))

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
local_path = "data/email_exchanges_big.txt"
url = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/email_exchanges_big.txt"

def download_file_if_not_exists(url, local_path):
    if not os.path.exists(local_path):
        print("Archivo no encontrado. Descargando desde GitHub...")
        response = requests.get(url)
        response.raise_for_status()  # lanza error si falla
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Descarga completa.")
    else:
        print("El archivo ya existe localmente.")


def read_incoming_emails(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        # Aquí haces lo que necesites con el contenido
        pattern = r"^From:\s*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})"
        return re.findall(pattern, content, flags=re.MULTILINE)


# Ejecución completa
download_file_if_not_exists(url, local_path)
emails = read_incoming_emails(local_path)
print(f"Total de e-mails {len(emails)}") 
print(emails[:10])

# Find the most common words in the English language.
# Call the name of your function find_most_common_words, 
# it will take two parameters - a string or a file and a positive integer, indicating the number of words. 
# Your function will return an array of tuples in descending order. Check the output
def find_most_comon_words(source, number):
    if os.path.exists(source):
        with open(source, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = source

    # 2. Convertir a minúsculas y extraer palabras con regex
    words = re.findall(r"[A-Za-z']+", text.lower())

    # 3. Contar palabras
    counter = Counter(words)

    # 4. Retornar las N más comunes como lista de tuplas
    return counter.most_common(number)

print(find_most_comon_words(local_path, 1))
print(find_most_comon_words(f"data/donald_speech.txt", 10))
print(find_most_comon_words("data/melina_trump_speech.txt", 10))

# Write a python application that checks similarity between two texts.
#  It takes a file or a string as a parameter and it will evaluate the similarity
#  of the two texts. For instance check the similarity between the transcripts of 
# Michelle's and Melina's speech. You may need a couple of functions, 
# function to clean the text(clean_text), function to remove support words(remove_support_words) and 
# finally to check the similarity(check_text_similarity). List of stop words are in the data directory

# =====================================================
# 1. Carga de texto desde archivo o string
# =====================================================
def load_text(src):
    if os.path.exists(src):
        with open(src, "r", encoding="utf-8") as f:
            return f.read()
    return src


# =====================================================
# 2. Limpieza avanzada del texto
# =====================================================
def clean_text(text):
    text = text.lower()
    # Mantener solo letras y apostrofes dentro de palabras
    text = re.sub(r"[^a-z\s']", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text





# =====================================================
# 4. Remover stopwords
# =====================================================
def remove_support_words(words, stopwords):
    return [w for w in words if w not in stopwords]


# =====================================================
# 5. Extraer palabras clave usando TF-IDF
# =====================================================
def extract_keywords(text, top_n=10):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text])
    scores = tfidf.toarray()[0]

    words = vectorizer.get_feature_names_out()
    word_scores = list(zip(words, scores))

    # Ordenar y devolver los más importantes
    ranked = sorted(word_scores, key=lambda x: x[1], reverse=True)
    return ranked[:top_n]


# =====================================================
# 6. Encontrar palabras en común entre dos textos
# =====================================================
def common_words(text1_words, text2_words, top_n=20):
    set1 = Counter(text1_words)
    set2 = Counter(text2_words)

    common = set(set1.keys()) & set(set2.keys())

    common_ranked = []
    for w in common:
        common_ranked.append((w, set1[w] + set2[w]))

    return sorted(common_ranked, key=lambda x: x[1], reverse=True)[:top_n]


# =====================================================
# 7. Función principal de similitud de textos
# =====================================================
def check_text_similarity(text1_src, text2_src, stopwords):
    # Load
    t1 = load_text(text1_src)
    t2 = load_text(text2_src)

    # Clean
    t1c = clean_text(t1)
    t2c = clean_text(t2)

    # Words
    w1 = t1c.split()
    w2 = t2c.split()

    # Stopwords
    w1 = remove_support_words(w1, stopwords)
    w2 = remove_support_words(w2, stopwords)

    f1 = " ".join(w1)
    f2 = " ".join(w2)

    # Similarity
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([f1, f2])
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    # Extra metrics
    keywords_1 = extract_keywords(f1)
    keywords_2 = extract_keywords(f2)
    common = common_words(w1, w2)

    return {
        "similarity": similarity,
        "keywords_text1": keywords_1,
        "keywords_text2": keywords_2,
        "common_words": common
    }

result = check_text_similarity(
    "data/michelle_speech.txt",
    "data/melina_speech.txt",
    stopwords= STOPWORDS
)

print("Similarity:", result["similarity"])
print("\nTop palabras clave texto 1:", result["keywords_text1"])
print("\nTop palabras clave texto 2:", result["keywords_text2"])
print("\nPalabras en común:", result["common_words"])

# Find the 10 most repeated words in the romeo_and_juliet.txt
url_1 = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/refs/heads/master/data/romeo_and_juliet.txt"
local_path_1 = "data/romeo_and_juliet"
download_file_if_not_exists(url_1, local_path_1)
print(find_most_comon_words("data/romeo_and_juliet", 10))

# Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript
url_2 = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/refs/heads/master/data/hacker_news.csv"
local_path_2 = "data/hacker_news"
download_file_if_not_exists(url_2, local_path_2)

def read_hacker_file(file_path, words):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    lower_lines = [line.lower() for line in lines]

    counter = sum(words in line for line in lower_lines)

    return counter

print(f"Python en archivos {read_hacker_file("data/hacker_news", "python")}")
print(f"Javascript en archivos {read_hacker_file("data/hacker_news", "Javascript")}")
print(f"Java en archivos {read_hacker_file("data/hacker_news", "java")}")


    