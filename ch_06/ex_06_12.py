# Exercise 06_12 from Deitel: Intro to Python for CS
"""
Use an online translation tool such as Bing Microsoft Translator or Google Translate
to translate English words to another language.
Create a translations dictionary that maps the English words to their translations.
Display a two-column table of translations.
"""

translations = {}
translations.update(milk='молоко',  butter='масло', bread='хлеб', cheese='сыр')

print("EN ===> RU")
for english_word in sorted(translations):
    print(f'{english_word:<10}:{translations[english_word]}')

print("--------------------------------")

print("RU ===> EN")
for english_word, russian_word in sorted(translations.items(), key=lambda x: x[1]):
    print(f"{russian_word:<10}:{english_word}")
