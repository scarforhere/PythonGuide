# -*- coding: utf-8 -*-

import numpy as np
import scipy as sc
from scipy.interpolate import griddata, interp2d
import sys

import matplotlib.pyplot as plt



######## 1.

daten = np.loadtxt('./data/messdaten.dat')
tt, x1, u, I = daten.T # 2d-Array entpacken

# Daten anschauen
if 0: #( 0 -> nicht ausführen)
    plt.plot(tt, x1)
    plt.figure()
    plt.plot(tt, u)
    plt.figure()
    plt.plot(tt, I)

    plt.show()
    sys.exit()


######## 2.

# Vorzeichen vom Strom anpassen:
I = I*np.sign(u)

# Hinweis: Wenn Spannung 0 -> VZ = 0 -> Strom = 0

if 0:

    plt.plot(tt, I)

    plt.show()
    sys.exit()

######## 3.

# Indizes der Spannungsimpulse herausfinden

udiff = np.diff(u)
change_indices = np.arange(len(u)-1)[udiff != 0]
# Indizes der Werte True, wo es eine Änderung in U gibt
# (BOOL-Indizierung wurde benutzt)

# Verhindern, dass ein evtl "halber Impuls am Ende mit erkannt wird"

if len(change_indices) % 2 == 1:
    zz = 0 # abc
    change_indices = change_indices[:-1]  # letzten Wert weglassen


# Bis jetzt sind die Indizes hintereinander
# Wir wollen immer zwei in einer Zeile
#1: Impuls-Start-Index, 2: Impuls-End-Index)

change_indices = change_indices.reshape(-1, 2) # -1  sagt: "so, dass es passt"

# erste Spalte noch um eins erhöhen, weil sich der Index auf den letzten
# Wert vor dem Sprung bezieht.

change_indices[:, 0] += 1

print(change_indices)

######### 4.

# Histogramm vom dritten "Strom-Block" anlegen:
if 0:
    i1, i2 = change_indices[3,:]

    plt.hist(I[i1:i2])
    plt.show()
    sys.exit()

######### 5.

# Strom mitteln:

I_mean = 0*I # neues ('leeres') Array anlegen

# Zeilenweise über change_indices iterieren
for i1, i2 in change_indices:
    I_mean[i1:i2] = np.mean(I[i1:i2]) # Mittelwert bilden und speichern


if 0:

    plt.plot(tt, I,label='I')
    plt.plot(tt, I_mean,label='I_mean')
    plt.legend()

    plt.show()
    sys.exit()

####### 6.

if 0:
    plt.figure()

    start_idcs = change_indices[:, 0] # erste Spalte: Indizes, wo es los geht

    # Für jeden Strom-Block ein Spannungs-Strom-Werte-Paar bestimmen:
    ii = I_mean[start_idcs]
    uu = u[start_idcs]

    plt.plot(uu, ii, 'bx', ms=7) # große blaue Kreuze (x)

    a1, a0 =  sc.polyfit(uu, ii, 1) # lineare Regression

    plt.plot(uu, a1*uu+a0, 'g-') # Polynom (Geradengleichung) auswerten und plotten
    # alternativ: sc.polyval [a1, a0]

    print("Leitwert:", a1)
    print("Strom-Offset", a0)

    plt.show()
    sys.exit()


######### 7.

dt = tt[1]
xd = np.diff(x1)/dt
xdd = np.diff(x1,2)/dt**2

######### 8.
if 0:
    for i1, i2 in change_indices:

        # wir wollen jetzt nur positive Spannungsimpulse
        # wenn u< 0 ist: mit nächstem Schleifendurchlauf weitermachen
        if u[i1] < 0: continue

        plt.plot(xd[i1:i2-1], xdd[i1:i2-1])

    plt.show()
    sys.exit()

######### 9.

# siehe
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.griddata.html

# Wir brauchen die Eingangsdaten in folgendem Format:

