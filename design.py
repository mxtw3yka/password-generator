# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(685, 498)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/password_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: #121212;\n"
"	color: white;\n"
"	margin: 16px;\n"
"	font-size: 10pt;\n"
"	font-family: Ubuntu;\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid gray;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#btn_lower, #btn_upper, #btn_digits, #btn_special {\n"
"	padding: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: #090;\n"
"}\n"
"QPushButon:pressed {\n"
"	border: 4px solid #090;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton#icon_lock {\n"
"	border: none;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #006300;\n"
"	border-color: #090;\n"
"}\n"
"QFrame {\n"
"	border: 2px solid grey;\n"
"	border-radius: 10px;\n"
"}\n"
"QFrame:hover {\n"
"	border-color: #090;\n"
"}\n"
"QLineEdit {\n"
"	border: none;\n"
"	margin: 0;\n"
"	font-size: 20pt;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon_lock = QPushButton(self.centralwidget)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/lock_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.icon_lock.setIcon(icon1)
        self.icon_lock.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.icon_lock)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.frame_password = QFrame(self.centralwidget)
        self.frame_password.setObjectName(u"frame_password")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy)
        self.frame_password.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_password)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_password = QLineEdit(self.frame_password)
        self.line_password.setObjectName(u"line_password")

        self.horizontalLayout_3.addWidget(self.line_password)

        self.btn_visibility = QPushButton(self.frame_password)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	margin: 0;\n"
"	background-color: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/visibility_off_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/icons/visibility_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_visibility.setIcon(icon2)
        self.btn_visibility.setIconSize(QSize(30, 30))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_visibility)

        self.btn_copy = QPushButton(self.frame_password)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	margin: 0;\n"
"	background-color: transparent;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/content_copy_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_copy.setIcon(icon3)
        self.btn_copy.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_copy)

        self.btn_refresh = QPushButton(self.frame_password)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	margin: 0;\n"
"	background-color: transparent;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/refresh_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_refresh.setIcon(icon4)
        self.btn_refresh.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_refresh)


        self.layout_password.addWidget(self.frame_password)


        self.verticalLayout.addLayout(self.layout_password)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_strength = QLabel(self.centralwidget)
        self.label_strength.setObjectName(u"label_strength")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_strength.sizePolicy().hasHeightForWidth())
        self.label_strength.setSizePolicy(sizePolicy1)
        self.label_strength.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_strength.setStyleSheet(u"border: none;")
        self.label_strength.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_strength)

        self.label_entropy = QLabel(self.centralwidget)
        self.label_entropy.setObjectName(u"label_entropy")
        sizePolicy1.setHeightForWidth(self.label_entropy.sizePolicy().hasHeightForWidth())
        self.label_entropy.setSizePolicy(sizePolicy1)
        self.label_entropy.setStyleSheet(u"border: none;")
        self.label_entropy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_entropy)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.layout_bar = QHBoxLayout()
        self.layout_bar.setObjectName(u"layout_bar")
        self.slider_length = QSlider(self.centralwidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slider_length.setMouseTracking(True)
        self.slider_length.setTabletTracking(True)
        self.slider_length.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"    border: 1px solid grey;\n"
"    width: 18px;\n"
"    margin: -2px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #090;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background-color: grey;\n"
"    border-radius: 4px;\n"
"}")
        self.slider_length.setMaximum(100)
        self.slider_length.setValue(12)
        self.slider_length.setOrientation(Qt.Orientation.Horizontal)

        self.layout_bar.addWidget(self.slider_length)

        self.box_length = QSpinBox(self.centralwidget)
        self.box_length.setObjectName(u"box_length")
        self.box_length.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.box_length.setStyleSheet(u"QSpinBox {\n"
"	border: 2px solid gray;\n"
"	border-radius:  5px;\n"
"	background: transparent;\n"
"	padding: 2px;\n"
"}\n"
"QSpinBox:hover {\n"
"	border-color: #009900;\n"
"}\n"
"	")
        self.box_length.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.box_length.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.box_length.setMaximum(100)
        self.box_length.setValue(12)

        self.layout_bar.addWidget(self.box_length)


        self.verticalLayout.addLayout(self.layout_bar)

        self.layout_char = QHBoxLayout()
        self.layout_char.setObjectName(u"layout_char")
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_char.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_char.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_char.addWidget(self.btn_digits)

        self.btn_special = QPushButton(self.centralwidget)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_special.setCheckable(True)
        self.btn_special.setChecked(True)

        self.layout_char.addWidget(self.btn_special)


        self.verticalLayout.addLayout(self.layout_char)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.icon_lock.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.icon_lock.setText("")
        self.btn_visibility.setText("")
        self.btn_copy.setText("")
#if QT_CONFIG(shortcut)
        self.btn_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.btn_refresh.setText("")
#if QT_CONFIG(shortcut)
        self.btn_refresh.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.label_strength.setText("")
        self.label_entropy.setText("")
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"#$%", None))
    # retranslateUi

