# Saisie de la durée
heures = int(input("Heures : "))
minutes = int(input("Minutes : "))
secondes = int(input("Secondes : "))

# Conversion
total_secondes = heures * 3600 + minutes * 60 + secondes

# Affichage
print(f"Durée totale en secondes : {total_secondes} s")

