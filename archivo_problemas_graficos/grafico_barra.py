import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df  = pd.read_csv("archivo_problemas_graficos\\confla_ingreso.csv")

#Creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#Obteniendo el total de ingresos 
total_ingresos = df["ingresos"].sum()

#mostrando el toal
print(f"El total de ingreso es de: ${total_ingresos} USD")

#mostrando el grafico
plt.show()
