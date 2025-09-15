import pandas as pd

table=pd.read_csv("table.csv") #dataframe
print(table)
#rinomino le colonne per richiamarle più facilmente
table.rename(columns={
    "Filler Concentration (wt%)": "filler_concentration",
    "Matrix Density (g/cm³)": "matrix_density",
    "Filler Density (g/cm³)": "filler_density",
    "Elastic Modulus matrix (MPa)": "E_matrix",
    "Elastic Modulus (MPa)": "E_composite",
    "Filler Volume Fraction (%)": "filler_volume_percentage",
    "Elastic Modulus filler (MPa)": "E_f",
    "Composite Density (g/cm³)": "composite_d"
}, inplace=True)

#filler concentration come frazione
#condizione if else

for index, row in table.iterrows():
    if row["filler_volume_percentage"] in ["c","-"] :
        #faccio una leggera modifica a if row["filler_volume_percentage"] == "c", in modo tale che la condizione valga anche se viene trovato "-"
        #se c'è una riga nella colonna filler_volume_percentage che ha -
        #viene riprodotto questo codice
        filler_concentration_fraction = row["filler_concentration"] / 100
        # calcolo il volume di fibre come frazione, che poi riporterò in percentuale
        num_volume = filler_concentration_fraction / row["filler_density"]
        den_volume = (filler_concentration_fraction / row["filler_density"]) + (
                    (1 - filler_concentration_fraction) / row["matrix_density"])
        filler_volume = num_volume / den_volume
        filler_volume_fraction = filler_volume * 100

        #aggiorno il dataframe con le nuove colonne
        #table.at[index, "filler_concentration_fraction_calc"] = filler_concentration_fraction
        table.at[index, "filler_volume_calc"] = filler_volume
        table.at[index, "filler_volume_fraction_calc"] = filler_volume_fraction

    else:
        table.at[index, "filler_volume_calc"] = pd.NA
        table.at[index, "filler_volume_fraction_calc"]=pd.NA


#seconda condizione if else
#calcolo formula inversa per trovare E filler

for index, row in table.iterrows():
    if row["E_f"] in ["c","-"] :
        E_filler = (row["E_composite"] - row["E_matrix"] * (1 - row["filler_volume_calc"])) / row["filler_volume_calc"]

        table.at[index, "E_filler_calc"]=E_filler

    else:
        table.at[index, "E_filler_calc"] = pd.NA

#terza condizione if

for index, row in table.iterrows():
    if row["composite_d"] in ["c","-"] :
        dproduct_filler = (row["filler_density"]) * (row["filler_volume_calc"])
        dproduct_matrix = ((row["matrix_density"]) * (1 - (row["filler_volume_calc"])))
        composite_density = dproduct_filler + dproduct_matrix

        table.at[index, "composite_density_calc"]=composite_density

    else:
        table.at[index, "composite_density_calc"]=pd.NA

table=table.round(3)


table.to_csv("new_table_improved.csv", index=False)
print("tabella nuova creata")