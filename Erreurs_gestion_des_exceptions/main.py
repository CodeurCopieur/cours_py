nom = input("Bonjour, quel est votre nom ? ")
age = input("Bonjour, quel est votre âge ? ")

try:
  age_prochain = int(age) + 1
except ValueError:
  print("Erreur: l'âge doit être un nombre entier")
else:
  print(f"vous vous appelez {nom} tu auras {age} ans.")
  print(f"l'an prochain tu auras {age_prochain} ans.")