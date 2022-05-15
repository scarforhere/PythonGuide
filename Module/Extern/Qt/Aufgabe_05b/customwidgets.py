# -*- coding: utf-8 -*-
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

import configparser as cfg



class NumberInput(QtWidgets.QWidget):
    """
    Widget, welches ein Label zur Beschreibung und ein LineEdit zur Eingabe
    enthält. Die beiden Widgets sind in einem horizontalen Layout angeordnet.
    Werte werden automatisch zwischen QString und float konvertiert, wenn die
    Funktionen setValue und getValue benutzt werden.
    """

    def __init__(self, text, value=0, parent=None):

        # Konstruktor der Basisklase aufrufen
        QtWidgets.QWidget.__init__(self, parent)

        # Widgets anlegen
        self.label = QtWidgets.QLabel(parent)

        self.edit = QtWidgets.QLineEdit(parent)
        self.edit.setAlignment(QtCore.Qt.AlignRight)
        self.edit.setValidator(QtGui.QDoubleValidator(self.edit))

        # Argumente aus Konstruktor setzen
        self.setText(text)
        self.setValue(value)

        # Layout anlegen und zuweisen
        self.hBox = QtWidgets.QHBoxLayout()
        #self.hBox.setMargin(5)
        self.hBox.addWidget(self.label)
        self.hBox.addStretch(1.0)
        self.hBox.addWidget(self.edit)

        self.setLayout(self.hBox)

        # maximale Breite des Eingabefeldes beschränken (Optik)
        self.edit.setMaximumWidth(70)

    def setText(self, text):
        """
        Setzt den Text des Labels:
        """

        if not isinstance(text, str):
            raise TypeError("Argument <text> muss ein string sein.")

        self.label.setText(text)

    def getText(self):
        """
        Gibt den Text des Labels als Python String zurück.
        """

        return str(self.label.text())

    def setValue(self, value):
        """
        Setzt den Wert des Eingabefeldes, erwartet eine Zahl als Argument!
        """

        if not isinstance(value, (int, float)):
            raise TypeError("Argument muss eine Zahl sein.")

        self.edit.setText(str(value))

    def getValue(self):
        """
        Gibt Wert des Eingabefeldes als float zurück.
        """

        return float(str(self.edit.text()))

    # Anlegen der zwei Properties
    # https://docs.python.org/3/library/functions.html#property
    value = property(getValue, setValue)
    text = property(getText, setText)


