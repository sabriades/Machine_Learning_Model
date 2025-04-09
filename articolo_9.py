import csv

headers = [
    # Material properties
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Fiber", "Fiber Concentration (wt%)",
    "Matrix Density (g/cm³)", "Filler Density (g/cm³)", "Fiber Density (g/cm³)", "Impact Toughness (kJ/m²)",

    # Mechanical properties
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",

    # Thermal properties
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",

    # EMI properties
    "EMI Shielding Effectiveness (dB)",

    # Filler characteristics
    "Filler Geometry", "Composite Density (g/cm³)", "Filler Volume Fraction (%)",

    # Moduli and fractions
    "Elastic Modulus matrix (MPa)", "Elastic Modulus filler (MPa)", "Fiber Volume Fraction (%)", "Friction Coefficient",

    # Additional mechanical
    "Tensile Modulus (MPa)", "Impact Strength (kJ/m²)", "Fiber Geometry",

    # Stress/strain properties
    "Offset Yield Stress (MPa)", "Fatigue Durability (cycles)", "Glass Transition Temperature (°C)",

    # Material characteristics
    "Linear Expansion Coefficient (1/°C)", "Oxygen Index (%)", "Rockwell Hardness (M)",
    "Mode II Interlaminar Fracture Toughness (kJ/m²)",

    # Hardness/resilience
    "Hardness (Shore D)", "Rebound Resilience (%)", "Brittleness (10^10/%·Pa)",

    # Thermal properties
    "Melting Temperature (°C)", "Crystallization Temperature (°C)", "Onset Crystallization Temperature (°C)",
    "Melting Enthalpy (J/g)", "Crystallinity Degree (%)",

    # Dynamic mechanical
    "Storage Modulus E′ at 25°C (MPa)", "Loss Modulus E″ at 25°C (MPa)", "tan δ at 25°C",

    # Processing properties
    "Melt Flow Index (g/10 min)", "Porosity (%)", "Adhesion Factor",

    # Dielectric properties
    "Dielectric Constant (1 kHz, RT)", "Dielectric Constant (1 kHz, 150°C)",
    "Breakdown Strength (MV/m, RT)", "Breakdown Strength (MV/m, 150°C)",
    "Energy Density (J/cm³, RT)", "Energy Density (J/cm³, 150°C)",
    "Efficiency (%) RT", "Efficiency (%) 150°C",

    # Charge transport
    "Hopping Distance (RT)", "Hopping Distance (150°C)",
    "Trap Depth (eV)", "Trapped Charge (nC)", "Cyclic Stability at 150°C (cycles)",

    # Dielectric loss
    "Dielectric Loss (tanδ, 1 kHz, RT)", "Dielectric Loss (tanδ, 1 kHz, 150°C)",

    # Conductivity
    "AC Conductivity (σ_AC, S/cm, RT)", "AC Conductivity (σ_AC, S/cm, 150°C)",

    # Surface properties
    "Zeta Potential KLNS Lamellae (mV)", "Zeta Potential KLNS Edges (mV)", "Zeta Potential NTCDA (mV)"
]

rows = [
    [  # KLNS/PEI Monolayer (0.2 wt%)
        # Material properties
        "Polyetherimide (PEI)", "KLNS", 0.2, None, None,
        None, None, None, None,

        # Mechanical properties
        None, None, None, None,

        # Thermal properties
        None, None, None,

        # EMI properties
        None,

        # Filler characteristics
        "Nanosheets (~3 nm thick, ~0.87 µm diameter, aspect ratio ~290, negatively charged lamellae / +7.04 mV edges",
        None, None,

        # Moduli and fractions
        None, None, None, None,

        # Additional mechanical
        None, None, None,

        # Stress/strain properties
        None, None, 217,

        # Material characteristics
        None, None, None, None,

        # Hardness/resilience
        None, None, None,

        # Thermal properties
        None, None, None,
        None, None,

        # Dynamic mechanical
        None, None, None,

        # Processing properties
        None, None, None,

        # Dielectric properties
        3.61, 3.41,
        571.2, 474.7,
        4.1, 3.2,
        88.4, 82.3,

        # Charge transport
        0.96, 1.24,
        None, None, None,

        # Dielectric loss
        0.015, 0.006,

        # Conductivity
        "<1e-12", "1.2e-12",

        # Surface properties
        -25.97, 7.04, None
    ],
    [  # Sandwich KLNS (0.2 wt%) + NTCDA (0.5 wt%)
        # Material properties
        "Polyetherimide (PEI)", "KLNS + NTCDA", "0.2 (KLNS middle) + 0.5 (NTCDA outer layers)", None, None,
        None, None, None, None,

        # Mechanical properties
        None, None, None, None,

        # Thermal properties
        None, None, None,

        # EMI properties
        None,

        # Filler characteristics
        "Nanosheets + Irregular π-conjugated n-type semiconductor blocks (1-20 µm)",
        None, None,

        # Moduli and fractions
        None, None, None, None,

        # Additional mechanical
        None, None, None,

        # Stress/strain properties
        None, 100000, 217,

        # Material characteristics
        None, None, None, None,

        # Hardness/resilience
        None, None, None,

        # Thermal properties
        None, None, None,
        None, None,

        # Dynamic mechanical
        None, None, None,

        # Processing properties
        None, None, None,

        # Dielectric properties
        3.88, 3.70,
        591.9, 580.1,
        5.3, 5.0,
        89.3, 88.7,

        # Charge transport
        0.62, 1.01,
        2.25, 51.8, 100000,

        # Dielectric loss
        0.006, 0.005,

        # Conductivity
        "<1e-12", "1.2e-12",

        # Surface properties
        -25.97, 7.04, 9.86
    ]
]

with open("9.csv", mode="w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("CSV file '9.csv' generated successfully with perfect alignment.")