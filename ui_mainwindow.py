# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(559, 511)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.destino_x_spinBox = QSpinBox(self.groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destino_x_spinBox, 3, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 11, 2, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destino_y_spinBox, 4, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.velocidad_lineEdit = QLineEdit(self.groupBox)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")

        self.gridLayout.addWidget(self.velocidad_lineEdit, 5, 2, 1, 1)

        self.orden_velocidad_pushButton = QPushButton(self.groupBox)
        self.orden_velocidad_pushButton.setObjectName(u"orden_velocidad_pushButton")

        self.gridLayout.addWidget(self.orden_velocidad_pushButton, 16, 0, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 11, 0, 1, 1)

        self.RGB_green_spinBox = QSpinBox(self.groupBox)
        self.RGB_green_spinBox.setObjectName(u"RGB_green_spinBox")
        self.RGB_green_spinBox.setMaximum(250)

        self.gridLayout.addWidget(self.RGB_green_spinBox, 9, 2, 1, 1)

        self.RGB_red_spinBox = QSpinBox(self.groupBox)
        self.RGB_red_spinBox.setObjectName(u"RGB_red_spinBox")
        self.RGB_red_spinBox.setMaximum(250)

        self.gridLayout.addWidget(self.RGB_red_spinBox, 8, 2, 1, 1)

        self.RGB_blue_spinBox = QSpinBox(self.groupBox)
        self.RGB_blue_spinBox.setObjectName(u"RGB_blue_spinBox")
        self.RGB_blue_spinBox.setMaximum(250)
        self.RGB_blue_spinBox.setValue(0)

        self.gridLayout.addWidget(self.RGB_blue_spinBox, 10, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.orden_distancia_pushButton = QPushButton(self.groupBox)
        self.orden_distancia_pushButton.setObjectName(u"orden_distancia_pushButton")

        self.gridLayout.addWidget(self.orden_distancia_pushButton, 16, 2, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)
        self.origen_y_spinBox.setValue(0)

        self.gridLayout.addWidget(self.origen_y_spinBox, 2, 2, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)
        self.origen_x_spinBox.setValue(0)

        self.gridLayout.addWidget(self.origen_x_spinBox, 1, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout.addWidget(self.id_lineEdit, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 14, 0, 1, 1)

        self.orden_id_pushButton = QPushButton(self.groupBox)
        self.orden_id_pushButton.setObjectName(u"orden_id_pushButton")

        self.gridLayout.addWidget(self.orden_id_pushButton, 14, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 2, 0, 1, 1)

        self.tabla_tableWidget = QTableWidget(self.tab_2)
        self.tabla_tableWidget.setObjectName(u"tabla_tableWidget")

        self.gridLayout_4.addWidget(self.tabla_tableWidget, 0, 0, 1, 4)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 2, 1, 1, 1)

        self.pushButton_orden_id_tabla = QPushButton(self.tab_2)
        self.pushButton_orden_id_tabla.setObjectName(u"pushButton_orden_id_tabla")

        self.gridLayout_4.addWidget(self.pushButton_orden_id_tabla, 2, 3, 1, 1)

        self.mostrar_pushButton_2 = QPushButton(self.tab_2)
        self.mostrar_pushButton_2.setObjectName(u"mostrar_pushButton_2")

        self.gridLayout_4.addWidget(self.mostrar_pushButton_2, 2, 2, 1, 1)

        self.pushButton_orden_velocidad_tabla = QPushButton(self.tab_2)
        self.pushButton_orden_velocidad_tabla.setObjectName(u"pushButton_orden_velocidad_tabla")

        self.gridLayout_4.addWidget(self.pushButton_orden_velocidad_tabla, 3, 2, 1, 1)

        self.pushButton_orden_distancia_tabla = QPushButton(self.tab_2)
        self.pushButton_orden_distancia_tabla.setObjectName(u"pushButton_orden_distancia_tabla")

        self.gridLayout_4.addWidget(self.pushButton_orden_distancia_tabla, 3, 3, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_5.addWidget(self.dibujar, 1, 0, 1, 1)

        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_5.addWidget(self.limpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 559, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Captura de Particulas", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino en x:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.orden_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por velocidad", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"RGB", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.orden_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por distancia", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino en y:", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.orden_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Id", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de la part\u00edcula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_orden_id_tabla.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Id", None))
        self.mostrar_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_orden_velocidad_tabla.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Velocidad", None))
        self.pushButton_orden_distancia_tabla.setText(QCoreApplication.translate("MainWindow", u"Orrdenar por Distancia", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

