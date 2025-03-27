import csv

# Header con le caratteristiche e le proprietà
headers = [
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry"
]

# Dati dei compositi con percentuali di peso corrette
composites = [
    # [Polymer Matrix, Filler, Filler Concentration, Impact Toughness, Elastic Modulus, Tensile Strength, Flexural Strength, Tensile Strain, Thermal Conductivity, Vicat Heat Resistance, Initiation of Destruction Temp., EMI Shielding Effectiveness, Filler Geometry, Flammability Oxygen Index, Self-Burning Time, Mass Loss at Ignition, Melt Flow Index]
    ["LDPE", "Basalt", 23.08, 11, None, None, None, None, None, 145, 273, None, "Particulate (≤140 μm)"],
    ["LDPE", "Basalt", 28.57, 39, None, 9.88, None, 250, None, 145, 273, None, "Particulate (≤140 μm)"],
    ["LDPE", "Basalt", 33.33, 21, None, None, None, None, None, 145, 273, None, "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 23.08, 60, None, None, None, None, None, 119, 284, None, "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 28.57, 80, 524, 9.88, None, 250, None, 119, 284, None, "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 33.33, 60, None, None, None, None, None, 119, 284, None, "Particulate (≤140 μm)"],
    ["PP", "Basalt", 28.57, None, 1970, 21.50, None, 4.33, None, None, None, None, "Particulate (≤140 μm)"]
]

# Scrivere i dati nel file CSV
with open('polymer_composites_corretto.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Scrivere l'header
    writer.writerow(headers)
    # Scrivere i dati dei compositi
    writer.writerows(composites)

print("File CSV creato con successo!")