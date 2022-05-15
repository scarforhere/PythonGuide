import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

import pyqtgraph as pg
import numpy as np
import scipy.integrate

import customwidgets as cw
import cart_pendulum_model


class Gui(QtWidgets.QMainWindow):
    """
    Eigene Klasse (abgeleitet von QMainWindow)
    """
    def __init__(self):
        # Konstruktor der Basis-Klass aufrufen
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowTitle('Pendelsimulation')
        self.setWindowIcon(QtGui.QIcon(r'E:\Die Schulfach im TUD\Python\kurs05\05b_GUI2\data\laufkatze.png'))

        self.centralwg = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwg)

        self.parameter_mask = cw.ParameterMask(parent=self.centralwg)

        self.scene = pg.PlotWidget()
        # bewirkt dass ein x und y auf Bildschirm gleich skalliert sind:
        self.scene.setAspectLocked()

        # iv bedeutet Initial-Value
        self.iv_slider_x = cw.IVSlider('x0', limits=(-1000, 1000))
        self.iv_slider_phi = cw.IVSlider('phi0', limits=(-180, 180))

        # slider für die Pendel-Länge
        self.slider_l = cw.IVSlider('l', limits=(0, 300))

        # Layout
        self.hbox = QtWidgets.QGridLayout()
        self.hbox.addWidget(self.parameter_mask, 0, 0)

        self.hbox.addWidget(self.iv_slider_x, 1, 0)
        self.hbox.addWidget(self.iv_slider_phi, 2, 0)
        self.hbox.addWidget(self.slider_l, 3, 0)

        self.hbox.addWidget(self.scene, 0, 1, 4, 1)  # mit rowspan=4, colspan=1
        self.centralwg.setLayout(self.hbox)

        # Actions für Dateimenü (Open, Save, Exit)
        # Einstellungen mit mehreren Aufrufen vornehmen
        self.actn_open = QtWidgets.QAction(self)
        self.actn_open.setText('Laden...')
        self.actn_open.setShortcut(QtGui.QKeySequence.Open)
        self.actn_open.setIcon(QtGui.QIcon('../data/open.png'))
        self.actn_open.triggered.connect(self.parameter_mask.openfile)

        # Action kann auch mit einem Aufruf erfolgen:
        self.actn_save = QtWidgets.QAction(QtGui.QIcon('../data/save.png'),
                'Speichern...', self, shortcut=QtGui.QKeySequence.Save,
                                       statusTip="Parameterdatei speichern",
                                       triggered=self.parameter_mask.savefile)

        self.actn_exit = QtWidgets.QAction("Beenden", self, shortcut="Ctrl+Q",
                                       statusTip="Programm beenden", triggered=self.close)

        # Status der Wiedergabe speichern
        self.is_playing = False

        # Instanzvariablen für die Konfigurationskoordinaten des Systems u. Pendellänge anlegen
        self.x = 0
        self.phi = 0.25*np.pi
        self.l = 1

        # Actions für Simulationssteuerung
        self.actn_start_anim = QtWidgets.QAction(self)
        self.actn_start_anim.setText('Play')
        self.actn_start_anim.setIcon(QtGui.QIcon('../data/play.png'))
        self.actn_start_anim.triggered.connect(self.start_animation)

        self.actn_stop_anim = QtWidgets.QAction(self)
        self.actn_stop_anim.setText('Play')
        self.actn_stop_anim.setIcon(QtGui.QIcon('../data/stop.png'))
        self.actn_stop_anim.triggered.connect(self.stop_animation)

        # Actions für Simulationssteuerung
        self.actn_toggle_anim = QtWidgets.QAction(self)
        self.actn_toggle_anim.setText('Play')
        self.actn_toggle_anim.setIcon(QtGui.QIcon('../data/play.png'))
        self.actn_toggle_anim.triggered.connect(self.toggle_animation)

        # Menüs zusammenbauen
        self.menu_file = self.menuBar().addMenu('&Datei')
        self.menu_file.addAction(self.actn_open)
        self.menu_file.addAction(self.actn_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actn_exit)

        # Toolbar für Dateimenü erstellen und mit Actions füttern
        self.toolbar_file = QtWidgets.QToolBar('Datei')
        self.toolbar_file.setIconSize(QtCore.QSize(24, 24))
        self.addToolBar(self.toolbar_file)
        self.toolbar_file.addAction(self.actn_open)
        self.toolbar_file.addAction(self.actn_save)

        # Toolbar für Simulation erstellen und mit Actions füttern
        self.toolbar_sim = QtWidgets.QToolBar('Simulation')
        self.toolbar_file.setIconSize(QtCore.QSize(24, 24))
        self.addToolBar(self.toolbar_sim)
        self.toolbar_sim.addAction(self.actn_toggle_anim)
        # self.toolbar_sim.addAction(self.actn_start_anim)
        # self.toolbar_sim.addAction(self.actn_stop_anim)

        # Slider-Änderungs-Signal mit Slot verbinden
        self.iv_slider_x.slider.valueChanged.connect(self.setx)
        self.iv_slider_x.slider.valueChanged.connect(self.draw_cart_pendulum)
        self.iv_slider_phi.slider.valueChanged.connect(self.setphi)
        self.iv_slider_phi.slider.valueChanged.connect(self.draw_cart_pendulum)

        self.slider_l.slider.valueChanged.connect(self.change_pendulum_length)
        self.slider_l.slider.valueChanged.connect(self.draw_cart_pendulum)

        # Die Start-Werte der Variablen self.x, self.phi und self.l sollten von Beginn an
        # durch die Slider dargestellt werden:
        self.slider_l.slider.setValue((self.l-0.3)*100)

        self.draw_cart_pendulum()

    def setx(self, x):
        self.x = x / 1000

    def setphi(self, phi):
        self.phi = phi / 180 * np.pi

    def draw_cart_pendulum(self):
        self.scene.clear()
        x_range = np.array([-2, 2])
        y_range = x_range - 1.0
        self.scene.setRange(xRange=x_range, yRange=y_range)
        dx = .1
        dy = .05
        # Eckpunkte eines Rechtecks (Mittelpunkt (x, 0) beginnend links unten)
        xvalues_cart = self.x + np.array([-dx, -dx, dx, dx, -dx])
        yvalues_cart = np.array([-dy, dy, dy, -dy, -dy])

        # Position der Aufhängung (joint) und der Last ("tip")
        l = self.l
        x_joint = self.x
        y_joint = 0
        x_tip = x_joint + l*np.sin(self.phi)
        y_tip = y_joint - l*np.cos(self.phi)
        self.scene.plot(xvalues_cart, yvalues_cart)
        self.scene.plot([x_joint, x_tip], [y_joint, y_tip], symbol='o')

    def toggle_animation(self):
        """
        Zwischen Wiedergabe und Stop umschalten
        """

        if self.is_playing:
            self.stop_animation()
            self.is_playing = False

        else:
            self.start_animation()
            self.is_playing = True

    def start_animation(self):
        """
        Starten der Simulation bzw. Animation. Dabei wird einfach ein Timer
        angelegt, der das System jede ms aktualisiert.
        """

        self.init_solver()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.calc_step)
        dt = float(self.parameter_mask.dt.getValue())*1000
        self.timer.start(dt)

        self.actn_toggle_anim.setText('Stop')
        self.actn_toggle_anim.setIcon(QtGui.QIcon('../data/stop.png'))

    def stop_animation(self):
        """
        Beendet die Animation und setzt das System auf die Startwerte zurück.
        Dabei wird einfach der Timer, der in self.startAnimation() angelegt
        wurde, gelöscht.
        """

        # timer löschen
        del self.timer

        self.actn_toggle_anim.setText('Play')
        self.actn_toggle_anim.setIcon(QtGui.QIcon('../data/play.png'))

    def init_solver(self):
        """
        Solver anlegen und Parameter (Schrittweite und Massen) übergeben
        """

        # Solver

        self.solver = scipy.integrate.ode(cart_pendulum_model.rhs)
        initial_state = [self.x, self.phi, 0, 0]
        self.solver.set_initial_value(initial_state)
        self.solver.set_integrator('vode', method='adams', rtol=1e-6, atol=1e-9)

        # Schrittweite
        self.dt = self.parameter_mask.dt.value

        # aktuelle Parameter holen und setzen
        m1 = self.parameter_mask.mLaufkatze.value
        m2 = self.parameter_mask.mLast.value
        self.solver.set_f_params(m1, m2)

    def calc_step(self):
        """
        Funktion zur Berechnung eines einzelnen Integrationsschrittes.
        Szene wird anschliessend aktualisiert.
        """

        # einen Schritt rechnen
        xx = self.solver.integrate(self.solver.t + self.dt)
        self.x, self.phi = xx[:2]

        # Szene aktualisieren
        self.draw_cart_pendulum()

    def change_pendulum_length(self, l):
        """
        Slider-Werte für Pendellänge verarbeiten
        """
        self.l = l/100.0 + 0.3  # Absolutwert und Skalierung
        cart_pendulum_model.l = self.l

app = QtWidgets.QApplication([])

gui = Gui()  # Instanz von obiger Klasse anlegen
gui.show()
app.exec_()
