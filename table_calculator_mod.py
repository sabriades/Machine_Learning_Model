import pandas as pd

table=pd.read_csv("table.csv")
print(table)
#rinomino le colonne per richiamarle più facilmente
table.rename(columns={
    "Filler Concentration (wt%)": "filler_concentration",
    "Matrix Density (g/cm³)": "matrix_density",
    "Filler Density (g/cm³)": "filler_density",
    "Elastic Modulus matrix (MPa)": "E_matrix",
    "Elastic Modulus (MPa)": "E_composite"
}, inplace=True)

#filler concentration come frazione
table["filler_concentration_fraction"]=table["filler_concentration"]/100

#calcolo il volume di fibre come frazione, che poi riporterò in percentuale
num_volume=table["filler_concentration_fraction"]/table["filler_density"]
den_volume=(table["filler_concentration_fraction"]/table["filler_density"])+((1-(table["filler_concentration_fraction"]))/table["matrix_density"])

table["filler_volume"]=num_volume/den_volume

table["filler_volume_fraction"]=(table["filler_volume"])*100

#calcolo formula inversa per trovare E filler

table["E_filler"]=(table["E_composite"]-table["E_matrix"]*(1-table["filler_volume"]))/table["filler_volume"]

#adesso calcolo dproduct_filler=(filler_float*filler_volume)
#dproduct_matrix=(matrix_float*(1-filler_volume))
#composite_density=dproduct_filler+dproduct_matrix

dproduct_filler=(table["filler_density"])*(table["filler_volume"])
dproduct_matrix=((table["matrix_density"])*(1-(table["filler_volume"])))
table["composite_density"]=dproduct_filler+dproduct_matrix

table=table.round(3)

print(table[["filler_volume_fraction","E_filler","composite_density"]])

table.to_csv("new_table.csv", index=False)
print("tabella nuova creata")