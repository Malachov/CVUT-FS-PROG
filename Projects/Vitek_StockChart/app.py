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
    QSpinBox
)
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QPalette, QColor, QPainter
from PyQt6.QtCore import Qt
from PyQt6.QtCharts import QCandlestickSeries, QChart, QChartView, QCandlestickSet, QValueAxis, QBarCategoryAxis, QBarSeries, QBarSet, QCategoryAxis, QAbstractAxis, QLineSeries




class Window(QWidget):
    def change_stock_ticker(self, ticker: str) -> None:
        self.stock_ticker = ticker
        #print(self.stock_ticker)
    
    def update_stock(self) -> None:
        self.downloadData()
        #self.chartview.update()
        #self.series.append(QCandlestickSet(120,150,105,130))
        #self.axisX.append(str('12.11.'))
    
    def change_market_days(self, days: int) -> None:
        self.market_days_shown = days
        #print(self.market_days_shown)
        self.processData()
        #self.chartview.update()

    stock_ticker = 'AAPL'
    market_days_shown = 20
    tm = []  # stores str type data

    def downloadData(self) -> None:
        # api key 9FTHOZM5TKJCTYXL
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&datatype=csv&symbol='+self.stock_ticker+'&outputsize=compact&apikey=9FTHOZM5TKJCTYXL'
        try:
            self.df = pd.read_csv(url)
            #print(self.df)
            self.processData()
        except KeyError:
            print("nepodařilo se stahnout, špatný ticker")
        except:
            print("nějaká jiná chyba")
        else:
            print("downloaded")
    
    def processData(self) -> None:
        self.series.clear()
        self.axisX.clear()
        self.tm = []

        y_min, y_max = (
            float("inf"),
            -float("inf"),
        )
        # process data
        for index, row in self.df.iterrows():
            self.series.insert(0,QCandlestickSet(row['open'], row['high'], row['low'], row['close']))
            timestamp = str(int(row['timestamp'][8:10]))+'.'+str(row['timestamp'][5:7])+'.'
            self.tm.insert(0,timestamp)
            y_min = min(y_min, row['open'], row['high'], row['low'], row['close'])
            y_max = max(y_max, row['open'], row['high'], row['low'], row['close'])
            if index == self.market_days_shown-1: break
        
        self.axisY.setMax(y_max)
        self.axisY.setMin(y_min)
        
        self.axisX.append(self.tm)
        
        



        #print("count:",self.series.count())
        #self.chart.update()
        #self.chart.show()

        


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

        spinbox = QSpinBox()
        spinbox.setRange(15,100) # number of market days shown allowed
        spinbox.setValue(20) # set initial value
        spinbox.valueChanged.connect(self.change_market_days)
        self.stock_symbol_container.layout().addWidget(spinbox)

        self.vbox.addWidget(self.stock_symbol_container)

        self.series = QCandlestickSeries()
        self.series.setDecreasingColor(QColor(255,0,0))
        self.series.setIncreasingColor(QColor(0,255,0))

        self.chart = QChart()
        self.chart.addSeries(self.series)  # candles
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.chart.legend().hide()
        
        self.axisY = QValueAxis()   # axis Y
        self.axisY.show()
        self.chart.addAxis(self.axisY, Qt.AlignmentFlag.AlignLeft)

        self.axisX = QBarCategoryAxis() # axis X
        self.axisX.setLabelsAngle(-90)
        self.axisX.show()
        self.chart.addAxis(self.axisX, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axisX)



        self.downloadData()
        self.chart.show()

        # VARIABLE GRID
        self.chartview = QChartView(self.chart)
        self.chartview.setUpdatesEnabled(True)
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
