# Saisie des données utilisateur
prenom = input("Quel est ton prénom ? ")
age = int(input("Quel est ton âge ? "))
ville = input("Dans quelle ville habites-tu ? ")
metier = input("Quel est ton métier ? ")

# Calcul de l'âge en jours (approximation)
jours = age * 365

# Affichage
print("\n--- Mini Profil ---")
print(f"Prénom : {prenom}")
print(f"Âge : {age} ans (environ {jours} jours)")
print(f"Ville : {ville}")
print(f"Métier : {metier}")
