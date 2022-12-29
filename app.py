#Python app.py
#Importing the libraries
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from random import choice

window_titles = [
  'My app',
  'My App',
  'Still My App',
  'Something went wrong'
]


class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    # self.button_is_checked = True
    self.n_times_clicked = 0

    self.setWindowTitle("App")

    #intializing the button
    self.button = QPushButton("Press the Button!")
    self.button.clicked.connect(self.the_button_was_clicked)

    self.windowTitleChanged.connect(self.the_window_title_changed)

    #Minimum value set for window
    self.setMinimumSize(QSize(300, 200))

    self.setCentralWidget(self.button)
  
  def the_button_was_clicked(self):
    print('Clicked!')
    new_window_title = choice(window_titles)
    print('Setting title: %s' % new_window_title)
    self.setWindowTitle(new_window_title)

  def the_window_title_changed(self, window_title):
    print("Window title chnaged: %s" % window_title)

    if window_title == 'Something went wrong':
      self.button.setDisabled(True)


app = QApplication([])

window = MainWindow()
window.show()

#Event loop
app.exec()