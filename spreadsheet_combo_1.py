import csv

# Header con le nuove colonne aggiunte
headers = [
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Fiber", "Fiber Concentration (wt%)",
    "Matrix Density (g/cm³)", "Filler Density (g/cm³)", "Fiber Density (g/cm³)", "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry" #18 colonne
]

# Dati dei compositi
composites = [
    ["LDPE", "Basalt", 23.08, None, None, 0.925, 2.907, None, 11, None, None, None, None, 145, 273, None, None,
     "Particulate (≤140 μm)"],
    #17 colonne
    #0.910–0.940 g/cm3 - ho preso i valori medi dei range per la densità
    ["LDPE", "Basalt", 28.57, None, None, 0.925, 2.907, None, 39, None, 9.88, None, 250, None, 145, 273, None,
     "Particulate (≤140 μm)"],
    ["LDPE", "Basalt", 33.33, None, None, 0.925, 2.907, None, 21, None, None, None, None, 145, 273, None, None,
     "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 23.08, None, None, 0.95, 2.907, None, 60, None, None, None, None, 119, 284, None, None,
     "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 28.57, None, None, 0.95, 2.907, None, 80, 524, 9.88, None, 250, None, 119, 284, None,
     "Particulate (≤140 μm)"],
    ["HDPE", "Basalt", 33.33, None, None, 0.95, 2.907, None, 60, None, None, None, None, 119, 284, None, None,
     "Particulate (≤140 μm)"],
    ["PP", "Basalt", 28.57, None, None, 0.925, 2.907, None, None, 1970, 21.50, None, 4.33, None, None, None, None,
     "Particulate (≤140 μm)"], #controlla la concentrazione

    ["Epoxy", "CNTs", 2, "Flax", None, 1.15, 1.35, 1.47, None, None, None, None, None, None, None, None, None, "Nanotubes"],
    ["Epoxy", "MWCNT + nano-diamond", 0.125, None, None, 1.15, None, None, None, None, None, None, None, None, None,
     None, None, "Nanotubes + Nanoparticles"],
    ["LDPE", "CB + nano-clay", 20, "OPEFB", None, 0.925, None, None, None, None, None, None, None, None, None, None, None,
     "Particulate + Nanoplatelets"],
    ["Epoxy", "α-cellulosic micro-filler (Cocos nucifera)", 15, None, None, 1.15, 0.5, None, None, None, None, None, None,
     None, 365, None, None, "Micro-powder"],
   # ["Concrete", "Biochar", 1, None, None, 2.41, 1.75, None, None, None, 0.219, None, None, None, None, None, None, "Micro-powder"],
   # ["Concrete", "Biochar", 2, None, None, 2.41, 1.75, None, None, None, 0.1945, None, None, None, None, None, None,
    # "Micro-powder"],
    ["Polyurethane", "TMPS-treated silane", None, "Kenaf core", None, 1.15, None, 0.288, None, None, None, None, 365,
     None, None, None, None, "Core-shell"],
    ["Polyurethane", "Silane (Untreated)", None, "Kenaf core", None, 1.15, 0.00134, 0.288, None, None, None, None, 350,
     None, None, None, None, "Agglomerate"],
   # ["PP", None, None, "Wood flour (513 µm)", 40, 0.925, None, 0.205, None, None, 3200, 21.7, None, None, None, None,
    # None, None],
    ["Epoxy", None, None, "Sisal + Glass", None, 1.15, None, None, None, None, None, None, None, None, None, None, None, None],

#CHECK: tutto corretto fino a questo punto

[
        "Butyl rubber (IIR)",               # Polymer Matrix
        "Low-density polyethylene (PE)",    # Filler
        10,                               # Filler Concentration (wt%) as given
        None,                               # Fiber
        None,                               # Fiber Concentration (wt%)
        1.34, 0.925, None, None, None, None, None, None, None, None, None,
        60,                            # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ], #18
[
        "Butyl rubber (IIR)",               # Polymer Matrix
        "Low-density polyethylene (PE)",    # Filler
        10,                               # Filler Concentration (wt%) as given
        None,                               # Fiber
        None,                               # Fiber Concentration (wt%)
        1.34, 0.925, None, None, None, None, None, None, None, None, None,
        50,                            # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    # 2. Carbon Black-Based Composites
    [
        "Chlorinated polyethylene (CPE)",   # Polymer Matrix
        "Ketjen carbon black (K-CB)",         # Filler
        30,                               # Filler Concentration (wt%)
        None, None, 0.945, None, None, None, None, None, None, None, None, None,
        None,
        #non sprecificato il tipo di filler, quindi non posso vedere la densità
        38.4,                             # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "Phenolic resin",                   # Polymer Matrix
        "Carbon black (CB) nanoparticles",   # Filler
        None,                               # Filler Concentration (wt%) unspecified
        None, None, 1.665, None, None, None, None, None, None, None, None, None, None,
        30,                            # EMI Shielding Effectiveness (dB)
        "nanoparticles"                     # Filler Geometry
    ],
[
        "Phenolic resin",                   # Polymer Matrix
        "Carbon black (CB) nanoparticles",   # Filler
        None,                               # Filler Concentration (wt%) unspecified
        None, None, 1.665, 1.95, None, None, None, None, None, None, None, None, None,
        40,                            # EMI Shielding Effectiveness (dB)
        "nanoparticles"                     # Filler Geometry
    ],
    # 3. Graphene-Based Composites
    [
        "Epoxy",                           # Polymer Matrix
        "Graphene",                        # Filler
        15,                              # Filler Concentration (wt%)
        None, None, 1.25, 2.267, None, None, None, None, None, None, None, None, None,
        20,                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
[
        "Epoxy",                           # Polymer Matrix
        "Graphene",                        # Filler
        15,                              # Filler Concentration (wt%)
        None, None, 1.25, 2.267, None, None, None, None, None, None, None, None, None,
        20,                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "PMMA",                            # Polymer Matrix
        "Graphene",                        # Filler
        3.30,  # era dato in 1.8 vol%, convertito poi in wt%   # Filler Concentration (wt%)
        None, None, 1.18, 2.267, None, None, None, None, None, None, None, None, None,
        13,                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry
    ],
[
        "PMMA",                            # Polymer Matrix
        "Graphene",                        # Filler
        3.30,  # era dato in 1.8 vol%, convertito poi in wt%   # Filler Concentration (wt%)
        None, None, 1.18, 2.267, None, None, None, None, None, None, None, None, None,
        19,                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry
    ],
    [
        "PEI (polyetherimide)",            # Polymer Matrix
        "Graphene@Fe₃O₄",                  # Filler
        10,                              # Filler Concentration (wt%)
        None, None, 1.27, None, None, None, None, None, None, None, None, None, None,
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
        1.14, None, 1.875, None, None, None, None, None, None, None, None,
        45,                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
[
        "Nylon 6,6",                       # Polymer Matrix
        None,
        None,
        "Long carbon fibers",              # Fiber
        30,    # Fiber Concentration (wt%)
        1.14, None, 1.875, None, None, None, None, None, None, None, None,
        75,                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "Polysulfone (PSU)",               # Polymer Matrix
        None,                              # Filler (not applicable)
        None,
        "Carbon nanofibers (CNF)",           # Fiber
        10,                              # Fiber Concentration (wt%)
        1.24, None, 1.125, None, None, None, None, None, None, None, None,
        19,                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
[
        "Polysulfone (PSU)",               # Polymer Matrix
        None,                              # Filler (not applicable)
        None,
        "Carbon nanofibers (CNF)",           # Fiber
        10,                              # Fiber Concentration (wt%)
        1.24, None, 1.125, None, None, None, None, None, None, None, None,
        45,                           # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    # 5. MWCNT-Based Composites
    [
        "Polyaniline (PANI)",                            # Polymer Matrix
        "MWCNTs",                          # Filler
        7,                               # Filler Concentration (wt%)
        None, None, 1.245, None, None, None, None, None, None, None, None, None, None,
        27.5,                       # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
[
        "Polyaniline (PANI)",                            # Polymer Matrix
        "MWCNTs",                          # Filler
        7,                               # Filler Concentration (wt%)
        None, None, 1.245, 0.11, None, None, None, None, None, None, None, None, None, #ho considerato la densità apparente
        39.2,                       # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "PVDF",                            # Polymer Matrix
        "MWCNTs",                          # Filler
        15,                              # Filler Concentration (wt%)
        None, None, 1.78, 0.11, None, None, None, None, None, None, None, None, None,
        56,                              # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry (not provided)
    ],
    [
        "Epoxy",                           # Polymer Matrix
        "Reduced graphene oxide (rGO)-CF + Fe₃O₄ nanoparticles",  # Filler
        None,                              # Filler Concentration (wt%) not provided
        None, None, 1.25, None, None, None, None, None, None, None, None, None, None,
        31.3,                       # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry not provided
    ],
[
        "Epoxy",                           # Polymer Matrix
        "Reduced graphene oxide (rGO)-CF + Fe₃O₄ nanoparticles",  # Filler
        None,                              # Filler Concentration (wt%)
        None, None, 1.25, None, None, None, None, None, None, None, None, None, None,
        51.1,                       # EMI Shielding Effectiveness (dB)
        None                                # Filler Geometry
    ],
    # 6. MXene-Based Composites

    [
        "PDMS",                           # Polymer Matrix
        "MXene foam",                     # Filler
        None,
        None, None, 1.03, None, None, None, None, None, None, None, None, None, None,
        70.5,                            # EMI Shielding Effectiveness (dB)
        "foam (2mm thickness)"                             # Filler Geometry, as indicated by "MXene foam"
    ],
    # 7. Metal-Filler Composites
    [
        "Synthetic Leather",                        # Polymer Matrix
        "Cu@Ag nanoflakes",                # Filler
        35.03,  #  5.17 vol% convertito in wt%   # Filler Concentration (wt%) field
        None, None, 0.9, 8.9, None, None, None, None, None, None, None, None, None,
        100,                            # EMI Shielding Effectiveness (dB)
        "nanoflakes"                       # Filler Geometry
    ],
    [
        "Waterborne polyurethane (WPU)",  # Polymer Matrix
        "Ag nanowires",                    # Filler
        28.6,                            # Filler Concentration (wt%)
        None, None, None, 0.785, None, None, #non viene detto nulla sul tipo di WPU, quindi non posso vedere la densità
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
        None, None, 1.245, None, None, None, None, None, None, None, None, None, None,
        41,                           # EMI Shielding Effectiveness (dB)
        "nanoparticles"                    # Filler Geometry
    ],
    [
        "PANI",  # Polymer Matrix
        "Li₀.₅Fe₂.₅₋ₓGdₓO₄ ferrite nanoparticles",  # Filler
        None,  # Filler Concentration not provided
        None, None, 1.245, None, None, None, None, None, None, None, None, None, None,
        42,  # EMI Shielding Effectiveness (dB)
        "nanoparticles"  # Filler Geometry
    ],
    [
        "Polystyrene (PS)",               # Polymer Matrix
        "Ag-coated hollow PPy microspheres",  # Filler
        "10 Ag",                             # Filler Concentration (wt%)
        #NOTA: non è specificata la concentrazione del filler, solo la concentrazione di Ag sulle sfere
        None, None, 1.005, None, None, None, None, None, None, None, None, None, None,
        23,                           # EMI Shielding Effectiveness (dB)
        "microspheres"                     # Filler Geometry
    ],
[
        "Polystyrene (PS)",               # Polymer Matrix
        "Ag-coated hollow PPy microspheres",  # Filler
        "10 Ag",                             # Filler Concentration (wt%)
        #NOTA: non è specificata la concentrazione del filler, solo la concentrazione di Ag sulle sfere
        None, None, 1.005, None, None, None, None, None, None, None, None, None, None,
        59,                           # EMI Shielding Effectiveness (dB)
        "microspheres"                     # Filler Geometry
    ]

]

# Scrivere i dati nel file CSV con le nuove colonne
with open('spreadsheet_combo_1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # scrive l'header
    writer.writerow(headers)
    # scrive i dati dei compositi
    writer.writerows(composites)

print("File CSV creato con successo con le nuove colonne vuote!")
