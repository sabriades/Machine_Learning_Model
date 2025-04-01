import csv

headers = [
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Fiber", "Fiber Concentration (wt%)",
    "Matrix Density (g/cm³)", "Filler Density (g/cm³)", "Fiber Density (g/cm³)", "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry", "Composite Density (g/cm³)", "Filler Volume Fraction (%)",
    "Elastic Modulus matrix (MPa)", "Elastic Modulus filler (MPa)", "Fiber Volume Fraction (%)", "Friction Coefficient",
    "Tensile Modulus (MPa)", "Impact Strength (kJ/m²)", "Fiber Geometry"
]

composites = [
    [
        "Polyetherimide (PEI)", "Fe₃O₄ microplate (FMP)", 4.76, None, None,
        1.27, 5.18, None, None,
        3104,  # Elastic Modulus (MPa) - Calcolato
        None, None, None, None, None, None,
        None, "Microplate", 1.29, 1.2, 3000, 200000, None, None, None, None, None
    ],
    [
        "Polyetherimide (PEI)", "Fe₃O₄ microplate (FMP)", 7.41, None, None,
        1.27, 5.18, None, None,
        3275,  # Elastic Modulus (MPa) - Calcolato
        None, None, None, None, None, None,
        None, "Microplate", 1.34, 1.9, 3000, 200000, None, None, None, None, None
    ],
    [
        "Polyetherimide (PEI)", "Fe₃O₄ microplate (FMP)", 9.09, None, None,
        1.27, 5.18, None, None,
        3412,  # Elastic Modulus (MPa) - Calcolato
        None, None, None, None, None, None,
        None, "Microplate", 1.40, 2.3, 3000, 200000, None, None, None, None, None
    ],
    [
        "Polyetherimide (PEI)", "Fe₃O₄ microplate (FMP)", 13.04, None, None,
        1.27, 5.18, None, None,
        3798,  # Elastic Modulus (MPa) - Calcolato
        None, None, None, None, None, None,
        None, "Microplate", 1.52, 3.4, 3000, 200000, None, None, None, None, None
    ],
    [
        "Polyetherimide (PEI)", "Fe₃O₄ microplate (FMP)", 16.67, None, None,
        1.27, 5.18, None, None,
        4326,  # Elastic Modulus (MPa) - Calcolato
        None, None, None, None, None, None,
        None, "Microplate", 1.65, 4.5, 3000, 200000, None, None, None, None, None
    ]
]

csv_filename = "PEI_matrix.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(composites)

print(f"File '{csv_filename}' generato. Righe: {len(composites)} | Colonne: {len(headers)}")