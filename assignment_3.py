# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 00:20:30 2025

@author: pkhan
"""

# QtDesigner_example.py

#

# Conrad Wolf

# 2025-09-17

# modified prince
 
import numpy as np

import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog

from  matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import sys
 
# Import GUI (conatins class Ui_MainWindow)

from plot_graph import Ui_Dialog

class QtDesigner_example_window(QMainWindow):               # Generate class for main window

    def __init__(self):                                     # Constructor of class

        super(QtDesigner_example_window, self).__init__()   # Call constructor of parent class

        self.ui = Ui_Dialog()                           # Create object that contains GUI elements from library

        self.ui.setupUi(self)                               # Initialize GUI elements


        self.ui.pushButton_load.clicked.connect(self.load_file)

        self.ui.pushButton_2.clicked.connect(self.plot_derivative)

        self.ui.pushButton.clicked.connect(self.plot_integral)
    def load_file(self):

        file,rubbish = QFileDialog.getOpenFileName(self)

        print(file)

        self.data=np.loadtxt(file)

        print(self.data)


    def plot_derivative(self):

        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))

        self.ui.verticalLayout.addWidget(self.canvas)  # Ensure verticalLayout exists in your .ui file

        self.canvas.axes = self.canvas.figure.add_subplot(111)

        x = self.data[:, 0]

        y = self.data[:, 1]
 
        self.canvas.axes.clear()

        self.canvas.axes.plot(x, y, color='green')

        self.canvas.axes.set_xlabel('x')

        self.canvas.axes.set_ylabel('y')

        self.canvas.axes.set_title('Plot of y vs x')

        self.canvas.draw()

        # self.data.setEnabled(False)

        # self.ui.pushButton_cos.setEnabled(True)

        # self.ui.label_title.setText('derivative')

    def plot_integral(self):

        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))

        self.ui.verticalLayout.addWidget(self.canvas)  # Ensure verticalLayout exists in your .ui file

        self.canvas.axes = self.canvas.figure.add_subplot(111)

        x = self.data[:, 0]

        y = self.data[:, 1]
 
        self.canvas.axes.clear()

        self.canvas.axes.plot(x, y, color='red')

        self.canvas.axes.set_xlabel('x')

        self.canvas.axes.set_ylabel('y')

        self.canvas.axes.set_title('Plot of integral y vs x')

        self.canvas.draw()



 
app = QApplication(sys.argv)

window = QtDesigner_example_window()

window.show()

app.exec_()

 