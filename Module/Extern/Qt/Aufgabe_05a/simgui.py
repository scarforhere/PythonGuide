# -*- coding: utf-8 -*-

"""
Das ist das Hauptprogramm.
"""

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

import sys

from model import rhs
from scipy.integrate import odeint
from numpy import arange

import matplotlib
matplotlib.use('Qt5Agg') # Backend explizit festlegen

import matplotlib.pyplot as plt

import configparser


# QApplication Instanz wird immer benötigt (sys.argv erst mal hinnehmen)
app = QtWidgets.QApplication(sys.argv)



#-------------------------------------------------------------------------------


# Dialog erzeugen
dialog = QtWidgets.QDialog()


# Label und Eingabefelder
mass1_label = QtWidgets.QLabel('Masse Laufkatze', dialog)
mass1_edit = QtWidgets.QLineEdit('0.8', dialog)

mass2_label = QtWidgets.QLabel('Masse Last', dialog)
mass2_edit = QtWidgets.QLineEdit('0.3', dialog)

len_label = QtWidgets.QLabel('Pendellänge', dialog)
len_edit = QtWidgets.QLineEdit('0.5', dialog)

dx_label = QtWidgets.QLabel('Schrittweite', dialog)
dx_edit = QtWidgets.QLineEdit('0.01', dialog)

t_end_label = QtWidgets.QLabel('Simulationsdauer', dialog)
t_end_edit = QtWidgets.QLineEdit('10', dialog)


# Buttons
sim_button = QtWidgets.QPushButton('Simulieren', dialog)
open_button = QtWidgets.QPushButton('Öffnen', dialog)
save_button = QtWidgets.QPushButton('Speichern', dialog)
exit_button = QtWidgets.QPushButton('Exit', dialog)


# Ausrichtung anpassen
mass1_edit.setAlignment(QtCore.Qt.AlignRight)
mass2_edit.setAlignment(QtCore.Qt.AlignRight)
len_edit.setAlignment(QtCore.Qt.AlignRight)
dx_edit.setAlignment(QtCore.Qt.AlignRight)
t_end_edit.setAlignment(QtCore.Qt.AlignRight)


# zulässige Zeichen beschränken - hier nur Zahlen eingeben
mass1_edit.setValidator(QtGui.QDoubleValidator(mass1_edit))
mass2_edit.setValidator(QtGui.QDoubleValidator(mass2_edit))
len_edit.setValidator(QtGui.QDoubleValidator(len_edit))
dx_edit.setValidator(QtGui.QDoubleValidator(dx_edit))
t_end_edit.setValidator(QtGui.QDoubleValidator(t_end_edit))


# Layout
layout = QtWidgets.QGridLayout()
layout.addWidget(mass1_label, 0, 0)
layout.addWidget(mass1_edit, 0, 1)
layout.addWidget(mass2_label, 1, 0)
layout.addWidget(mass2_edit, 1, 1)
layout.addWidget(len_label, 2, 0)
layout.addWidget(len_edit, 2, 1)
layout.addWidget(dx_label, 3, 0)
layout.addWidget(dx_edit, 3, 1)
layout.addWidget(t_end_label, 4, 0)
layout.addWidget(t_end_edit, 4, 1)

layout.addWidget(sim_button, 5, 0, 1, 2)
layout.addWidget(open_button, 6, 1, 2, 1)
layout.addWidget(save_button, 6, 0, 2, 1)
layout.addWidget(exit_button, 8 , 0, 1, 2)

dialog.setLayout(layout)


# Focus auf Exit
exit_button.setFocus()


