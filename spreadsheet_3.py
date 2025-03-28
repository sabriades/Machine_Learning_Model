import csv


headers = [
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Fiber", "Fiber Concentration (wt%)",
    "Matrix Density (g/cm³)", "Filler Density (g/cm³)", "Fiber Density (g/cm³)", "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry"
]


data = [
    # Composito con 5 phr di FMP
    [
        "Polyetherimide (PEI)",  # Polymer Matrix
        "Fe₃O₄ microplate (FMP)",  # Filler
        20.57,  # Filler Concentration (wt%) = 5 phr
        None,  # Fiber
        None,  # Fiber Concentration (wt%)
        None,  # Matrix Density (g/cm³)
        5.17,  # Filler Density (g/cm³)
        None,  # Fiber Density (g/cm³)
        None,  # Impact Toughness (kJ/m²)
        None,  # Elastic Modulus (MPa)
        None,  # Tensile Strength (MPa)
        None,  # Flexural Strength (MPa)
        None,  # Tensile Strain (%)
        None,  # Thermal Conductivity (W/m·K)
        None,  # Vicat Heat Resistance (°C)
        None,  # Initiation of Destruction Temp. (°C)
        None,  # EMI Shielding Effectiveness (dB)
        "nanoplate"  # Filler Geometry
    ],
    # Composito con 8 phr di FMP
    [
        "Polyetherimide (PEI)",  # Polymer Matrix
        "Fe₃O₄ microplate (FMP)",  # Filler
        29.28,  # Filler Concentration (wt%) = 8 phr
        None,  # Fiber
        None,  # Fiber Concentration (wt%)
        None,  # Matrix Density (g/cm³)
        5.17,  # Filler Density (g/cm³) #ho cercanto la densità di Fe₃O₄
        None,  # Fiber Density (g/cm³)
        None,  # Impact Toughness (kJ/m²)
        None,  # Elastic Modulus (MPa)
        None,  # Tensile Strength (MPa)
        None,  # Flexural Strength (MPa)
        None,  # Tensile Strain (%)
        None,  # Thermal Conductivity (W/m·K)
        None,  # Vicat Heat Resistance (°C)
        None,  # Initiation of Destruction Temp. (°C)
        None,  # EMI Shielding Effectiveness (dB)
        "nanoplate"  # Filler Geometry
    ],
    # Composito con 10 phr di FMP
    [
        "Polyetherimide (PEI)",  # Polymer Matrix
        "Fe₃O₄ microplate (FMP)",  # Filler
        34.06,  # Filler Concentration (wt%) = 10 phr
        None,  # Fiber
        None,  # Fiber Concentration (wt%)
        None,  # Matrix Density (g/cm³)
        5.17,  # Filler Density (g/cm³)
        None,  # Fiber Density (g/cm³)
        None,  # Impact Toughness (kJ/m²)
        None,  # Elastic Modulus (MPa)
        None,  # Tensile Strength (MPa)
        None,  # Flexural Strength (MPa)
        None,  # Tensile Strain (%)
        None,  # Thermal Conductivity (W/m·K)
        None,  # Vicat Heat Resistance (°C)
        None,  # Initiation of Destruction Temp. (°C)
        None,  # EMI Shielding Effectiveness (dB)
        "nanoplate"  # Filler Geometry
    ],
    # Composito con 15 phr di FMP
    [
        "Polyetherimide (PEI)",  # Polymer Matrix
        "Fe₃O₄ microplate (FMP)",  # Filler
        43.69,  # Filler Concentration (wt%) = 15 phr
        None,  # Fiber
        None,  # Fiber Concentration (wt%)
        None,  # Matrix Density (g/cm³)
        5.17,  # Filler Density (g/cm³)
        None,  # Fiber Density (g/cm³)
        None,  # Impact Toughness (kJ/m²)
        None,  # Elastic Modulus (MPa)
        None,  # Tensile Strength (MPa)
        None,  # Flexural Strength (MPa)
        None,  # Tensile Strain (%)
        None,  # Thermal Conductivity (W/m·K)
        None,  # Vicat Heat Resistance (°C)
        None,  # Initiation of Destruction Temp. (°C)
        None,  # EMI Shielding Effectiveness (dB)
        "nanoplate"  # Filler Geometry
    ],
    # Composito con 20 phr di FMP
    [
        "Polyetherimide (PEI)",  # Polymer Matrix
        "Fe₃O₄ microplate (FMP)",  # Filler
        50.85,  # Filler Concentration (wt%) = 20 phr
        None,  # Fiber
        None,  # Fiber Concentration (wt%)
        None,  # Matrix Density (g/cm³)
        5.17,  # Filler Density (g/cm³)
        None,  # Fiber Density (g/cm³)
        None,  # Impact Toughness (kJ/m²)
        None,  # Elastic Modulus (MPa)
        None,  # Tensile Strength (MPa)
        None,  # Flexural Strength (MPa)
        None,  # Tensile Strain (%)
        None,  # Thermal Conductivity (W/m·K)
        None,  # Vicat Heat Resistance (°C)
        None,  # Initiation of Destruction Temp. (°C)
        None,  # EMI Shielding Effectiveness (dB)
        "nanoplate"  # Filler Geometry
    ]
]


with open('spreadsheet_3.csv', mode='w', newline='') as file:
    writer = csv.writer(file)


    writer.writerow(headers)


    for row in data:
        writer.writerow(row)

print("CSV file 'composite_properties.csv' created successfully.")
