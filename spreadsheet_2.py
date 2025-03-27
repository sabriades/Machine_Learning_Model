import csv

headers = [
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Fiber", "Fiber Concentration (wt%)",
    "Matrix Density (g/cm³)", "Filler Density (g/cm³)", "Fiber Density (g/cm³)", "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry"
]

# List of composites, each as a row corresponding to the header
# For values with uncertainty (e.g., "38.5±2.9"), only the central value is used.
composites = [
    # 1. Conductive Polymer Composites
    [
        "Butyl rubber (IIR)",               # Polymer Matrix
        "Low-density polyethylene (PE)",    # Filler
        10,                               # Filler Concentration (wt%) as given
        None,                               # Fiber
        None,                               # Fiber Concentration (wt%)
        None, None, None, None, None, None, None, None, None, None, None,
        "50–60",                            # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    # 2. Carbon Black-Based Composites
    [
        "Chlorinated polyethylene (CPE)",   # Polymer Matrix
        "Ketjen carbon black (K-CB)",         # Filler
        30,                               # Filler Concentration (wt%)
        None, None, None, None, None, None, None, None, None, None, None, None,
        38.4,                             # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "Phenolic resin",                   # Polymer Matrix
        "Carbon black (CB) nanoparticles",   # Filler
        None,                               # Filler Concentration (wt%) unspecified
        None, None, None, None, None, None, None, None, None, None, None, None,
        "30–40",                            # EMI Shielding Effectiveness (dB)
        "nanoparticles"                     # Filler Geometry
    ],
    # 3. Graphene-Based Composites
    [
        "Epoxy",                           # Polymer Matrix
        "Graphene",                        # Filler
        15,                              # Filler Concentration (wt%)
        None, None, None, None, None, None, None, None, None, None, None, None,
        "20–21",                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "PMMA",                            # Polymer Matrix
        "Graphene",                        # Filler
        3.30,  # era dato in 1.8 vol%, convertito poi in wt%   # Filler Concentration (wt%)
        None, None, 1.18, 2.2, None, None, None, None, None, None, None, None,
        "13–19",                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry
    ],
    [
        "PEI (polyetherimide)",            # Polymer Matrix
        "Graphene@Fe₃O₄",                  # Filler
        10,                              # Filler Concentration (wt%)
        None, None, None, None, None, None, None, None, None, None, None, None,
        41.5,                            # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry
    ],
    # 4. Carbon Fiber (CF) Composites
    [
        "Nylon 6,6",                       # Polymer Matrix
        None,
        None,
        "Long carbon fibers",              # Fiber
        30,    # Fiber Concentration (wt%)
        None, None, None, None, None, None, None, None, None, None, None,
        "45–75",                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "Polysulfone (PSU)",               # Polymer Matrix
        None,                              # Filler (not applicable)
        None,
        "Carbon nanofibers (CNF)",           # Fiber
        10,                              # Fiber Concentration (wt%)
        None, None, None, None, None, None, None, None, None, None, None,
        "19–45",                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    # 5. MWCNT-Based Composites
    [
        "PANI",                            # Polymer Matrix
        "MWCNTs",                          # Filler
        7,                               # Filler Concentration (wt%)
        None, None, None, None, None, None, None, None, None, None, None, None,
        "27.5–39.2",                       # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "PVDF",                            # Polymer Matrix
        "MWCNTs",                          # Filler
        15,                              # Filler Concentration (wt%)
        None, None, None, None, None, None, None, None, None, None, None, None,
        56,                              # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "Epoxy",                           # Polymer Matrix
        "Reduced graphene oxide (rGO)-CF + Fe₃O₄ nanoparticles",  # Filler
        None,                              # Filler Concentration (wt%) not provided
        None, None, None, None, None, None, None, None, None, None, None, None,
        "31.3–51.1",                       # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry not provided
    ],
    # 6. MXene-Based Composites
    [
        "PANI-PpAP",                      # Polymer Matrix
        "MXene",                          # Filler
        None,                             # Filler Concentration (wt%) unspecified
        None, None, None, None, None, None, None, None, None, None, None, None,
        "45.18",                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "PDMS",                           # Polymer Matrix
        "MXene foam",                     # Filler
        None,  # Note: provided as 2 mm thickness, not wt%
        None, None, None, None, None, None, None, None, None, None, None, None,
        70.5,                            # EMI Shielding Effectiveness (dB)
        "foam (2mm thickness)"                             # Filler Geometry, as indicated by "MXene foam"
    ],
    # 7. Metal-Filler Composites
    [
        "Synthetic Leather",                        # Polymer Matrix
        "Cu@Ag nanoflakes",                # Filler
        35.03,  #  5.17 vol% convertito in wt%   # Filler Concentration (wt%) field
        None, None, 0.9, 8.9, None, None, None, None, None, None, None, None,
        "~100",                            # EMI Shielding Effectiveness (dB)
        "nanoflakes"                       # Filler Geometry
    ],
    [
        "Waterborne polyurethane (WPU)",  # Polymer Matrix
        "Ag nanowires",                    # Filler
        28.6,                            # Filler Concentration (wt%)
        None, None, None, None, None, None,
        None, 38.5,  # Tensile Strength (MPa): ho preso il valore centrale "38.5 ± 2.9"
        None, None, None, None, None,
        64,                              # EMI Shielding Effectiveness (dB)
        "nanowires"                        # Filler Geometry
    ],
    # 8. Particle-Filler Composites
    [
        "PANI",                           # Polymer Matrix
        "Li₀.₅Fe₂.₅₋ₓGdₓO₄ ferrite nanoparticles",  # Filler
        None,                             # Filler Concentration not provided
        None, None, None, None, None, None, None, None, None, None, None, None,
        "41–42",                           # EMI Shielding Effectiveness (dB)
        "nanoparticles"                    # Filler Geometry
    ],
    [
        "Polystyrene (PS)",               # Polymer Matrix
        "Ag-coated hollow PPy microspheres",  # Filler
        "10 Ag",                             # Filler Concentration (wt%)
        #NOTA: non è specificata la concentrazione del filler, solo la concentrazione di Ag sulle sfere
        None, None, None, None, None, None, None, None, None, None, None, None,
        "23–59",                           # EMI Shielding Effectiveness (dB)
        "microspheres"                     # Filler Geometry
    ]
]

# Write the CSV file
with open("composites.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)  # write header
    writer.writerows(composites)

print("CSV file 'composites.csv' generated successfully with", len(composites), "composites.")
