import csv

# Header con le nuove colonne aggiunte
headers = [
    "Polymer Matrix", "Filler", "Filler Concentration (wt%)", "Fiber", "Fiber Concentration (wt%)",
    "Matrix Density (g/cm³)", "Filler Density (g/cm³)", "Fiber Density (g/cm³)", "Impact Toughness (kJ/m²)",
    "Elastic Modulus (MPa)", "Tensile Strength (MPa)", "Flexural Strength (MPa)", "Tensile Strain (%)",
    "Thermal Conductivity (W/m·K)", "Vicat Heat Resistance (°C)", "Initiation of Destruction Temp. (°C)",
    "EMI Shielding Effectiveness (dB)", "Filler Geometry", "Composite Density (g/cm³)", "Filler Volume Fraction (%)",
    "Elastic Modulus matrix (MPa)", "Elastic Modulus filler (MPa)", "Fiber Volume Fraction (%)", "Friction Coefficient",
    "Tensile Modulus (MPa)", "Impact Strength (kJ/m²)", "Fiber Geometry",
    "Offset Yield Stress (MPa)", "Fatigue Durability (cycles)", "Glass Transition Temperature (°C)",
    "Linear Expansion Coefficient (1/°C)", "Oxygen Index (%)", "Rockwell Hardness (M)", "Mode II Interlaminar Fracture Toughness (kJ/m²)",

"Hardness (Shore D)", "Rebound Resilience (%)", "Brittleness (10^10/%·Pa)",
    "Melting Temperature (°C)", "Crystallization Temperature (°C)", "Onset Crystallization Temperature (°C)",
    "Melting Enthalpy (J/g)", "Crystallinity Degree (%)",
    "Storage Modulus E′ at 25°C (MPa)", "Loss Modulus E″ at 25°C (MPa)", "tan δ at 25°C",
    "Melt Flow Index (g/10 min)",
    # "Complex Viscosity (Trend)",
    "Porosity (%)", "Adhesion Factor",

    # DA AGGIUNGERE ALLA LISTA DELLE PROP - # Dielectric/Electrical properties
     "Dielectric Constant (1 kHz, RT)", "Dielectric Constant (1 kHz, 150°C)",
    "Breakdown Strength (MV/m, RT)", "Breakdown Strength (MV/m, 150°C)", "Energy Density (J/cm³, RT)",
    "Energy Density (J/cm³, 150°C)", "Efficiency (%) RT", "Efficiency (%) 150°C",
    # "Leakage Current Mechanism",
    "Hopping Distance (RT)", "Hopping Distance (150°C)",
    "Trap Depth (eV)", "Trapped Charge (nC)", "Cyclic Stability at 150°C (cycles)",

    "Dielectric Loss (tanδ, 1 kHz, RT)", "Dielectric Loss (tanδ, 1 kHz, 150°C)",
    "AC Conductivity (σ_AC, S/cm, RT)", "AC Conductivity (σ_AC, S/cm, 150°C)",
    "Zeta Potential KLNS Lamellae (mV)", "Zeta Potential KLNS Edges (mV)", "Zeta Potential NTCDA (mV)",
    "Activation Energy (Ea)",
    "Bandgap (Eg)", "Interfacial Thickness (nm)"
]

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

    ["PU", "TMPS-treated silane", None, "Kenaf core", None, 1.15, None, 0.288, None, None, None, None, 365,
     None, None, None, None, "Core-shell", None, None, None, None, None],

    ["PU", "Silane (Untreated)", None, "Kenaf core", None, 1.15, 0.00134, 0.288, None, None, None, None, 350,
     None, None, None, None, "Agglomerate", None, None, None, None, None],
# PU - Polyurethane
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

#[
      #  "Butyl rubber (IIR)",               # Polymer Matrix
       # "Low-density polyethylene (PE)",    # Filler
        #10,                               # Filler Concentration (wt%) as given
     #   None,                               # Fiber
       # None,                               # Fiber Concentration (wt%)
        #1.34, 0.925, None, None, None, None, None, None, None, None, None,
        #60,                            # EMI Shielding Effectiveness (dB)
        #None, # Filler Geometry
    #1.25, #composite density
    #13.8, #filler volume fraction = (0.10/0.925) / [(0.10/0.925)+(0.90/1.34)]*100 = 13.8%
    #None, #elastic modulus matrix
    #None #elastic modulus filler

    #], #18