# points (Shape = (N, 2)) Jede Zeile ist ein Punkt im Geschw.-Beschl.-Diagramm
# voltage (len = N), der zum jeweiligen Punkt gehörende Spannungswert

# Wir arbeiten erstmal mit Listen (lassen sich leichter verketten).
# Die Listen wandeln wir am Ende in Arrays um.

points_vel = []
points_acc = []
voltage = []

for i1, i2 in change_indices:

    # negative Werte ignorieren
    if u[i1] < 0: continue

    points_vel += list(xd[i1:i2-1])
    points_acc += list(xdd[i1:i2-1])

    # Liste der entsprechenden Länge, in der alle Elemente den gleichen Wert haben
    # nämlich den passenden Spannungswert
    voltage += [u[i1]]*(i2-1-i1)


# Problem-Umgehung bei Interpolation:
# Pseudo-Messwerte am Rand hinzufügen um nan-Werte ("not-a-number") zu vermeiden.
# Annahme: bei 3V bewegt sich noch (fast) nichts
points_vel = [0, 0,   0,  7,  7] + points_vel
points_acc = [0, 3,  14,  0, 14] + points_acc
voltage =    [3, 3,  12, 12, 12] + voltage

# Listen als Arrays zusammenpacken:
points = np.array([points_vel, points_acc]).T
voltage = np.array(voltage)


xd_max = max(points[:,0])
xdd_max = max(points[:,1])
N_grid = 100

# reguläres Gitter erzeugen
grid_v_arr1d = np.linspace(0, xd_max, N_grid)
grid_a_arr1d = np.linspace(0, xdd_max, N_grid)
vv, aa = np.meshgrid(grid_v_arr1d, grid_a_arr1d) # 2d arrays


# Interpolation durchfürhen
interp_voltage = griddata(points, voltage, (vv, aa) )

# nan-Werte am Rand eleminieren
interp_voltage[:, 0] = interp_voltage[:, 1] # erste Spalte := zweite Spalte
interp_voltage[0, :] = interp_voltage[1, :] # erste Zeile:= zweite Zeile

if 0:
    # Datenfeld grafisch darstellen
    plt.figure()
    plt.imshow(interp_voltage,
               extent=(0, xd_max, 0, xdd_max), origin='lower', interpolation='nearest')
    plt.xlabel("Geschwindigkeit")
    plt.ylabel("Beschleunigung")
    plt.colorbar(label="Spannung")
    plt.title("Zsh. zwischen Geschwindigkeit und Beschleunigung \n"
              "in Abhängigkeit der Spannung.")



    # nochmal die Linien zeichnen
    for i1, i2 in change_indices:

        if u[i1] < 0: continue

        plt.plot(xd[i1:i2-1], xdd[i1:i2-1], 'k-')

    # Erklärung: Jede Kurve entspricht einer Messreihe.
    # Wenn der Wagen steht (Geschwindigkeit 0) steht die
    # komplette Motorleistung für die Beschleunigung zur Verfügung.
    # Je schneller der Wagen ist, um so mehr Motorleisung wird für
    # das Halten der Geschwindigkeit benötigt -> Beschleunigung sinkt.


    plt.savefig("res.pdf")

    plt.show()
    sys.exit()

##### 10.

def calc_voltage(v, a):
    s = np.sign(a)
    a = np.abs(a)
    v = np.abs(v)


    i1 = int( v/xd_max*N_grid )
    i2 = int( a/xdd_max*N_grid )

    return interp_voltage[i1, i2]*s

###### 11.

data = np.load('./data/aufschwingen.npy')

tt, x1, x2, x3, x4, acc = data.T

u = acc*0

for i in range(len(acc)):
    a = acc[i]
    v = x2[i]

    u[i] = calc_voltage(v, a)

if 1:
    plt.figure()
    plt.plot(tt, acc)
    plt.plot(tt, u)

    plt.show()
    sys.exit()

