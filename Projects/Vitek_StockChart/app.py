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
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QPalette, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtCharts import QCandlestickSeries, QChart, QChartView, QCandlestickSet



class Window(QWidget):
    def change_stock(self) -> None:
        self.update_stock()
        pass

    def update_stock(self) -> None:
        pass

    stock_ticker: str = 'BA'

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("StockChart")

        self.scroll_area = QScrollArea()
        self.vbox = QVBoxLayout()

        # STOCK BUTTON AND LINE EDIT
        

        self.stock_symbol_container = QWidget()
        self.stock_symbol_container.setLayout(QHBoxLayout())

        btn = QPushButton("Aktualizovat")
        btn.clicked.connect(self.change_stock)
        self.stock_symbol_container.layout().addWidget(btn)
        line_edit = QLineEdit(self.stock_ticker)
        self.stock_symbol_container.layout().addWidget(line_edit)

        self.vbox.addWidget(self.stock_symbol_container)

        # VARIABLE GRID

        """ self.variable_store = VariableStore()
        self.grid_for_variables = GridInput(
            list(self.variable_store.variables.values())
        )
        for iovar in self.variable_store.variables.values():
            if not iovar.is_input and not iovar.is_header:
                self.grid_for_variables.set_value(iovar, "")

        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.grid_for_variables)
        self.vbox.sizeHint()

        self.fix_scroll_area_size()
        self.vbox.addWidget(self.scroll_area)

        # CALCULATE, PRINT, PDF BUTTON

        self.calculate_button_container = QWidget()
        self.calculate_button_container.setLayout(QHBoxLayout())

        btn = QPushButton("(1) Vypočítej")
        btn.clicked.connect(self.calculate)
        self.calculate_button_container.layout().addWidget(btn)

        btn = QPushButton("(2) Vytvoř .tex soubor")
        btn.clicked.connect(self.create_tex_file)
        self.calculate_button_container.layout().addWidget(btn)

        btn = QPushButton("(3) pdfLaTeX")
        btn.clicked.connect(self.run_pdflatex)
        self.calculate_button_container.layout().addWidget(btn)

        self.vbox.addWidget(self.calculate_button_container) """

        # MAIN LAYOUT

        self.vbox.addWidget(QLabel("Vytvořil Lukáš Vítek, 2022"))
        self.setLayout(self.vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