#[
       # "Butyl rubber (IIR)",               # Polymer Matrix
        #"Low-density polyethylene (PE)",    # Filler
        #10,                               # Filler Concentration (wt%) as given
        #None,                               # Fiber
       # None,                               # Fiber Concentration (wt%)
        #1.34, 0.925, None, None, None, None, None, None, None, None, None,
        #50,                            # EMI Shielding Effectiveness (dB)
        #None, # filler geometry
   # 1.25,  # composite density
    #13.8,  # filler volume fraction
   # None,  # elastic modulus matrix
    #None  # elastic modulus filler

  #  ],
    # 2. Carbon Black-Based Composites
    [
        "CPE",   # Polymer Matrix - Chlorinated polyethylene
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
        "PEI",            # Polymer Matrix
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
        "PSU",               # Polymer Matrix - Polysulfone
        None,                              # Filler
        None,
        "Carbon nanofibers (CNF)",           # Fiber
        10,                              # Fiber Concentration (wt%)
        1.24, None, 1.125, None, None, None, None, None, None, None, None,
        19,                           # EMI Shielding Effectiveness (dB)
        None,  # filler geometry
        1.23,  # composite density
        None,  # filler volume fraction
        2600,  # elastic modulus matrix - valore standard
        300000,  # elastic modulus filler - valore standard
       10.9  # fiber volume fraction
    ],
[
        "PSU",               # Polymer Matrix - Polysulfone
        None,                              # Filler (not applicable)
        None,
        "Carbon nanofibers (CNF)",           # Fiber
        10,                              # Fiber Concentration (wt%)
        1.24, None, 1.125, None, None, None, None, None, None, None, None,
        45,                           # EMI Shielding Effectiveness (dB)
    None,  # filler geometry
    1.23,  # composite density
    None,  # filler volume fraction
    2600,  # elastic modulus matrix - valore standard
    300000,  # elastic modulus filler - valore standard
    10.9  # fiber volume fraction
    ],
    # 5. MWCNT-Based Composites
    [
        "PANI",                            # Polymer Matrix - Polyaniline
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
        "PANI",                            # Polymer Matrix
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
        2000,  # elastic modulus matrix - valore standard
        300000,  # elastic modulus filler - valore standard
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
        "WPU",  # Polymer Matrix - Waterborne polyurethane
        "Ag nanowires",                    # Filler
        28.6,                            # Filler Concentration (wt%)
        None, None,
        1.05, #densità matrice - valore standard per WPU
        0.785, None, None,
        None, 38.5,  # Tensile Strength (MPa): ho preso il valore centrale "38.5 ± 2.9"
        None, None, None, None, None,
        64,                              # EMI Shielding Effectiveness (dB)
        "nanowires",                # Filler Geometry
        0.89, #composite density - ricavata
        28.5 #filler volume fraction % - ricavata
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
        "PS",               # Polymer Matrix - Polystyrene
        "Ag-coated hollow PPy microspheres",  # Filler
        10,                             # Filler Concentration (wt%)
        #NOTA: non è specificata la concentrazione del filler, solo la concentrazione di Ag sulle sfere
        None, None, 1.005, None, None, None, None, None, None, None, None, None, None,
        23,                           # EMI Shielding Effectiveness (dB)
        "microspheres"                     # Filler Geometry
    ],
[
        "PS",               # Polymer Matrix
        "Ag-coated hollow PPy microspheres",  # Filler
        10,                             # Filler Concentration (wt%)
        #NOTA: non è specificata la concentrazione del filler, solo la concentrazione di Ag sulle sfere
        None, None, 1.005, None, None, None, None, None, None, None, None, None, None,
        59,                           # EMI Shielding Effectiveness (dB)
        "microspheres"                     # Filler Geometry
    ],
