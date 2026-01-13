import webbrowser
import requests
import statistics

url_list = [
     'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

""" for url in url_list: 
    webbrowser.open_new_tab(url) """

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)
#print(response.text)
#print(response.status_code)
#print(response.headers)

url_2 = 'https://restcountries.eu/rest/v2/all'
response_2 = requests.get(url_2)
print(response_2.text)

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :

    #the min, max, mean, median, standard deviation of cats' weight in metric units.
    #the min, max, mean, median, standard deviation of cats' lifespan in years.
    #Create a frequency table of country and breed of cats

cat_url = 'https://api.thecatapi.com/v1/breeds'
response_3 = requests.get(cat_url)
cats = response_3.json()

weights = []
lifespans = []
countries = []
breeds = []

for cat in cats:
    # Peso en kg
    if cat.get("weight") and cat["weight"].get("metric"):
        w = cat["weight"]["metric"]
        if "-" in w:
            min_w, max_w = map(float, w.split("-"))
            weights.append((min_w + max_w) / 2)

    # Esperanza de vida
    if cat.get("life_span"):
        l = cat["life_span"]
        if "-" in l:
            min_l, max_l = map(float, l.split("-"))
            lifespans.append((min_l + max_l) / 2)

    # País y raza
    if cat.get("origin"):
        countries.append(cat["origin"])
    if cat.get("name"):
        breeds.append(cat["name"])

print("Weight (kg)")
print("Min:", min(weights))
print("Max:", max(weights))
print("Mean:", statistics.mean(weights))
print("Median:", statistics.median(weights))
print("Std Dev:", statistics.stdev(weights))

print("\nLife Span (years)")
print("Min:", min(lifespans))
print("Max:", max(lifespans))
print("Mean:", statistics.mean(lifespans))
print("Median:", statistics.median(lifespans))
print("Std Dev:", statistics.stdev(lifespans))

from collections import Counter

country_freq = Counter(countries)

print("\nFrequency by country")
for country, count in country_freq.items():
    print(country, ":", count)

breed_freq = Counter(breeds)

print("\nFrequency by breed")
for breed, count in breed_freq.items():
    print(breed, ":", count)