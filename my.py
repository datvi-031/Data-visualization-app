from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib 
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import sip

# canvas object from matplotlib
class MatplotlibCanvas(FigureCanvasQTAgg):
    """docstring for MatplotlibCanvas"""
    def __init__(self, parent=None, width=5, height=4, dpi=120):
        fig = Figure(figsize = (width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        fig.tight_layout()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1420, 879)
        icon = QtGui.QIcon.fromTheme("python")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_choose_theme = QtWidgets.QLabel(self.centralwidget)
        self.label_choose_theme.setStyleSheet("#label_choose_file {\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"}")
        self.label_choose_theme.setObjectName("label_choose_theme")
        self.horizontalLayout.addWidget(self.label_choose_theme)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1041, 0))
        self.tabWidget.setStatusTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1381, 731))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.spacerItem1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 1381, 731))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(self.spacerItem2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1420, 28))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.action_choose_file = QtWidgets.QAction(MainWindow)
        self.action_choose_file.setObjectName("action_choose_file")
        self.actionminimize = QtWidgets.QAction(MainWindow)
        self.actionminimize.setObjectName("actionminimize")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionmin = QtWidgets.QAction(MainWindow)
        self.actionmin.setObjectName("actionmin")
        self.actionmaximize = QtWidgets.QAction(MainWindow)
        self.actionmaximize.setObjectName("actionmaximize")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionmaximize_2 = QtWidgets.QAction(MainWindow)
        self.actionmaximize_2.setObjectName("actionmaximize_2")
        self.actionexit_2 = QtWidgets.QAction(MainWindow)
        self.actionexit_2.setObjectName("actionexit_2")
        self.maximize_window = QtWidgets.QAction(MainWindow)
        self.maximize_window.setObjectName("maximize_window")
        self.normalizewindow = QtWidgets.QAction(MainWindow)
        self.normalizewindow.setObjectName("normalizewindow")
        self.action_exit_window = QtWidgets.QAction(MainWindow)
        self.action_exit_window.setObjectName("action_exit_window")
        self.actionnormal = QtWidgets.QAction(MainWindow)
        self.actionnormal.setObjectName("actionnormal")
        self.actionmaximize_3 = QtWidgets.QAction(MainWindow)
        self.actionmaximize_3.setObjectName("actionmaximize_3")
        self.menufile.addAction(self.action_choose_file)
        self.menufile.addAction(self.action_exit_window)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.action_exit_window.triggered.connect(MainWindow.close) # type: ignore
        self.actionnormal.triggered.connect(MainWindow.showNormal) # type: ignore
        self.actionmaximize_3.triggered.connect(MainWindow.showMaximized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # ======================================================================================================
        self.filename = ''
        self.canv = MatplotlibCanvas(self)
        self.df = []

        ##################################################
        self.toolbar = Navi(self.canv, self.centralwidget)
        self.horizontalLayout.addWidget(self.toolbar)
        ##################################################

        self.themes = ['seaborn']
        self.comboBox.addItems(self.themes)

        self.pushButton.clicked.connect(self.getFile)
        self.comboBox.currentIndexChanged['QString'].connect(self.update)

    def update(self,value):
        print("value from comboBox: ", value)
        plt.clf()
        plt.style.use(value)
        try: 
            self.horizontalLayout.removeWidget(self.toolbar)
            self.verticalLayout_2.removeWidget(self.canv) #tab 1
            self.verticalLayout_3.removeWidget(self.canv) #tab 2
            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None
            self.verticalLayout_2.removeItem(self.spacerItem1)
            self.verticalLayout_3.removeItem(self.spacerItem2)
        except Exception as e:
            print(e)
            pass


        # Adding line plot to tab 1 (verticalLayout_2) --------------------- LINE PLOT
        self.canv1 = MatplotlibCanvas(self)
        self.toolbar = Navi(self.canv1, self.centralwidget)

        # attach matplotlib toolbar
        # widget.setParent(None)
        self.horizontalLayout.removeWidget(self.toolbar)
        self.horizontalLayout.addWidget(self.toolbar)

        self.verticalLayout_2.removeWidget(self.canv1)
        self.verticalLayout_2.addWidget(self.canv1)
        self.canv1.axes.cla()
        ax = self.canv1.axes
        self.df.plot(ax = self.canv1.axes)
        legend = ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Title')
        self.canv1.draw()
        # ------------------------------------------------------------------

        # Adding line plot to tab 2 (verticalLayout_3) --------------------- BAR PLOT
        self.canv2 = MatplotlibCanvas(self)
        self.toolbar = Navi(self.canv2, self.centralwidget)

        # attach matplotlib toolbar
        self.horizontalLayout.removeWidget(self.toolbar)
        self.horizontalLayout.addWidget(self.toolbar)

        self.verticalLayout_3.removeWidget(self.canv2)
        self.verticalLayout_3.addWidget(self.canv2)
        self.canv2.axes.cla()
        ax = self.canv2.axes
        self.df.plot.bar(ax = self.canv2.axes)
        legend = ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Title')
        self.canv2.draw()
        

    def getFile(self):
        """ this function will get the address of the CSV file location.
            also calls readData() function
        """
        self.filename = QFileDialog.getOpenFileName(filter = "csv (*.csv)")[0]
        print("File name: ", self.filename)
        self.readData()

    def readData(self):
        """This function will read the data from the csv file
            using pandas and calls update function to plot the 
        """
        self.df = pd.read_csv(self.filename, encoding='utf-8').fillna(0)
        # themes[0] -> first theme value
        self.update(self.themes[0])
    # ============================================================================================================

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "data visualizer"))
        MainWindow.setStatusTip(_translate("MainWindow", "data visualization"))
        self.label_choose_theme.setText(_translate("MainWindow", "select theme"))
        self.pushButton.setText(_translate("MainWindow", "open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "line"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "histogram"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.action_choose_file.setText(_translate("MainWindow", "select file"))
        self.action_choose_file.setStatusTip(_translate("MainWindow", "choose CSV file"))
        self.actionminimize.setText(_translate("MainWindow", "shrink"))
        self.actionclose.setText(_translate("MainWindow", "exit"))
        self.actionmin.setText(_translate("MainWindow", "mininize"))
        self.actionmaximize.setText(_translate("MainWindow", "maximize"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionmaximize_2.setText(_translate("MainWindow", "maximize"))
        self.actionexit_2.setText(_translate("MainWindow", "exit"))
        self.maximize_window.setText(_translate("MainWindow", "maximize"))
        self.maximize_window.setStatusTip(_translate("MainWindow", "expand the window"))
        self.normalizewindow.setText(_translate("MainWindow", "normal"))
        self.normalizewindow.setStatusTip(_translate("MainWindow", "best fit"))
        self.action_exit_window.setText(_translate("MainWindow", "exit"))
        self.action_exit_window.setStatusTip(_translate("MainWindow", "close the window"))
        self.action_exit_window.setShortcut(_translate("MainWindow", "Shift+C"))
        self.actionnormal.setText(_translate("MainWindow", "normal"))
        self.actionnormal.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionmaximize_3.setText(_translate("MainWindow", "maximize"))
        self.actionmaximize_3.setShortcut(_translate("MainWindow", "Shift+M"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
