import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox, \
    QMessageBox
import pandas as pd


class ExcelMergerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.merge_button = None
        self.merge_type = None
        self.merge_type_label = None
        self.browse2_button = None
        self.file2_path = None
        self.file2_label = None
        self.browse1_button = None
        self.file1_path = None
        self.file1_label = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Excel File Merger')
        self.setGeometry(100, 100, 600, 200)

        layout = QVBoxLayout()

        self.file1_label = QLabel('Select First Excel File:')
        layout.addWidget(self.file1_label)
        self.file1_path = QLineEdit(self)
        layout.addWidget(self.file1_path)
        self.browse1_button = QPushButton('Browse', self)
        self.browse1_button.clicked.connect(self.browse_file1)
        layout.addWidget(self.browse1_button)

        self.file2_label = QLabel('Select Second Excel File:')
        layout.addWidget(self.file2_label)
        self.file2_path = QLineEdit(self)
        layout.addWidget(self.file2_path)
        self.browse2_button = QPushButton('Browse', self)
        self.browse2_button.clicked.connect(self.browse_file2)
        layout.addWidget(self.browse2_button)

        self.merge_type_label = QLabel('Select Merge Type:')
        layout.addWidget(self.merge_type_label)
        self.merge_type = QComboBox(self)
        self.merge_type.addItems(['inner', 'outer', 'left', 'right', 'cross'])
        layout.addWidget(self.merge_type)

        self.merge_button = QPushButton('Merge', self)
        self.merge_button.clicked.connect(self.merge_files)
        layout.addWidget(self.merge_button)

        self.setLayout(layout)

    def browse_file1(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Excel File', '', 'Excel Files (*.xlsx *.xls)')
        if file_path:
            self.file1_path.setText(file_path)

    def browse_file2(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Excel File', '', 'Excel Files (*.xlsx *.xls)')
        if file_path:
            self.file2_path.setText(file_path)

    def merge_files(self):
        file1 = self.file1_path.text()
        file2 = self.file2_path.text()
        merge_type = self.merge_type.currentText()

        if not file1 or not file2:
            QMessageBox.critical(self, 'Error', 'Please select both Excel files.')
            return

        try:
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)
            merged_df = pd.merge(df1, df2, how=merge_type)

            save_path, _ = QFileDialog.getSaveFileName(self, 'Save Merged File', '', 'Excel Files (*.xlsx *.xls)')
            if save_path:
                merged_df.to_excel(save_path, index=False)
                QMessageBox.information(self, 'Success', 'Files merged successfully!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExcelMergerApp()
    ex.show()
    sys.exit(app.exec_())