#CHECK: i dati estratti sono tutti corretti. anche il calcolo di dati aggiuntivi
    # (oltre a quelli estratti nei 3 articoli) è corretto. vorrei calcolare altri dati,
    # ma la priorità è concentrarsi su compositi PEI (finora ce n'è solo uno) 30/03
    [
        "PEI", "Fe₃O₄ microplate (FMP)", 4.76, None, None,
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
        "PEI", "Fe₃O₄ microplate (FMP)", 7.41, None, None,
        1.27, 5.18, None, None,
        3275,  # Elastic Modulus (MPa) - Calcolato
        None, None, None, None, None, None,
        None, "Microplate", 1.34, 1.9, 3000, 200000, None, None, None, None, None
    ],
    [
        "PEI", "Fe₃O₄ microplate (FMP)", 9.09, None, None,
        1.27, 5.18, None, None,
        3412,  # Elastic Modulus (MPa) - Calcolato
        None, None, None, None, None, None,
        None, "Microplate", 1.40, 2.3, 3000, 200000, None, None, None, None, None
    ],
    [
        "PEI", "Fe₃O₄ microplate (FMP)", 13.04, None, None,
        1.27, 5.18, None, None,
        3798,  # Elastic Modulus (MPa) - Calcolato
        None, None, None, None, None, None,
        None, "Microplate", 1.52, 3.4, 3000, 200000, None, None, None, None, None
    ],
    [
        "PEI", "Fe₃O₄ microplate (FMP)", 16.67, None, None,
        1.27, 5.18, None, None,
        4326,  # Elastic Modulus (MPa) - Calcolato
        None, None, None, None, None, None,
        None, "Microplate", 1.65, 4.5, 3000, 200000, None, None, None, None, None
    ],

#anche la quarta tabella con tutti i PEI è stata verificata
    #3 APRILE - NUOVI DATI:

    # Row 1: PI/CF100
    [
        "PI", None, None, "CF100", 10,
        1.38, None, None, None,
        4200, 119.2, None, 5.6,
        None, None, None, None, None, None, None,
        3350, 60000, None, None, 4200, None,
        "AR = 10, L = 100 μm",
        65.1, 3500, 260, 3.68e-5, 46, 110
    ],
    # Row 2: PEI/CF100
    [
        "PEI", None, None, "CF100", 10,
        1.27, None, None, None,
        4100, 102, None, 3.7,
        None, None, None, None, None, None, None,
        3400, 60000, None, None, 4100, None,
        "AR = 10, L = 100 μm",
        65.9, 1200, 217, 5.2e-5, 47, 109
    ],
    # Row 3: PI/CF200
    [
        "PI", None, None, "CF200", 10,
        1.38, None, None, None,
        6900, 111, None, 2.3,
        None, None, None, None, None, None, None,
        3350, 200000, None, None, 6900, None,
        "AR = 20, L = 200 μm",
        88.0, 5400, 260, 3.68e-5, 46, 110
    ],
    # Row 4: PEI/CF200
    [
        "PEI", None, None, "CF200", 10,
        1.27, None, None, None,
        5500, 104.5, None, 3.2,
        None, None, None, None, None, None, None,
        3400, 200000, None, None, 5500, None,
        "AR = 20, L = 200 μm",
        75.0, 1600, 217, 5.2e-5, 47, 109
    ],
    # Row 5: PI/CF2000
    [
        "PI", None, None, "CF2000", 10,
        1.38, None, None, None,
        8100, 128, None, 1.9,
        None, None, None, None, None, None, None,
        3350, 200000, None, None, 8100, None,
        "AR = 200, L = 2000 μm",
        121.0, 14400, 260, 3.68e-5, 46, 110
    ],
    # Row 6: PEI/CF2000
    [
        "PEI", None, None, "CF2000", 10,
        1.27, None, None, None,
        7100, 120, None, 2.1,
        None, None, None, None, None, None, None,
        3400, 200000, None, None, 7100, None,
        "AR = 200, L = 2000 μm",
        108.0, 3400, 217, 5.2e-5, 47, 109
    ],

