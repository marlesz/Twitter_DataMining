
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy, scipy
import scipy.cluster.hierarchy as hier
import scipy.spatial.distance as dist
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import sys
from PyQt4 import QtCore, QtGui
import wtyczka
import array
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
import os.path
import glob
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtXml import *

class TwitterLocation:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):

        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'TwitterLocation_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&TwitterLocation')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'TwitterLocation')
        self.toolbar.setObjectName(u'TwitterLocation')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):

        return QCoreApplication.translate('TwitterLocation', message)
    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/TwitterLocation/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'TwitterLocation'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&TwitterLocation'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
            #ustanowienie klienta bazy MongoDB
            client = MongoClient('localhost', 27017)

            #dostep do bazy danych
            mydb = client.Twitter

            #dostep do kolekcji
            myCollection = mydb.collect1

            def pushButtonClicked(self):
                #slowa kluczowe
                keyy = self.lineEdit.text()
                keyy = keyy.split(",")
                key = []
                for word in keyy:
                    key.append(str(word))
                #print key
                keywordsCount = []
                dict = []
                for i in key:
                    keywordsCount.append(myCollection.find({'text': {'$regex': i, '$options': 'i'}}).count())
                #print keywordsCount
                #dodaje kolekcje do tablicy
                keyWords = []
                for i in key:
                    for item in myCollection.find({'text': {'$regex': i, '$options': 'i'}}):
                        keyWords.append(item)
                #print 'keyWords:', len(keyWords)
                #zapisuje wspolrzedne do pliku txt
                hospFile = open('C:/Users/ML/OneDrive/GIK/Metody eksploracji danych/Twitter projekt/DataMining/hosp_wsp.txt', 'w')
                for i in range(0, len(keyWords)):
                    keyWords2 = str(keyWords[i]['geo']['coordinates'])
                    hospFile.writelines(str(keyWords2.strip('[]')) +'\n' )
                hospFile.close()

                file = open('C:/Users/ML/OneDrive/GIK/Metody eksploracji danych/Twitter projekt/DataMining/hosp_wsp.txt','r')
                #save the column/row headers (conditions/genes) into an array
                global dataMatrix
                global distanceMatrix
                dataMatrix = []
                for line in file:
                    data = line.strip().split(', ')
                    #rowHeaders.append(data[0])
                    dataMatrix.append([float(x) for x in data[0:]])
                #convert native data array into a numpy array
                global dataMatrix2
                dataMatrix2 = []
                dataMatrix = numpy.array(dataMatrix)
                for i in dataMatrix:
                    if (i[0]<47.7592 and i[0]>47.4792 and i[1]<-122.2421 and i[1]>-122.4440):
                        dataMatrix2.append(i)
                #print dataMatrix
                file.close()
                distanceMatrix = dist.pdist(dataMatrix2, 'euclidean')

                global linkageMatrix
                #Metoda centroidów
                if self.comboBox.currentIndex() == 0:
                    linkageMatrix = hier.linkage(dataMatrix2, 'centroid', 'euclidean')
                #Pojedyńcze wiązanie
                elif self.comboBox.currentIndex() == 1:
                    linkageMatrix = hier.linkage(distanceMatrix, 'single', 'euclidean')
                #Pełne wiązanie
                elif self.comboBox.currentIndex() == 2:
                    linkageMatrix = hier.linkage(distanceMatrix, 'complete', 'euclidean')
                #Wiązanie średnich
                elif self.comboBox.currentIndex() == 3:
                    linkageMatrix = hier.linkage(distanceMatrix, 'average', 'euclidean')

                #Dendrogram
                dendro = scipy.cluster.hierarchy.dendrogram(linkageMatrix, no_plot=False)
                #plt.show()

                fig = plt.figure(1)
                canvas = FigureCanvas(fig)
                canvas.setParent(ui.widget)
                #axes = fig.add_subplot(111)
                toolbar = NavigationToolbar(canvas, ui.widget)
                plotLayout = QtGui.QVBoxLayout()
                plotLayout.addWidget(toolbar)
                plotLayout.addWidget(canvas)
                ui.widget.setLayout(plotLayout)

            def pushButtonClicked2(self):
                global clust
                #Kryterium: distance
                if self.comboBox2.currentIndex() == 0:
                    clust = hier.fcluster(linkageMatrix, self.lineEdit_2.text() , criterion = 'distance')
                #Kryterium: niespojnosc
                elif self.comboBox2.currentIndex() == 1:
                    clust = hier.fcluster(linkageMatrix, self.lineEdit_2.text() , criterion = 'inconsistent')

                result = []
                for i in range(len(clust)):
                    result = result + [[clust[i], dataMatrix2[i][0], dataMatrix2[i][1]]]
                result.sort()
                result = numpy.array(result)
                #print result

                meanx = result[0][1]
                meany = result[0][2]
                count = 1
                final = []

                for i in range(len(clust)):
                    if i < len(clust)-1:
                       if result[i][0] == result[i+1][0]:
                           meanx = meanx + result[i+1][1]
                           meany = meany + result[i+1][2]
                           count = count +1
                       else:
                           meanx = meanx/count
                           meany = meany/count
                           meanxy = [meanx, meany]
                           final.append(meanxy)
                           count = 1
                           meanx = result[i+1][1]
                           mean = result[i+1][2]
                    else:
                       if result[i][0] == result[i-1][0]:
                           meanx = meanx/count
                           meany = meany/count
                           meanxy = [meanx, meany]
                           final.append(meanxy)
                       else:
                           meanx = result[i][1]
                           meany = result[i][2]
                           meany = [meanx, meany]
                           final.append(meanxy)

                #print final

                file2 = open('C:/Users/ML/OneDrive/GIK/Metody eksploracji danych/Twitter projekt/DataMining/final.csv', 'w')
                for i in range(len(final)):
                         #final2 = str(final[i])
                         file2.writelines(str(final[i]).strip('[]'))
                         file2.writelines("\n")
                file2.close()

                mapinstance = QgsMapLayerRegistry.instance()
                uri = "file:///C:/Users/ML/OneDrive/GIK/Metody eksploracji danych/Twitter projekt/DataMining/final.csv?delimiter=%s&xField=%s&yField=%s&useHeader=no&crs=epsg:4326" % (",", "field_2","field_1")
                punkty = iface.addVectorLayer(uri, "klasteryzacja", "delimitedtext")
                renderer = punkty.rendererV2()
                symbol = QgsMarkerSymbolV2.createSimple({'name': 'circle', 'color': 'red', 'size' : '3'})
                punkty.rendererV2().setSymbol(symbol)
                mapinstance.addMapLayer(punkty)

                uri2 = "file:///C:/Users/ML/OneDrive/GIK/Metody eksploracji danych/Twitter projekt/DataMining/hosp_wsp.txt?delimiter=%s&xField=%s&yField=%s&useHeader=no&crs=epsg:4326" % (",", "field_2","field_1")
                punkty2 = iface.addVectorLayer(uri2, "tweety", "delimitedtext")
                renderer2 = punkty2.rendererV2()
                symbol2 = QgsMarkerSymbolV2.createSimple({'name': 'circle', 'color': 'blue', 'size' : '1'})
                punkty2.rendererV2().setSymbol(symbol2)
                mapinstance.addMapLayer(punkty2)

            def main():
                 #import sys
                 #app = QtGui.QApplication(sys.argv)
                 MainWindow = QtGui.QDialog() # <-- Instantiate QMainWindow object.
                 global ui
                 ui = wtyczka.Ui_Form()
                 ui.setupUi(MainWindow)
                 ui.pushButton2.clicked.connect(lambda: pushButtonClicked(ui))
                 ui.pushButton.clicked.connect(lambda: pushButtonClicked2(ui))
                 MainWindow.show()
                 MainWindow.exec_()

            main()
            client.close()

