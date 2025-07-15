distance = float(input("Distance (km) : "))
temps = float(input("Temps (h) : "))

# Calcul des vitesses
vitesse_kmh = distance / temps
vitesse_ms = (distance * 1000) / (temps * 3600)

# Affichage
print(f"Vitesse moyenne : {vitesse_kmh:.2f} km/h")
print(f"Vitesse moyenne : {vitesse_ms:.2f} m/s")

