import csv

# Header con le nuove colonne aggiunte
headers = [
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Fiber", "Fiber Concentration (wt%)",
    "Matrix Density (g/cm³)", "Filler Density (g/cm³)", "Fiber Density (g/cm³)", "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry"
]

# Dati dei compositi
composites = [
    ["LDPE", "Basalt", 23.08, None, None, 0.925, 2.907, None, 11, None, None, None, None, 145, 273, None,
     "Particulate (≤140 μm)"], #0.910–0.940 g/cm3 - ho preso i valori medi dei range per la densità
    ["LDPE", "Basalt", 28.57, None, None, 0.925, 2.907, None, 39, None, 9.88, None, 250, None, 145, 273, None,
     "Particulate (≤140 μm)"],
    ["LDPE", "Basalt", 33.33, None, None, 0.925, 2.907, None, 21, None, None, None, None, 145, 273, None,
     "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 23.08, None, None, 0.95, 2.907, None, 60, None, None, None, None, 119, 284, None,
     "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 28.57, None, None, 0.95, 2.907, None, 80, 524, 9.88, None, 250, None, 119, 284, None,
     "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 33.33, None, None, 0.95, 2.907, None, 60, None, None, None, None, 119, 284, None,
     "Particulate (≤140 μm)"],
    ["PP", "Basalt", 28.57, None, None, 0.9075, 2.907, None, None, 1970, 21.50, None, 4.33, None, None, None, None,
     "Particulate (≤140 μm)"],

    ["Epoxy", "CNTs", 2, "Flax", None, 1.15, 1.35, 1.47, None, None, None, None, None, None, None, None, "Nanotubes"],
    ["Epoxy", "MWCNT + nano-diamond", 0.125, None, None, 1.15, None, None, None, None, None, None, None, None, None,
     None, "Nanotubes + Nanoparticles"],
    ["LDPE", "CB + nano-clay", 20, "OPEFB", None, 0.925, None, None, None, None, None, None, None, None, None, None,
     "Particulate + Nanoplatelets"],
    ["Epoxy", "α-cellulosic micro-filler (Cocos nucifera)", 15, None, None, 1.15, 0.5, None, None, None, None, None,
     None, 365, None, "Micro-powder"],
    ["Concrete", "Biochar", 1, None, None, 2.41, 1.75, None, None, None, 0.219, None, None, None, None, "Micro-powder"],
    ["Concrete", "Biochar", 2, None, None, 2.41, 1.75, None, None, None, 0.1945, None, None, None, None,
     "Micro-powder"],
    ["Polyurethane", "TMPS-treated silane", None, "Kenaf core", None, 1.15, None, 0.288, None, None, None, None, 365,
     None, "Core-shell"],
    ["Polyurethane", "Silane (Untreated)", None, "Kenaf core", None, 1.15, 0.00134, 0.288, None, None, None, None, 350,
     None, "Agglomerate"],
    ["PP", None, 40, "Wood flour (513 µm)", None, 0.9075, None, 0.205, None, None, 3200, 21.7, None, None, None, None,
     None],
    ["Epoxy", None, None, "Sisal + Glass", None, 1.15, None, None, None, None, None, None, None, None, None, None]
]

# Scrivere i dati nel file CSV con le nuove colonne
with open('spreadsheet_combo_0.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Scrivere l'header
    writer.writerow(headers)
    # Scrivere i dati dei compositi
    writer.writerows(composites)

print("File CSV creato con successo con le nuove colonne vuote!")