class ParameterMask(QtWidgets.QWidget):
    """
    Kapselung aller Eingabefelder in einem Widget. Es stellt gleichzeitig
    Funktionen zum Speichern und Laden der Parameter in einer Konfigurations-
    datei bereit.
    """

    def __init__(self, parent=None):

        # Konstruktor der Basisklasse
        QtWidgets.QWidget.__init__(self, parent)


        # Widgets für Parametereingabe
        self.mLaufkatze = NumberInput("Masse Laufkatze", 10, self)
        self.mLast = NumberInput("Masse Last", 2.5, self)
        self.dt = NumberInput("Schrittweite", 0.02, self)
        self.tEnd = NumberInput("Simulationsdauer", 10, self)

        # Layout
        self.vBox = QtWidgets.QVBoxLayout()
        self.vBox.addWidget(self.mLaufkatze)
        self.vBox.addWidget(self.mLast)
        self.vBox.addWidget(self.dt)
        self.vBox.addWidget(self.tEnd)
        self.vBox.addStretch(1.0)
        #self.vBox.setMargin(0)

        self.setLayout(self.vBox)

        # MaximaleBreite beschränken
        self.setMaximumWidth(200)


    def openfile(self):
        """
        Öffnet eine ini-Datei und liest die gespeicherten Daten
        """

        # Dialog zum Öffnen eine Datei
        fName, _filter = QtWidgets.QFileDialog.getOpenFileName(filter="*.ini")

        if not fName:
            return

        # Configparser anlegen
        c = cfg.SafeConfigParser()

        # aus Datei lesen
        if c.read(fName):
            print("Datei erfolgreich geladen: {}".format(fName))
        else:
            print("Keine Konfigurationsdatei geladen")

        # Werte lesen
        self._readparams(c, "Parameter", [self.mLaufkatze, self.mLast])
        self._readparams(c, "Simulation", [self.dt, self.tEnd])

    def _readparams(self, cfgParser, section, paramList):
        """
        Diese Funktion wird nur benötigt, um das Auslesen der Parameter um
        eine Fehlerbehandlung zu erweitern. Argumente sind eine Instanz des
        ConfigParsers, ein String, der die Section angibt, aus der gelesen
        werden soll und eine Liste der Eingabefelder, die belegt werden sollen.

        Die Funktion prüft, ob die Section überhaut in der Datei existiert
        und setzt andernfalls alle Werte auf eins. Vorteil der Fehlerbehandlung
        ist, dass Parameter auch weiter korrekt eingelesen werden, wenn
        zwischendurch ein Wert oder eine Section fehlt.
        """

        # Prüfung, ob Section vorhanden
        try:
            cfgParser.get(section, "")
        except cfg.NoSectionError:
            msg = "Section `{}` existiert nicht in Konfigdatei. " \
                "Setze alle Parameter auf 1."
            print(msg.format(section))

            for p in paramList:
                p.value = 1
            return
        except cfg.NoOptionError:
            pass

        # Lesen der Parameter
        for i in paramList:
            try:
                i.value = float(cfgParser.get(section, i.text))

            except cfg.NoOptionError:
                msg = "Parameter `{0}` existiert nicht in Konfigdatei. " \
                    "Setze `{0}`:=1."
                print(msg.format(i.text))
                i.value = 1

    def savefile(self):
        """
        Dialog zur Auswahl einer Datei öffnen und die aktuellen Parameter darin
        abspeichern
        """

        # Dialog für Dateiname
        fName, _filter = QtWidgets.QFileDialog.getSaveFileName(filter="*.ini")

        if not fName:
            return

        # Configparser anlegen und Daten übergeben
        c = cfg.ConfigParser()

        c.add_section("Parameter")
        c.set("Parameter", self.mLaufkatze.text, str(self.mLaufkatze.value))
        c.set("Parameter", self.mLast.text, str(self.mLast.value))

        c.add_section("Simulation")
        c.set("Simulation", self.dt.text, str(self.dt.value))
        c.set("Simulation", self.tEnd.text, str(self.tEnd.value))

        # Konfig-Datei schreiben
        with open(fName, "w") as fid:
            c.write(fid)


class IVSlider(QtWidgets.QWidget):
    """
    Initial Value Slider (Startwert-Slider)
    Label und Slider zum ändern der Anfangswerte der Simulation. Werden
    in horizontalem Layout angeordnet.
    """

    def __init__(self, text, limits, parent=None):
        """
        Konstruktor

        text - String, Label des Sliders
        limits - Liste oder Tupel mit 2 Werten: min und max des Sliders
        """

        # Konstruktor der Basisklasse
        QtWidgets.QWidget.__init__(self, parent)

        # Label und Slider
        self.label = QtWidgets.QLabel(text)
        self.slider = QtWidgets.QSlider()

        # Limits des Sliders - Achtung: nur Integer Werte erlaubt!
        self.slider.setMinimum(limits[0])
        self.slider.setMaximum(limits[1])

        # Ausrichtung des Sliders
        self.slider.setOrientation(QtCore.Qt.Horizontal)

        # Layout
        self.hBox = QtWidgets.QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.slider)

        self.setLayout(self.hBox)

        # Grössen anpassen
        self.label.setFixedWidth(20)
        self.setMaximumWidth(200)



    def getValue(self):
        """
        Gibt Wert des Sliders als float zurück
        """

        return float(self.slider.value())