def saveFile():
    """
    Dialog zur Auswahl einer Datei öffnen und die aktuellen Parameter darin
    abspeichern
    """

    # Dialog für Dateiname (gibt ein 2-Tupel zurück), siehe Folie 9
    filename, type_filter = QtWidgets.QFileDialog.getSaveFileName()

    if filename == "":
        return  # wenn "Abbrechen"/"Cancel" gedrückt wurde -> nichts tun

    # Configparser anlegen und Daten übergeben
    c = configparser.SafeConfigParser()

    c.add_section('Parameter')
    c.set('Parameter', 'm1', str(mass1_edit.text()))
    c.set('Parameter', 'm2', str(mass2_edit.text()))
    c.set('Parameter', 'l',  str(len_edit.text()))

    c.add_section('Simulation')
    c.set('Simulation', 'dx', str(dx_edit.text()))
    c.set('Simulation', 't_end', str(t_end_edit.text()))

    # Configfile schreiben
    with open(filename, 'w') as fid:
        c.write(fid)


def openFile():
    """
    Öffnet eine ini-Datei und liest die gespeicherten Daten
    """

    # Dialog für Dateiname (gibt ein 2-Tupel zurück), siehe Folie 9
    filename, type_filter = QtWidgets.QFileDialog.getOpenFileName()

    if filename == "":
        return  # wenn "Abbrechen"/"Cancel" gedrückt wurde -> nichts tun

    # Configparser anlegen
    c = configparser.SafeConfigParser()

    # aus Datei lesen
    print('lade', filename)

    if c.read(str(filename)):
        print('OK')
    else:
        print('Keine Konfigurationsdatei geladen')

    # Werte den LineEdits zuordnen
    mass1_edit.setText(c.get('Parameter', 'm1'))
    mass2_edit.setText(c.get('Parameter', 'm2'))
    len_edit.setText(c.get('Parameter', 'l'))

    dx_edit.setText(c.get('Simulation', 'dx'))
    t_end_edit.setText(c.get('Simulation', 't_end'))


def simulate():
    """
    Diese Funktion liest die Parameter aus allen LineEdits, konvertiert sie in
    floats und führt damit die Simulation aus. Anschließend werden die
    Ergebnisse mit matplotlib dargestellt. Die Startwerte der Simulation sind
    hier noch statisch vorgegeben.
    """

    # Werte holen
    m1 = float(mass1_edit.text())
    m2 = float(mass2_edit.text())
    l = float(len_edit.text())
    dx = float(dx_edit.text())
    t_end = float(t_end_edit.text())

    # oder auch:
    #m = mass1_edit.text().toDouble()[0]   # gibt Tupel ala (wert, OK) zurück

    # Zeitachse anlegen
    t = arange(0, t_end, dx)

    # Simulation ausführen
    res = odeint(rhs, [0, 0.3, 0, 0], t, args=(m1, m2, l))

    # Ergebnisse plotten
    fig = plt.figure(figsize=(18, 6))

    # Hier muss etwas getrickst werden: wir legen einen neuen Dialog an, auf den
    # matplotlib zeichnet. Der plotDialog hat unseren Hauptdialog als parent und
    # ist modeless. Damit können wir beliebig viele Ergebnisfenster parallel
    # darstellen.
    plotDialog = QtWidgets.QDialog(dialog)
    fig.canvas.parent().setParent(plotDialog)

    # Ergebnisse für Laufkatze
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(t, res[:, 0], label='x')
    ax1.plot(t, res[:, 2], label='dx')

    ax1.grid(True)
    ax1.legend()
    ax1.set_ylabel('Laufkatze')

    # Ergebnisse für Last
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(t, res[:, 1], label='phi')
    ax2.plot(t, res[:, 3], label='dphi')

    ax2.grid(True)
    ax2.legend()
    ax2.set_xlabel('Zeit [s]')
    ax2.set_ylabel('Last')

    # Hier wird jetzt der Dialog angezeigt und nicht mehr die show-Funktion von
    # matplotlib aufgerufen!
    plotDialog.show()



# Buttons verknüpfen
sim_button.clicked.connect(simulate)
open_button.clicked.connect(openFile)
save_button.clicked.connect(saveFile)
exit_button.clicked.connect(dialog.close)


#-------------------------------------------------------------------------------

# Dialog anzeigen
dialog.exec_()