#NUOVO ARTICOLO 5: verificare che nella colonna della impact toughness ci sia
    # effettivamente la impact toughness - verificare
    #ho ancora il dubbio riguardo come chiamata l'ultima colonna
    [
        "PEEK",
        None,  # Filler assente (solo fibre)
        None,  # Filler Concentration (wt%) assente
        "Teijin TENAX E HTA 40",
        None,  # Fiber Concentration (wt%) non specificata (solo 4.5% sizing sulla fibra)
        None,  # Matrix Density non riportata
        None,  # Filler Density irrilevante
        None,  # Fiber Density non riportata
        None,  # Impact Toughness
        69000,  # Elastic Modulus (69 GPa → 69000 MPa)
        690,  # Tensile Strength (Tabella 2)
        None,  # Flexural Strength non misurata
        5.8,  # Tensile Strain (±45°, Tabella 2)
        None,  # Thermal Conductivity non misurata
        None,  # Vicat Heat Resistance non riportata
        None,  # Initiation of Destruction Temp
        None,  # EMI Shielding non misurato
        None,  # Filler Geometry assente
        None,  # Composite Density non riportata
        None,  # Filler Volume Fraction assente
        None,  # Elastic Modulus matrix
        None,  # Elastic Modulus filler
        53,  # Fiber Volume Fraction (Tabella 1)
        None,  # Friction Coefficient
        20000,  # Tensile Modulus (±45°, 20 GPa → 20000 MPa)
       None,  # Impact Strength
        "Woven fabric (5H satin, 7.0 µm, 375 g/m²)",  # Dettagli fibra (Sezione 2.1)
        None,  # Offset Yield Stress
        None,  # Fatigue Durability
        143,  # Glass Transition Temperature PEEK (dall'introduzione)
        None,  # Linear Expansion Coefficient
        None,  # Oxygen Index
        None,  # Rockwell Hardness
1.34 #valore calcolato
    ],
    [
        "PEI",
        None,
        None,
        "Teijin TENAX E HTA 40",
        None,
        None,
        None,
        None,
        None,
        69000,  # Elastic Modulus (69 GPa → 69000 MPa)
        700,  # Tensile Strength (Tabella 2)
        None,
        3.1,  # Tensile Strain (±45°)
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        52,  # Fiber Volume Fraction
        None,
        18000,  # Tensile Modulus (±45°, 18 GPa → 18000 MPa)
        None,
        "Woven fabric (5H satin, 7.0 µm, 375 g/m²)",
        None,
        None,
        217,  # Glass Transition Temperature PEI
        None,
        None,
        None,
1.53 #valore calcolato
    ],
    [
        "PEEK + PEI (30/70 vol%)",
        None,
        None,
        "Teijin TENAX E HTA 40",
        None,
        None,
        None,
        None,
        None,
        67000,  # Elastic Modulus (67 GPa → 67000 MPa)
        672,  # Tensile Strength (Tabella 2)
        None,
        4.6,  # Tensile Strain (±45°): deformazione a rottura quando il carico è applicato
        # a 45° rispetto alle fibre
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        45,  # Fiber Volume Fraction
        None,
        17000,  # Tensile Modulus (±45°, 17 GPa → 17000 MPa)
        None,
        "Woven fabric (5H satin, 7.0 µm, 375 g/m²)",
        None,
        None,
        None,  # Glass Transition Temperature
        None,
        None,
        None,
1.71 #valore calcolato
    ],

    #check: tutto ok

# ARTICOLO 6 - 7 APRILE

[
    "PEI",                          # Polymer Matrix
    None,                # Filler
    None,                             # Filler Concentration (wt%)
    "Carbon fibers",                # Fiber
    58,                             # Fiber Concentration (wt%)
    None,                           # Matrix Density (g/cm³)
    1.75,                           # Filler Density (g/cm³) [valore tipico per le carbon fibers]
    1.75,                           # Fiber Density (g/cm³) [same as filler]
    None,                           # Impact Toughness (kJ/m²)
    None,                           # Elastic Modulus (MPa)
    None,                           # Tensile Strength (MPa)
    998,                            # Flexural Strength (MPa) (unaged)
    None,                           # Tensile Strain (%)
    None,                           # Thermal Conductivity (W/m·K)
    None,                           # Vicat Heat Resistance (°C)
    None,                           # Initiation of Destruction Temp. (°C)
    None,                           # EMI Shielding Effectiveness (dB)
    "Continuous fibers (5H satin weave, 285 g/m²)",  # Filler Geometry
    1.51,                           # Composite Density (g/cm³) [calculated from 51 vol% fibers]
    51,                             # Filler Volume Fraction (%)
    3000,                           # Elastic Modulus matrix (MPa) [valore tipico per il  PEI]
    230000,                         # Elastic Modulus filler (MPa) [valore tipico per le carbon fibers]
    51,                             # Fiber Volume Fraction (%)
    None,                           # Friction Coefficient
    None,                           # Tensile Modulus (MPa)
    None,                           # Impact Strength (kJ/m²)
    "5H satin weave, 285 g/m²",     # Fiber Geometry
    None,                           # Offset Yield Stress (MPa)
    None,                           # Fatigue Durability (cycles)
    183,                            # Glass Transition Temperature (°C) (nel PEI)
    None,                           # Linear Expansion Coefficient (1/°C)
    None,                           # Oxygen Index (%)
    None,                           # Rockwell Hardness (M)
    None                            # Mode II Interlaminar Fracture Toughness (kJ/m²)
], #NOTA:. ho usato i valori tipici di densità e moduli elastici per arricchire il dataset

