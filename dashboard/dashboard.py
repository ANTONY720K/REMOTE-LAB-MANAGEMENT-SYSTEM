import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lab Management Dashboard')
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel('Welcome to the Lab Management Dashboard')
        layout.addWidget(label)

        button = QPushButton('Manage Lab PCs')
        button.clicked.connect(self.manage_lab_pcs)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def manage_lab_pcs(self):
        # Functionality to manage lab PCs will be implemented here
        print('Manage Lab PCs clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())