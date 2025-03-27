import csv

# Header con le caratteristiche e le proprietà
headers = [
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Fiber", "Fiber Concentration (wt%)" , "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry"
]

# Dati dei compositi con percentuali di peso corrette
composites = [
    # [Polymer Matrix, Filler, Filler Concentration, Impact Toughness, Elastic Modulus, Tensile Strength, Flexural Strength, Tensile Strain, Thermal Conductivity, Vicat Heat Resistance, Initiation of Destruction Temp., EMI Shielding Effectiveness, Filler Geometry, Flammability Oxygen Index, Self-Burning Time, Mass Loss at Ignition, Melt Flow Index]
    ["LDPE", "Basalt", 23.08, None, None, 11, None, None, None, None, None, 145, 273, None, "Particulate (≤140 μm)"], #10
    ["LDPE", "Basalt", 28.57, None, None, 39, None, 9.88, None, 250, None, 145, 273, None, "Particulate (≤140 μm)"],
    ["LDPE", "Basalt", 33.33, None, None, 21, None, None, None, None, None, 145, 273, None, "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 23.08, None, None, 60, None, None, None, None, None, 119, 284, None, "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 28.57, None, None, 80, 524, 9.88, None, 250, None, 119, 284, None, "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 33.33, None, None, 60, None, None, None, None, None, 119, 284, None, "Particulate (≤140 μm)"],
    ["PP", "Basalt", 28.57, None, None, None, 1970, 21.50, None, 4.33, None, None, None, None, "Particulate (≤140 μm)"],

#epoly

   # ["HDPE", "Nano-clay", 3, "Sisal", None, None, None, None, None, None, None, None, None, None, None],
    ["Epoxy", "CNTs", 2, "Flax", None, None, None, None, None, None, None, None, None, None, "Nanotubes"],
    ["Epoxy", "MWCNT + nano-diamond", 0.125, None, None, None, None, None, None, None, None, None, None, None,
     "Nanotubes + Nanoparticles"],
    ["LDPE", "CB + nano-clay", 20, "OPEFB", None, None, None, None, None, None, None, None, None, None, "Particulate + Nanoplatelets"],
    ["Epoxy", "α-cellulosic micro-filler (Cocos nucifera)", 15, None, None, None, None, None, None, None, None, None, 365, None, "Micro-powder"],
    ["Concrete", "Biochar", 1, None, None, None, None, None, None, None, 0.219, None, None, None, "Micro-powder"],
    # Biochar 1%
    ["Concrete", "Biochar", 2, None, None, None, None, None, None, None, 0.1945, None, None, None, "Micro-powder"],    # Biochar 2%
    ["Polyurethane", "TMPS-treated silane", None, "Kenaf core", None, None, None, None, None, None, None, None, 365,
     None, "Core-shell"],
    ["Polyurethane", "Silane (Untreated)", None, "Kenaf core", None, None, None, None, None, None, None, None, 350, None, "Agglomerate"],  # Non trattato
    ["PP", None, 40, "Wood flour (513 µm)", None, None, 3200, 21.7, None, None, None, None, None, None, None],
    # Composite 1
    ["Epoxy", None, None, "Sisal + Glass", None, None, None, None, None, None, None, None, None, None, None]


]

# Scrivere i dati nel file CSV
with open('spreadsheet_combo_0.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Scrivere l'header
    writer.writerow(headers)
    # Scrivere i dati dei compositi
    writer.writerows(composites)

print("File CSV creato con successo!")