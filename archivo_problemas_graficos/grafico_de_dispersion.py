import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df  = pd.read_csv("archivo_problemas_graficos\\dispersion.csv")

#Creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)





#mostrando el grafico
plt.show()
