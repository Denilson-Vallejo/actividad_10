from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from actividad_9.algoritmos import distancia_euclidiana
from actividad_9.gestion_particulas import Gestor_Particulas
from actividad_9.particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.gestor_particulas = Gestor_Particulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)


    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.gestor_particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio con exito el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self, 
                "Error",
                "No se pudo abrir con exito el archivo" + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.gestor_particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Guardado",
                "Se guardo con éxito el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo almacenar el archivo" + ubicacion
            )

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.gestor_particulas))
    
    @Slot()
    def click_agregar_final(self):
        ID = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red =self.ui.RGB_red_spinBox.value()
        green = self.ui.RGB_green_spinBox.value()
        blue = self.ui.RGB_blue_spinBox.value()

        particula = Particula(ID, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.gestor_particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        ID = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red =self.ui.RGB_red_spinBox.value()
        green = self.ui.RGB_green_spinBox.value()
        blue = self.ui.RGB_blue_spinBox.value()

        particula = Particula(ID, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.gestor_particulas.agregar_inicio(particula)
