import csv

# Definizione degli header
headers = [
    "Polymer Matrix", "Fiber", "Fiber Concentration (wt%)", "Filler", "Filler Concentration (wt%)", "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry", "Flammability Oxygen Index (%)",
    "Self-Burning Time (s)", "Mass Loss at Ignition (%)", "Melt Flow Index (g/10 min)"
]

# Dati dei compositi (solo valori numerici)
data = [
    ["HDPE", "Sisal", None, "Nano-clay", 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ["Epoxy", "Flax", None, "CNTs", 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ["Epoxy", None, None, "MWCNT + nano-diamond", 0.125, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ["LDPE", "OPEFB", None, "CB", 20, None, None, None, None, None, 0.1945, None, None, None, None, None, None, None, None],
    ["Epoxy", None, None, "α-cellulosic micro-filler (Cocos nucifera)", 15, None, None, None, None, None, None, None, 365, None, None, None, None, None, None],
    ["Concrete", None, None, "Biochar", 1, None, None, None, None, None, 0.219, None, None, None, None, None, None, None, None],  # Biochar 1%
    ["Concrete", None, None, "Biochar", 2, None, None, None, None, None, 0.1945, None, None, None, None, None, None, None, None],  # Biochar 2%
    ["Polyurethane", "Kenaf core", None, "TMPS-treated silane", None, None, None, None, None, None, None, None, None, 27, None, None, None, None, None],
    ["Polyurethane", "Kenaf core", None, "Silane", None, None, None, None, None, None, None, None, None, 19, None, None, None, None, None]  # Non trattato
]

# Creazione del file CSV
filename = "spreadsheet_epoly.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Scrive l'header
    writer.writerows(data)  # Scrive i dati

print(f"File CSV '{filename}' generato con successo!")