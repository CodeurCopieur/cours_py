# boucle while : tant que la condition est vraie, on exécute le bloc d'instructions

# Exemple 1
i = 0 
while i < 5:
    print(f"la valeur de i est {i}")
    i += 1

# Exemple 2

mdp = ""
while not mdp == "mdp":
    mdp = input("Entrez votre mot de passe: ")
print("Mot de passe correct")

# Programme 

age_pro = 0
while age_pro == 0:
  age = input("Entrez votre age: ")
  try:
    age_pro = int(age) + 1
    age = int(age)
  except:
    print("Veuillez entrer un nombre entier") 
print(f"Votre age est {age}, l'an prochain vous aurez {age_pro} ans")
print("l'an prochain vous aurez " + str(age + 1) + " ans")