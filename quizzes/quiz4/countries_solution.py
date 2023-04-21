french_speaking_countries = ["Belgium", "Benin", "Cameroon", "Canada", "Chad", "Ivory Coast", "Djibouti", "Haiti", "Mali", "Monaco", "Niger", "Rwanda", "Senegal"]
english_speaking_countries = ["Cameroon", "Burundi", "Kenya", "Zimbabwe", "Ghana","Djibouti", "Rwanda", "Sudan", "Botswana", "Ethiopia", "Chad","Haiti"]

french_speaking_countries = set(french_speaking_countries)
english_speaking_countries = set(english_speaking_countries)

print(f"English-only speaking countries: {english_speaking_countries - french_speaking_countries}")
print(f"French-only speaking countries: {french_speaking_countries - english_speaking_countries}")
print(f"Bilingual countries: {french_speaking_countries.intersection(english_speaking_countries)}")
print(f"Monolingual countries: {french_speaking_countries.symmetric_difference(english_speaking_countries)}")