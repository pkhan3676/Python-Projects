#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 10:30:50 2025

@author: gani
"""



import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QThread, pyqtSignal
import time
import sys

# Import GUI (contains class Ui_Dialog)
from threadgui import Ui_Dialog

# Data source function
def data_source():
    t = time.time()
    return np.sin(0.9 * t) + np.sin(1.1 * t)

# Thread class for data acquisition
class data_acquisition_thread(QThread):
    new_value = pyqtSignal(float)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            value = data_source()
            self.new_value.emit(value)
            time.sleep(0.1)

    def stop(self):
        self.running = False

# Main window class
class simple_counter_window(QMainWindow):
    def __init__(self):
        super(simple_counter_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.start_button.clicked.connect(self.start_acquisition)
        self.ui.stop_button.clicked.connect(self.stop_acquisition)

        # Setup matplotlib canvas
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.ui.verticalLayout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111)
        self.x_data = []
        self.y_data = []

    def start_acquisition(self):
        self.gani = data_acquisition_thread()
        self.gani.new_value.connect(self.update_plot)
        self.gani.start()

    def stop_acquisition(self):
        if hasattr(self, 'thread'):
            self.gani.stop()
            self.gani.wait()

    def update_plot(self, value):
        current_time = time.time()
        self.x_data.append(current_time)
        self.y_data.append(value)

        # Keep only the last 100 points
        self.x_data = self.x_data[-100:]
        self.y_data = self.y_data[-100:]

        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, color='blue')
        self.ax.set_title("Real-time Data Acquisition")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Value")
        self.canvas.draw()

# Run the application
app = QApplication(sys.argv)
window = simple_counter_window()
window.show()
app.exec_()