#ARTICOLO 7 - 7 APRILE
    # PE/1Al
[
    "HDPE", "Aluminum", 1, None, None,
    0.954, 2.6, None, None,
    1162, 24.8, None, 25.6,
    None, None, None,
    None, "Micrometric particles (~65 µm)", None, None,
    1220, None, None, None,
    1162, None, None,
    None, None, None,
    None, None, None, None,

    56.2, 18.0, 0.273,
    132.3, 112.4, 115.8,
    207.1, 71.3,
    1433, 81, 0.0568,
    30,
    # "Slight increase at 1–2 wt%",
    1.20, -0.0436
],
    # PE/2Al
    [
        "HDPE", "Aluminum", 2, None, None,
        0.954, 2.6, None, None,
        1126, 25.2, None, 21.6,
        None, None, None,
        None, "Micrometric particles (~65 µm)", None, None,
        1220, None, None, None,
        1126, None, None,
        None, None, None,
        None, None, None, None,

        56.5, 17.8, 0.358,
        132.4, 112.3, 116.0,
        194.6, 67.6,
        1296, 72, 0.0557,
        30,
       # "Slight increase at 1–2 wt%",
        1.83, -0.0580
    ],
    # PE/5Al
    [
        "HDPE", "Aluminum", 5, None, None,
        0.954, 2.6, None, None,
        1149, 24.2, None, 17.5,
        None, None, None,
        None, "Micrometric particles (~65 µm)", None, None,
        1220, None, None, None,
        1149, None, None,
        None, None, None,
        None, None, None, None,

        57.0, 17.0, 0.413,
        132.3, 112.5, 116.1,
        196.0, 70.3,
        1388, 78, 0.0564,
        30,
       # "Minimal change for >2 wt%",
        4.40, -0.0404
    ],
    # PE/10Al
    [
        "HDPE", "Aluminum", 10, None, None,
        0.954, 2.6, None, None,
        1225, 23.6, None, 10.6,
        None, None, None,
        None, "Micrometric particles (~65 µm)", None, None,
        1220, None, None, None,
        1225, None, None,
        None, None, None,
        None, None, None, None,

        57.7, 16.4, 0.534,
        132.4, 112.4, 115.9,
        188.7, 71.4,
        1766, 97, 0.0550,
        30,
        # "Minimal change for >2 wt%",
        9.52, -0.0359
    ],
    # PE/20Al
    [
        "HDPE", "Aluminum", 20, None, None,
        0.954, 2.6, None, None,
        1422, 21.3, None, 7.9,
        None, None, None,
        None, "Micrometric particles (~65 µm)", None, None,
        1220, None, None, None,
        1422, None, None,
        None, None, None,
        None, None, None, None,

        59.6, 15.1, 0.682,
        131.7, 112.3, 116.1,
        166.2, 70.8,
        1853, 105, 0.0567,
        30,
        # "Minimal change for >2 wt%", 16.37, 0.0352
    ],

    #per ora 61 righe in tabella
    #NUOVO ARTICOLO - 9 APRILE - DA CONTROLLARE

  [  # KLNS/PEI Monolayer (0.2 wt%)
        # Material properties
        "PEI", "KLNS", 0.2, None, None,
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
        0.96, 1.24,
        None, None, None,

        0.015, 0.006,

        # Conductivity
        "<1e-12", "1.2e-12",

        # Surface properties
        -25.97, 7.04, None
    ],
    [  # Sandwich KLNS (0.2 wt%) + NTCDA (0.5 wt%)
        # Material properties
        "PEI", "KLNS + NTCDA", "0.2 (KLNS middle) + 0.5 (NTCDA outer layers)", None, None,
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

],

    # 1. SiC@SiO₂/PEI - 0.15 wt%
    [
        "PEI", "SiC@SiO₂", 0.15, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None,
        "Core-shell nanoparticles (~50 nm, 6 nm SiO₂ shell)", None, None,
        None, None, None, None,
        None, None, None,
        None, None, 217,
        None, None, None,
        None, None, None,
        None, None, None, None, None,
        None, None, None,
        None, None,
        3.82, None,
        539.37, 510.63, None, 5.26, None, 95,
        None, None, None, None, None,
        0.05, 0.05, None, None, None, None, None,
        None, None, None, None, 19.15,
        
    ],
    # 2. SiC@SiO₂/PEI - 0.30 wt%
    [
        "PEI", "SiC@SiO₂", 0.30, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None,
        "Core-shell nanoparticles (~50 nm, 6 nm SiO₂ shell)", None, None,
        None, None, None, None,
        None, None, None,
        None, None, 217,
        None, None, None,
        None, None, None,
        None, None, None, None, None,
        None, None, None,
        None, None,
        3.82, None,
        539.37, 510.63, None, 5.26, None, 95,
        None, None, None, None, None,
        0.05, 0.05, None, None, None, None, None,
        None, None, None, None, 19.15,

    ],
    # 3. SiC@SiO₂/PEI - 0.45 wt%
    [
        "PEI", "SiC@SiO₂", 0.45, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None,
        "Core-shell nanoparticles (~50 nm, 6 nm SiO₂ shell)", None, None,
        None, None, None, None,
        None, None, None,
        None, None, 217,
        None, None, None,
        None, None, None,
        None, None, None, None, None,
        None, None, None,
        None, None,
        None, None,
        None, None, None, None, None, None,
        None, None, None, None, None,
        0.05, 0.05, None, None, None, None, None,
        None, None, None, None, None,  # Interfacial Thickness in 70

    ],
    # 4. SiC@SiO₂/PEI - 0.60 wt%
    [
        "PEI", "SiC@SiO₂", 0.60, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None,
        "Core-shell nanoparticles (~50 nm, 6 nm SiO₂ shell)", None, None,
        None, None, None, None,
        None, None, None,
        None, None, 217,
        None, None, None,
        None, None, None,
        None, None, None, None, None,
        None, None, None,
        None, None,
        None, None,
        None, None, None, None, None, None,
        None, None, None, None, None,
        0.05, 0.05, None, None, None, None, None,
        None, None, None, None, None,  # Interfacial Thickness in 70

    ],
    # 5. SiC/PEI - 0.15 wt%
    [
        "PEI", "SiC", 0.15, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None,
        "Nanoparticles (~50 nm)", None, None,
        None, None, None, None,
        None, None, None,
        None, None, 217,
        None, None, None,
        None, None, None,
        None, None, None, None, None,
        None, None, None,
        None, None,
        4.31, None,
        None, None, None, None, None, None,
        None, None, None, None, None,
        0.05, 0.05, None, None, None, None, None,
        None, None, None, None, 15.94,  # Interfacial Thickness in 70

    ],
    # 6. SiC/PEI - 0.30 wt%
    [
        "PEI", "SiC", 0.30, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None,
        "Nanoparticles (~50 nm)", None, None,
        None, None, None, None,
        None, None, None,
        None, None, 217,
        None, None, None,
        None, None, None,
        None, None, None, None, None,
        None, None, None,
        None, None,
        4.31, None,
        None, None, None, None, None, 59.6,
        None, None, None, None, None,
        0.05, 0.05, None, None, None, None, None,
        None, None, None, None, 15.94,  # Interfacial Thickness in 70

    ],
    # 7. SiC/PEI - 0.45 wt%
    [
        "PEI", "SiC", 0.45, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None,
        "Nanoparticles (~50 nm)", None, None,
        None, None, None, None,
        None, None, None,
        None, None, 217,
        None, None, None,
        None, None, None,
        None, None, None, None, None,
        None, None, None,
        None, None,
        None, None,
        None, None, None, None, None, None,
        None, None, None, None, None,
        0.05, 0.05, None, None, None, None, None,
        None, None, None, None, None,  # Interfacial Thickness in 70

    ],
    # 8. SiC/PEI - 0.60 wt%
    [
        "PEI", "SiC", 0.60, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None,
        "Nanoparticles (~50 nm)", None, None,
        None, None, None, None,
        None, None, None,
        None, None, 217,
        None, None, None,
        None, None, None,
        None, None, None, None, None,
        None, None, None,
        None, None,
        None, None,
        None, None, None, None, None, None,
        None, None, None, None, None,
        0.05, 0.05, None, None, None, None, None,
        None, None, None, None, None,  # Interfacial Thickness in 70

    ]
]
# Scrivere i dati nel file CSV con le nuove colonne
with open('spreadsheet_combo_newp6.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # scrive l'header
    writer.writerow(headers)
    # scrive i dati dei compositi
    writer.writerows(composites)

print("file CSV creato!")