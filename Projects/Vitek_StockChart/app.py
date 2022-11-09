import sys
import pandas as pd
from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QGridLayout,
    QScrollArea,
    QStyle,
    QSizePolicy,
    QMessageBox,
)
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QPalette, QColor, QPainter
from PyQt6.QtCore import Qt
from PyQt6.QtCharts import QCandlestickSeries, QChart, QChartView, QCandlestickSet, QValueAxis, QBarCategoryAxis, QBarSeries, QBarSet, QCategoryAxis, QAbstractAxis, QLineSeries




class Window(QWidget):
    def change_stock_ticker(self, ticker: str) -> None:
        self.stock_ticker = ticker
        #print(self.stock_ticker)

    def update_stock(self) -> None:
        self.series.clear()
        self.chart.removeAllSeries()
        self.downloadData()
        

    stock_ticker = 'AAPL'    
    tm = []  # stores str type data

    def downloadData(self):
        # api key 9FTHOZM5TKJCTYXL
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&datatype=csv&symbol='+self.stock_ticker+'&outputsize=compact&apikey=9FTHOZM5TKJCTYXL'
        try:
            self.df = pd.read_csv(url)
            print(self.df)
            self.processData()
        except KeyError:
            print("nepodařilo se stahnout, špatný ticker")
        except:
            print("nějaká jiná chyba")
        else:
            print("downloaded")
    
    def processData(self):
        

        self.series = QCandlestickSeries()
        self.series.setDecreasingColor(QColor(255,0,0))
        self.series.setIncreasingColor(QColor(0,255,0))
        
        # process data
        for index, row in self.df.iterrows():
            #print(row['open'], row['high'], row['low'], row['close'])
            self.series.append(QCandlestickSet(row['open'], row['high'], row['low'], row['close']))
            timestamp = str(int(row['timestamp'][8:10]))+'.'+str(row['timestamp'][5:7])+'.'
            self.tm.insert(0,timestamp)
            if index == 20-1: break
        


        self.chart = QChart()
        self.chart.addSeries(self.series)  # candles
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.chart.createDefaultAxes()
        self.chart.legend().hide()

        self.axisX = QBarCategoryAxis()
        self.axisX.setLabelsAngle(-90)
        self.axisX.append(self.tm)

        self.axisX.show()
        self.chart.addAxis(self.axisX, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axisX)
        
        self.chart.show()

        
        
        
        
        #self.chart.axes(Qt.AlignmentFlag.AlignBottom, self.axisX)
        #axisX(self.series).setCategories(self.tm)


    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("StockChart")

        self.scroll_area = QScrollArea()
        self.vbox = QVBoxLayout()

        # STOCK BUTTON AND LINE EDIT
        

        self.stock_symbol_container = QWidget()
        self.stock_symbol_container.setLayout(QHBoxLayout())

        btn = QPushButton("Aktualizovat")
        btn.clicked.connect(self.update_stock)
        self.stock_symbol_container.layout().addWidget(btn)
        line_edit = QLineEdit(self.stock_ticker)
        line_edit.textChanged.connect(self.change_stock_ticker)
        self.stock_symbol_container.layout().addWidget(line_edit)

        self.vbox.addWidget(self.stock_symbol_container)

        self.downloadData()

        # VARIABLE GRID
        self.chartview = QChartView(self.chart)
        self.chartview.setObjectName("chartview")
        self.vbox.addWidget(self.chartview)

        # MAIN LAYOUT

        self.vbox.addWidget(QLabel("Vytvořil Lukáš Vítek, 2022"))
        self.setLayout(self.vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(800, 600)
    window.move(300, 100)
    sys.exit(app.exec())
