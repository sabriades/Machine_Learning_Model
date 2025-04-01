import csv

# Header con le nuove colonne aggiunte
headers = [
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Fiber", "Fiber Concentration (wt%)",
    "Matrix Density (g/cm³)", "Filler Density (g/cm³)", "Fiber Density (g/cm³)", "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry", "Composite Density (g/cm³)", "Filler Volume Fraction (%)",
    "Elastic Modulus matrix (MPa)", "Elastic Modulus filler (MPa)", "Fiber Volume Fraction (%)", "Friction Coefficient",
    "Tensile Modulus (MPa)", "Impact Strength (kJ/m²)", "Fiber Geometry"

    #27 colonne
]

# Dati dei compositi
composites = [
    ["LDPE", "Basalt", 23.08, None, None, 0.925, 2.907, None, 11, 340, None, None, None, 145, 273, None, None,
     "Particulate (≤140 μm)", 1.123, 8.7, 250, 70000, None],

    #0.910–0.940 g/cm3 - ho preso i valori medi dei range per la densità
    ["LDPE", "Basalt", 28.57, None, None, 0.925, 2.907, None, 39, 440, 9.88, 14.82, 250, None, 145, 273, None,
     "Particulate (≤140 μm)", 1.183, 11.3, 250, 70000, None, 0.15], # Flexural ≈ 1.5*Tensile

    ["LDPE", "Basalt", 33.33, None, None, 0.925, 2.907, None, 21, 550, None, None, None, 145, 273, None, None,
     "Particulate (≤140 μm)", 1.246, 14.2, 250, 70000, None],

    ["HDPE", "Basalt", 23.08, None, None, 0.95, 2.907, None, 60, 1450, None, None, None, 119, 284, None, None,
     "Particulate (≤140 μm)", 1.156, 8.5, 1100, 70000, None],

    ["HDPE", "Basalt", 28.57, None, None, 0.95, 2.907, None, 80, 524, 9.88, 14.82, 250, None, 119, 284, None,
     "Particulate (≤140 μm)", 1.230, 11.1, 1100, 70000, None, 0.18],

    ["HDPE", "Basalt", 33.33, None, None, 0.95, 2.907, None, 60, 1850, None, None, None, 119, 284, None, None,
     "Particulate (≤140 μm)", 1.308, 14, 1100, 70000, None],

    ["PP", "Basalt", 28.57, None, None, 0.925, 2.907, None, None, 1970, 21.5, 32.25, 4.33, None, None, None, None,
     "Particulate (≤140 μm)", 1.183, 11.3, 1500, 70000, None, None, None],


    ["Epoxy", "CNTs", 2, "Flax", None, 1.15, 1.35, 1.47, None, None, None, None, None, None, None, None, None, "Nanotubes", 1.151, 1.5, None, None, None],

    ["Epoxy", "MWCNT + nano-diamond", 0.125, None, None, 1.15, None, None, None, None, None, None, None, None, None,
     None, None, "Nanotubes + Nanoparticles", None, None, None, None, None],

    ["LDPE", "CB + nano-clay", 20, "OPEFB", None, 0.925, None, None, None, None, None, None, None, None, None, None, None,
     "Particulate + Nanoplatelets", None, None, None, None, None],

    ["Epoxy", "α-cellulosic micro-filler (Cocos nucifera)", 15, None, None, 1.15, 0.5, None, None, None, None, None, None,
     None, 365, None, None, "Micro-powder", 1.073, 29.8, None, None, None],

   # ["Concrete", "Biochar", 1, None, None, 2.41, 1.75, None, None, None, 0.219, None, None, None, None, None, None, "Micro-powder"],
   # ["Concrete", "Biochar", 2, None, None, 2.41, 1.75, None, None, None, 0.1945, None, None, None, None, None, None,
    # "Micro-powder"],

    ["Polyurethane", "TMPS-treated silane", None, "Kenaf core", None, 1.15, None, 0.288, None, None, None, None, 365,
     None, None, None, None, "Core-shell", None, None, None, None, None],

    ["Polyurethane", "Silane (Untreated)", None, "Kenaf core", None, 1.15, 0.00134, 0.288, None, None, None, None, 350,
     None, None, None, None, "Agglomerate", None, None, None, None, None],

    ["PP",
     None,
     None,
     "Wood flour (513 µm)",
     40,
     0.925, # è valore medio della densità della matrice
     None,
     1.5,
     None,
     3200, #elastic modulus
     21.7, #tensile strength
     32.5, #flexural
     None, None, None,
     None, None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     3200, #tensile modulus
     4.5, #impact strength
     "Particulate"], #fiber geometry

    ["Epoxy", None, None, "Sisal + Glass", None, 1.15, None, None, None, None, None, None, None, None, None, None, None, None, None, None],

#CHECK: tutto corretto fino a questo punto

[
        "Butyl rubber (IIR)",               # Polymer Matrix
        "Low-density polyethylene (PE)",    # Filler
        10,                               # Filler Concentration (wt%) as given
        None,                               # Fiber
        None,                               # Fiber Concentration (wt%)
        1.34, 0.925, None, None, None, None, None, None, None, None, None,
        60,                            # EMI Shielding Effectiveness (dB)
        None, # Filler Geometry
    1.25, #composite density
    13.8, #filler volume fraction = (0.10/0.925) / [(0.10/0.925)+(0.90/1.34)]*100 = 13.8%
    None, #elastic modulus matrix
    None #elastic modulus filler

    ], #18
[
        "Butyl rubber (IIR)",               # Polymer Matrix
        "Low-density polyethylene (PE)",    # Filler
        10,                               # Filler Concentration (wt%) as given
        None,                               # Fiber
        None,                               # Fiber Concentration (wt%)
        1.34, 0.925, None, None, None, None, None, None, None, None, None,
        50,                            # EMI Shielding Effectiveness (dB)
        None, # filler geometry
    1.25,  # composite density
    13.8,  # filler volume fraction
    None,  # elastic modulus matrix
    None  # elastic modulus filler

    ],
    # 2. Carbon Black-Based Composites
    [
        "Chlorinated polyethylene (CPE)",   # Polymer Matrix
        "Ketjen carbon black (K-CB)",         # Filler
        30,                               # Filler Concentration (wt%)
        None, None, 0.945, 1.95, None, None, None, None, None, None, None, None,
        None,
        #non sprecificato il tipo di filler, quindi non posso vedere la densità
        38.4,                             # EMI Shielding Effectiveness (dB)
        None, # filler geometry
        1.16,  # composite density
        17.2,  # filler volume fraction
        None,  # elastic modulus matrix
        None  # elastic modulus filler

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
        None, # filler geometry
        1.36,  # composite density
        8.9,  # filler volume fraction
        None,  # elastic modulus matrix
        None  # elastic modulus filler

    ],
[
        "Epoxy",                           # Polymer Matrix
        "Graphene",                        # Filler
        15,                              # Filler Concentration (wt%)
        None, None, 1.25, 2.267, None, None, None, None, None, None, None, None, None,
        21,                           # EMI Shielding Effectiveness (dB)
    None,  # filler geometry
    1.36,  # composite density
    8.9,  # filler volume fraction
    None,  # elastic modulus matrix
    None  # elastic modulus filler                          # Filler Geometry (not provided)
    ],
    [
        "PMMA",                            # Polymer Matrix
        "Graphene",                        # Filler
        3.30,  # era dato in 1.8 vol%, convertito poi in wt%   # Filler Concentration (wt%)
        None, None, 1.18, 2.267, None, None, None, None, None, None, None, None, None,
        13,                           # EMI Shielding Effectiveness (dB)
        None,  # filler geometry
        1.19,  # composite density
        1.7,  # filler volume fraction
        None,  # elastic modulus matrix
        None  # elastic modulus filler
    ],
[
        "PMMA",                            # Polymer Matrix
        "Graphene",                        # Filler
        3.30,  # era dato in 1.8 vol%, convertito poi in wt%   # Filler Concentration (wt%)
        None, None, 1.18, 2.267, None, None, None, None, None, None, None, None, None,
        19,                           # EMI Shielding Effectiveness (dB)
    None,  # filler geometry
    1.19,  # composite density
    1.7,  # filler volume fraction
    None,  # elastic modulus matrix
    None  # elastic modulus filler
    ],
    [
        "PEI (polyetherimide)",            # Polymer Matrix
        "Graphene@Fe₃O₄",                  # Filler
        10,                              # Filler Concentration (wt%)
        None, None, 1.27, None, None, None, None, None, None, None, None, None, None,
        41.5,                            # EMI Shielding Effectiveness (dB)
        None,  # filler geometry
        None,  # composite density
        None,  # filler volume fraction
        None,  # elastic modulus matrix
        None  # elastic modulus filler
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
        None,  # filler geometry
        1.29,  # composite density
        None,  # filler volume fraction
        None,  # elastic modulus matrix
        None,  # elastic modulus filler
        20.8 #fiber volume fraction
    ],
[
        "Nylon 6,6",                       # Polymer Matrix
        None,
        None,
        "Long carbon fibers",              # Fiber
        30,    # Fiber Concentration (wt%)
        1.14, None, 1.875, None, None, None, None, None, None, None, None,
        75,                           # EMI Shielding Effectiveness (dB)
    None,  # filler geometry
    1.29,  # composite density
    None,  # filler volume fraction
    None,  # elastic modulus matrix
    None,  # elastic modulus filler
    20.8  # fiber volume fraction
    ],
    [
        "Polysulfone (PSU)",               # Polymer Matrix
        None,                              # Filler (not applicable)
        None,
        "Carbon nanofibers (CNF)",           # Fiber
        10,                              # Fiber Concentration (wt%)
        1.24, None, 1.125, None, None, None, None, None, None, None, None,
        19,                           # EMI Shielding Effectiveness (dB)
        None,  # filler geometry
        1.23,  # composite density
        None,  # filler volume fraction
        None,  # elastic modulus matrix
        None,  # elastic modulus filler
       10.9  # fiber volume fraction
    ],
[
        "Polysulfone (PSU)",               # Polymer Matrix
        None,                              # Filler (not applicable)
        None,
        "Carbon nanofibers (CNF)",           # Fiber
        10,                              # Fiber Concentration (wt%)
        1.24, None, 1.125, None, None, None, None, None, None, None, None,
        45,                           # EMI Shielding Effectiveness (dB)
    None,  # filler geometry
    1.23,  # composite density
    None,  # filler volume fraction
    None,  # elastic modulus matrix
    None,  # elastic modulus filler
    10.9  # fiber volume fraction
    ],
    # 5. MWCNT-Based Composites
    [
        "Polyaniline (PANI)",                            # Polymer Matrix
        "MWCNTs",                          # Filler
        7,                               # Filler Concentration (wt%)
        None, None, 1.245, None, None, None, None, None, None, None, None, None, None,
        27.5,                       # EMI Shielding Effectiveness (dB)
        None,  # filler geometry
        None,  # composite density
        None,  # filler volume fraction
        None,  # elastic modulus matrix
        None,  # elastic modulus filler
        None  # fiber volume fraction
    ],
[
        "Polyaniline (PANI)",                            # Polymer Matrix
        "MWCNTs",                          # Filler
        7,                               # Filler Concentration (wt%)
        None, None, 1.245, 0.11, None, None, None, None, None, None, None, None, None, #ho considerato la densità apparente
        39.2,                       # EMI Shielding Effectiveness (dB)
    None,  # filler geometry
    None,  # composite density
   None,  # filler volume fraction
    None,  # elastic modulus matrix
    None,  # elastic modulus filler
    None  # fiber volume fraction
    ],
    [
        "PVDF",                            # Polymer Matrix
        "MWCNTs",                          # Filler
        15,                              # Filler Concentration (wt%)
        None, None, 1.78, 0.11, None, None, None, None, None, None, None, None, None,
        56,                              # EMI Shielding Effectiveness (dB)
        None,  # filler geometry
        0.19,  # composite density
        74.1,  # filler volume fraction
        None,  # elastic modulus matrix
        None,  # elastic modulus filler
        None  # fiber volume fraction
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
    ],
#CHECK: i dati estratti sono tutti corretti. anche il calcolo di dati aggiuntivi
    # (oltre a quelli estratti nei 3 articoli) è corretto. vorrei calcolare altri dati,
    # ma la priorità è concentrarsi su compositi PEI (finora ce n'è solo uno) 30/03
    [
        "Polyetherimide (PEI)", "Fe₃O₄ microplate (FMP)", 4.76, None, None,
        1.27, #matrix density
        5.18, #filler density
        None, None,
        3104,  # Elastic Modulus (MPa) tramite Halpin-Tsai per filler piastriformi (per tutti i compositi successivi PEI MATRIX)
        None, None, None, None, None, None,
        None, "Microplate",
        1.29, #composite density
        1.2, #filler volume fraction
        3000, #elastic modulus matrix
        200000, #elastic modulur filler
        None, None, None, None, None
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

#anche la quarta tabella con tutti i PEI è stata verificata
]

# Scrivere i dati nel file CSV con le nuove colonne
with open('spreadsheet_combo_newp_1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # scrive l'header
    writer.writerow(headers)
    # scrive i dati dei compositi
    writer.writerows(composites)

print("File CSV creato con successo con le nuove colonne vuote!")
