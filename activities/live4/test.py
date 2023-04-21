
french_speaking_countries = ["Belgium", "Benin", "Cameroon", "Canada", "Chad", "Ivory Coast", "Djibouti", "Haiti", "Mali", "Monaco", "Niger", "Rwanda", "Senegal"]
english_speaking_countries = ["Cameroon", "Burundi", "Kenya", "Zimbabwe", "Ghana","Djibouti", "Rwanda", "Sudan", "Botswana", "Ethiopia", "Chad","Haiti"]

# to do
only_french = french_speaking_countries.difference(english_speaking_countries)
only_english = english_speacking_countires.difference(french_speaking_countries)


print(f"English-only speaking countries: {only_english}")
print(f"French-only speaking countries:{only_french}")
print(f"Bilingual countries:")
print(f"Monolingual countries:")