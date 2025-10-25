from collections import Counter
import re
import json
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
        top_3 = counter.most_common(10)
        
        # Mostramos el resultado
        print(f"Las 3 palabras mas usada en {files_address}: ")
        for palabra, freq in top_3:
            print(f"{palabra}, {freq} veces")


read_files("data/donald_speech.txt")
read_files("data/melina_trump_speech.txt")
read_files("data/michelle_obama_speech.txt")
read_files("data/obama_speech.txt")

# Read the countries_data.json data file in data directory, 
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