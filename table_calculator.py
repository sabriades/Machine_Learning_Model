import pandas as pd

table=pd.read_csv("tabella.csv")

#rinomino le colonne per richiamarle più facilmente
table.rename(columns={
    "Filler Concentration (wt%)": "filler_concentration",
    "Matrix Density (g/cm³)": "matrix_density",
    "Filler Density (g/cm³)": "filler_density",
    "Elastic Modulus matrix (MPa)": "E_matrix",
    "Elastic Modulus filler (MPa)": "E_filler"
}, inplace=True)

#filler concentration come frazione
table["filler_concentration_fraction"]=table["filler_concentration"]/100

#calcolo il volume di fibre come frazione, che poi riporterò in percentuale
num_volume=table["filler_concentration_fraction"]/table["filler_density"]
den_volume=(table["filler_concentration_fraction"]/table["filler_density"])+((1-(table["filler_concentration_fraction"]))/table["matrix_density"])

table["filler_volume"]=num_volume/den_volume

table["filler_volume_fraction"]=(table["filler_volume"])*100

#adesso calcolo product_filler=(Efiller_float*filler_volume)
#product_matrix=(Ematrix_float*(1-filler_volume))
#Ecomposite=product_filler+product_matrix

product_filler=(table["E_filler"])*(table["filler_volume"])
product_matrix=(table["E_matrix"])*((1-(table["filler_volume"])))

table["E_composite"]=product_filler+product_matrix

#adesso calcolo dproduct_filler=(filler_float*filler_volume)
#dproduct_matrix=(matrix_float*(1-filler_volume))
#composite_density=dproduct_filler+dproduct_matrix

dproduct_filler=(table["filler_density"])*(table["filler_volume"])
dproduct_matrix=((table["matrix_density"])*(1-(table["filler_volume"])))
table["composite_density"]=dproduct_filler+dproduct_matrix

print(table[["filler_volume_fraction","E_composite","composite_density"]])

#nel mio caso sarebbe più utile cambiare il codice con la formula inversa per calcolare E filler. rifaccio