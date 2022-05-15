# Quelle der Daten:
# - https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.csv
# - https://data.giss.nasa.gov/gistemp/graphs/ (Übersicht)



import numpy as np
import scipy as sc
import matplotlib.pyplot as plt



data = np.loadtxt("graph.csv", skiprows=3, delimiter=",")

years, temp, avg = data.T

plt.plot(years, temp, "k.-", label="Jahresmittel")
plt.plot(years, avg, "r-", label="Gleitender-Mittelwert (5 Jahre)")


# broadcasting
plt.plot(years, years*0 + np.mean(temp[20:120]), label="Mittelwert 20. Jh.")

plt.xlabel("Jahr")
plt.ylabel("Temperaturanomalie")

# Legende erzeugen
plt.legend()
# plt.savefig("temperatur-anomalie.pdf")
plt.show()

