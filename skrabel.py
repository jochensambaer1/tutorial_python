import requests

def get_word_info(api_key, word):
    base_url = "https://wordsapiv1.p.rapidapi.com/words/"
    headers = {
        'X-RapidAPI-Host': "wordsapiv1.p.rapidapi.com",
        'X-RapidAPI-Key': api_key
    }

    response = requests.get(base_url + word, headers=headers)
    data = response.json()

    return data

def scrabble_score(word):
    # Voeg hier je Words API-sleutel toe
    api_key = "VOEG_HIER_JE_API_SLEUTEL_TOE"

    # Roep de Words API aan voor extra informatie over het woord
    word_info = get_word_info(api_key, word)

    # Haal de Scrabble-score op zoals eerder
    word = word.upper()
    score_table = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
        'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
        'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }

    score = 0
    for letter in word:
        score += score_table.get(letter, 0)

    return score, word_info

# Voorbeeldgebruik
ingevuld_woord = input("Voer het woord in: ")
score, word_info = scrabble_score(ingevuld_woord)
print(f"De Scrabble-score voor '{ingevuld_woord}' is: {score}")

# Toon extra informatie van de Words API
if word_info:
    print("Extra informatie:")
    print("Definitie:", word_info.get("results", {}).get("definition", "Niet beschikbaar"))
    print("Mogelijke synoniemen:", word_info.get("results", {}).get("synonyms", "Niet beschikbaar"))
