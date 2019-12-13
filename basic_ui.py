from vendor.Qt import QtCore, QtGui, QtWidgets
import sys


# class Panel(QtWidgets.QDialog):
#     def __init__(self):
#         super(Panel, self).__init__()

#         label = QtWidgets.QLabel("Hello Nuke!!")
#         layout = QtWidgets.QHBoxLayout()
#         layout.addWidget(label)
#         self.setLayout(layout)

# class Panel(QtWidgets.QWidget):
#     def __init__(self):
#         super(Panel, self).__init__()

#         list_widget = QtWidgets.QListWidget()
#         list_widget.addItems(["World", "Test", "Welcome"])

#         master_layout = QtWidgets.QHBoxLayout()
#         master_layout.addWidget(list_widget)
#         self.setLayout(master_layout)

class Panel(QtWidgets.QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        table = QtWidgets.QTabWidget()

        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QHBoxLayout()
        layout3 = QtWidgets.QHBoxLayout()

        for i in range(5):
            layout1.addWidget(QtWidgets.QPushButton())

        for i in range(5):
            layout2.addWidget(QtWidgets.QCheckBox())

        for i in range(5):
            layout3.addWidget(QtWidgets.QLineEdit())

        tab1 = QtWidgets.QWidget()
        tab2 = QtWidgets.QWidget()
        tab3 = QtWidgets.QWidget()
        tab1.setLayout(layout1)
        tab2.setLayout(layout2)
        tab3.setLayout(layout3)

        table.addTab(tab1,"Push")
        table.addTab(tab2,"Checkbox")
        table.addTab(tab3,"Line edit")

        master_layout = QtWidgets.QHBoxLayout()
        master_layout.addWidget(table)
        self.setLayout(master_layout)

def showpanel():
    showpanel.panel = Panel()
    showpanel.panel.show()
