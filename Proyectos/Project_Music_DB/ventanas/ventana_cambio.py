# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanas/ventana_cambio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registro_window(object):
    def setupUi(self, registro_window):
        registro_window.setObjectName("registro_window")
        registro_window.resize(800, 630)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        registro_window.setPalette(palette)
        registro_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        registro_window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(registro_window)
        palette = QtGui.QPalette()
        gradient = QtGui.QConicalGradient(0.5, 0.5, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 235, 235, 206))
        gradient.setColorAt(0.258706, QtGui.QColor(255, 188, 188, 80))
        gradient.setColorAt(0.425, QtGui.QColor(255, 132, 132, 156))
        gradient.setColorAt(0.44, QtGui.QColor(252, 128, 128, 80))
        gradient.setColorAt(0.507463, QtGui.QColor(255, 162, 162, 80))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(0.5, 0.5, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 235, 235, 206))
        gradient.setColorAt(0.258706, QtGui.QColor(255, 188, 188, 80))
        gradient.setColorAt(0.425, QtGui.QColor(255, 132, 132, 156))
        gradient.setColorAt(0.44, QtGui.QColor(252, 128, 128, 80))
        gradient.setColorAt(0.507463, QtGui.QColor(255, 162, 162, 80))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(0.5, 0.5, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 235, 235, 206))
        gradient.setColorAt(0.258706, QtGui.QColor(255, 188, 188, 80))
        gradient.setColorAt(0.425, QtGui.QColor(255, 132, 132, 156))
        gradient.setColorAt(0.44, QtGui.QColor(252, 128, 128, 80))
        gradient.setColorAt(0.507463, QtGui.QColor(255, 162, 162, 80))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QConicalGradient(0.5, 0.5, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 235, 235, 206))
        gradient.setColorAt(0.258706, QtGui.QColor(255, 188, 188, 80))
        gradient.setColorAt(0.425, QtGui.QColor(255, 132, 132, 156))
        gradient.setColorAt(0.44, QtGui.QColor(252, 128, 128, 80))
        gradient.setColorAt(0.507463, QtGui.QColor(255, 162, 162, 80))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(0.5, 0.5, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 235, 235, 206))
        gradient.setColorAt(0.258706, QtGui.QColor(255, 188, 188, 80))
        gradient.setColorAt(0.425, QtGui.QColor(255, 132, 132, 156))
        gradient.setColorAt(0.44, QtGui.QColor(252, 128, 128, 80))
        gradient.setColorAt(0.507463, QtGui.QColor(255, 162, 162, 80))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(0.5, 0.5, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 235, 235, 206))
        gradient.setColorAt(0.258706, QtGui.QColor(255, 188, 188, 80))
        gradient.setColorAt(0.425, QtGui.QColor(255, 132, 132, 156))
        gradient.setColorAt(0.44, QtGui.QColor(252, 128, 128, 80))
        gradient.setColorAt(0.507463, QtGui.QColor(255, 162, 162, 80))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QConicalGradient(0.5, 0.5, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 235, 235, 206))
        gradient.setColorAt(0.258706, QtGui.QColor(255, 188, 188, 80))
        gradient.setColorAt(0.425, QtGui.QColor(255, 132, 132, 156))
        gradient.setColorAt(0.44, QtGui.QColor(252, 128, 128, 80))
        gradient.setColorAt(0.507463, QtGui.QColor(255, 162, 162, 80))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(0.5, 0.5, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 235, 235, 206))
        gradient.setColorAt(0.258706, QtGui.QColor(255, 188, 188, 80))
        gradient.setColorAt(0.425, QtGui.QColor(255, 132, 132, 156))
        gradient.setColorAt(0.44, QtGui.QColor(252, 128, 128, 80))
        gradient.setColorAt(0.507463, QtGui.QColor(255, 162, 162, 80))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(0.5, 0.5, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 235, 235, 206))
        gradient.setColorAt(0.258706, QtGui.QColor(255, 188, 188, 80))
        gradient.setColorAt(0.425, QtGui.QColor(255, 132, 132, 156))
        gradient.setColorAt(0.44, QtGui.QColor(252, 128, 128, 80))
        gradient.setColorAt(0.507463, QtGui.QColor(255, 162, 162, 80))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 235, 235, 206), stop:0.258706 rgba(255, 188, 188, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:0.507463 rgba(255, 162, 162, 80), stop:1 rgba(255, 255, 255, 0));")
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_nueva_cancion = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nueva_cancion.setGeometry(QtCore.QRect(20, 40, 361, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.lbl_nueva_cancion.setFont(font)
        self.lbl_nueva_cancion.setObjectName("lbl_nueva_cancion")
        self.btn_cambiar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cambiar.setGeometry(QtCore.QRect(350, 470, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(9)
        self.btn_cambiar.setFont(font)
        self.btn_cambiar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_cambiar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ventanas\\guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cambiar.setIcon(icon)
        self.btn_cambiar.setIconSize(QtCore.QSize(50, 50))
        self.btn_cambiar.setObjectName("btn_cambiar")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 140, 641, 331))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.fly_datos_registro = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.fly_datos_registro.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.fly_datos_registro.setContentsMargins(0, 22, 0, 0)
        self.fly_datos_registro.setVerticalSpacing(31)
        self.fly_datos_registro.setObjectName("fly_datos_registro")
        self.lbl_titulo = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.fly_datos_registro.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_titulo)
        self.txt_titulo = QtWidgets.QLineEdit(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.txt_titulo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.txt_titulo.setFont(font)
        self.txt_titulo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_titulo.setObjectName("txt_titulo")
        self.fly_datos_registro.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_titulo)
        self.lbl_artista = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.lbl_artista.setFont(font)
        self.lbl_artista.setObjectName("lbl_artista")
        self.fly_datos_registro.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_artista)
        self.txt_artista = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.txt_artista.setFont(font)
        self.txt_artista.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_artista.setObjectName("txt_artista")
        self.fly_datos_registro.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_artista)
        self.lbl_album = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.lbl_album.setFont(font)
        self.lbl_album.setObjectName("lbl_album")
        self.fly_datos_registro.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_album)
        self.txt_album = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.txt_album.setFont(font)
        self.txt_album.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_album.setObjectName("txt_album")
        self.fly_datos_registro.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_album)
        self.lbl_anio = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.lbl_anio.setFont(font)
        self.lbl_anio.setObjectName("lbl_anio")
        self.fly_datos_registro.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_anio)
        self.txt_anio = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.txt_anio.setFont(font)
        self.txt_anio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_anio.setObjectName("txt_anio")
        self.fly_datos_registro.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_anio)
        self.lbl_estilo = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.lbl_estilo.setFont(font)
        self.lbl_estilo.setObjectName("lbl_estilo")
        self.fly_datos_registro.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_estilo)
        self.txt_estilo = QtWidgets.QLineEdit(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.txt_estilo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.txt_estilo.setFont(font)
        self.txt_estilo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_estilo.setObjectName("txt_estilo")
        self.fly_datos_registro.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_estilo)
        registro_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(registro_window)
        QtCore.QMetaObject.connectSlotsByName(registro_window)

    def retranslateUi(self, registro_window):
        _translate = QtCore.QCoreApplication.translate
        registro_window.setWindowTitle(_translate("registro_window", "Registro de Canciones"))
        self.lbl_nueva_cancion.setText(_translate("registro_window", "<html><head/><body><p><span style=\" font-weight:600; color:#a7115b;\">ACTUALIZAR CANCIÓN</span></p></body></html>"))
        self.lbl_titulo.setText(_translate("registro_window", "Título:"))
        self.lbl_artista.setText(_translate("registro_window", "Artista:"))
        self.lbl_album.setText(_translate("registro_window", "Album:"))
        self.lbl_anio.setText(_translate("registro_window", "Año:"))
        self.lbl_estilo.setText(_translate("registro_window", "Estilo:"))
