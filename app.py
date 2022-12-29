#Python app.py
#Importing the libraries
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()

    self.button_is_checked = True

    self.setWindowTitle("App")

    #intializing the button
    button = QPushButton("Press the Button!")
    button.setCheckable(True)
    button.clicked.connect(self.the_button_was_clicked)
    button.clicked.connect(self.the_button_was_toggled)
    button.setChecked(self.button_is_checked)

    #Minimum value set for window
    self.setMinimumSize(QSize(300, 200))

    self.setCentralWidget(button)
  
  def the_button_was_clicked(self):
    print('Clicked!')

  def the_button_was_toggled(self, checked):
    self.button_is_checked = checked

    print(self.button_is_checked)


app = QApplication([])

window = MainWindow()
window.show()

#Event loop
app.exec()