from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                          QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                         QFont, QFontDatabase, QGradient, QIcon,
                         QImage, QKeySequence, QLinearGradient, QPainter,
                         QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 590)
        MainWindow.setMaximumSize(QSize(900, 590))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget_layout = QVBoxLayout(self.centralwidget)
        self.centralwidget_layout.setObjectName(u"centralwidget_layout")
        self.app_header_frame = QFrame(self.centralwidget)
        self.app_header_frame.setObjectName(u"app_header_frame")
        self.app_header_frame.setMinimumSize(QSize(0, 150))
        self.app_header_frame.setMaximumSize(QSize(16777215, 150))
        self.app_header_frame.setFrameShape(QFrame.StyledPanel)
        self.app_header_frame.setFrameShadow(QFrame.Raised)
        self.app_header_frame_layout = QVBoxLayout(self.app_header_frame)
        self.app_header_frame_layout.setSpacing(3)
        self.app_header_frame_layout.setObjectName(u"app_header_frame_layout")
        self.app_header_frame_layout.setContentsMargins(-1, 10, -1, 10)
        self.app_logo_lbl = QLabel(self.app_header_frame)
        self.app_logo_lbl.setObjectName(u"app_logo_lbl")
        self.app_logo_lbl.setMinimumSize(QSize(60, 60))
        self.app_logo_lbl.setMaximumSize(QSize(60, 60))

        self.app_header_frame_layout.addWidget(self.app_logo_lbl, 0, Qt.AlignHCenter)

        self.project_title_lbl = QLabel(self.app_header_frame)
        self.project_title_lbl.setObjectName(u"project_title_lbl")
        font = QFont()
        font.setFamilies([u"Poppins ExtraBold"])
        font.setPointSize(17)
        self.project_title_lbl.setFont(font)

        self.app_header_frame_layout.addWidget(self.project_title_lbl, 0, Qt.AlignHCenter)

        self.case_study_lbl = QLabel(self.app_header_frame)
        self.case_study_lbl.setObjectName(u"case_study_lbl")
        font1 = QFont()
        font1.setFamilies([u"Poppins Light"])
        font1.setPointSize(10)
        self.case_study_lbl.setFont(font1)

        self.app_header_frame_layout.addWidget(self.case_study_lbl, 0, Qt.AlignHCenter)

        self.centralwidget_layout.addWidget(self.app_header_frame)

        self.app_central_frame = QFrame(self.centralwidget)
        self.app_central_frame.setObjectName(u"app_central_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_central_frame.sizePolicy().hasHeightForWidth())
        self.app_central_frame.setSizePolicy(sizePolicy)
        self.app_central_frame.setFrameShape(QFrame.StyledPanel)
        self.app_central_frame.setFrameShadow(QFrame.Raised)
        self.app_central_frame_layout = QVBoxLayout(self.app_central_frame)
        self.app_central_frame_layout.setObjectName(u"app_central_frame_layout")
        self.app_central_frame_layout.setContentsMargins(-1, 20, -1, -1)
        self.document_entry_frame = QFrame(self.app_central_frame)
        self.document_entry_frame.setObjectName(u"document_entry_frame")
        self.document_entry_frame.setMinimumSize(QSize(0, 130))
        self.document_entry_frame.setFrameShape(QFrame.StyledPanel)
        self.document_entry_frame.setFrameShadow(QFrame.Raised)
        self.document_entry_frame_layout = QVBoxLayout(self.document_entry_frame)
        self.document_entry_frame_layout.setSpacing(5)
        self.document_entry_frame_layout.setObjectName(u"document_entry_frame_layout")
        self.document_entry_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.upload_train_frame = QFrame(self.document_entry_frame)
        self.upload_train_frame.setObjectName(u"upload_train_frame")
        self.upload_train_frame.setMinimumSize(QSize(0, 60))
        self.upload_train_frame_layout = QHBoxLayout(self.upload_train_frame)
        self.upload_train_frame_layout.setSpacing(2)
        self.upload_train_frame_layout.setObjectName(u"upload_train_frame_layout")
        self.upload_train_frame_layout.setContentsMargins(-1, -1, -1, 15)
        self.upload_document_btn = QPushButton(self.upload_train_frame)
        self.upload_document_btn.setObjectName(u"upload_document_btn")
        self.upload_document_btn.setMinimumSize(QSize(150, 35))
        self.upload_document_btn.setMaximumSize(QSize(150, 35))

        self.upload_train_frame_layout.addWidget(self.upload_document_btn)

        self.train_model_btn = QPushButton(self.upload_train_frame)
        self.train_model_btn.setObjectName(u"train_model_btn")
        self.train_model_btn.setMinimumSize(QSize(150, 35))
        self.train_model_btn.setMaximumSize(QSize(150, 35))

        self.upload_train_frame_layout.addWidget(self.train_model_btn)

        self.document_entry_frame_layout.addWidget(self.upload_train_frame)

        self.target_doc_lbl = QLabel(self.document_entry_frame)
        self.target_doc_lbl.setObjectName(u"target_doc_lbl")

        self.document_entry_frame_layout.addWidget(self.target_doc_lbl)

        self.target_entry = QFrame(self.document_entry_frame)
        self.target_entry.setObjectName(u"target_entry")
        self.target_entry_layout = QHBoxLayout(self.target_entry)
        self.target_entry_layout.setSpacing(2)
        self.target_entry_layout.setObjectName(u"target_entry_layout")
        self.target_document_input = QLineEdit(self.target_entry)
        self.target_document_input.setObjectName(u"target_document_input")
        self.target_document_input.setMinimumSize(QSize(600, 35))
        self.target_document_input.setMaximumSize(QSize(600, 35))

        self.target_entry_layout.addWidget(self.target_document_input)

        self.import_target_btn = QPushButton(self.target_entry)
        self.import_target_btn.setObjectName(u"import_target_btn")
        self.import_target_btn.setMinimumSize(QSize(25, 35))
        self.import_target_btn.setMaximumSize(QSize(25, 35))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.import_target_btn.setFont(font2)

        self.target_entry_layout.addWidget(self.import_target_btn)

        self.document_entry_frame_layout.addWidget(self.target_entry)

        self.app_central_frame_layout.addWidget(self.document_entry_frame, 0, Qt.AlignHCenter)

        self.statut_report_box = QGroupBox(self.app_central_frame)
        self.statut_report_box.setObjectName(u"statut_report_box")
        self.statut_report_box.setMinimumSize(QSize(0, 110))
        self.statut_report_box.setFont(font2)
        self.statut_report_box_layout = QGridLayout(self.statut_report_box)
        self.statut_report_box_layout.setObjectName(u"statut_report_box_layout")
        self.minimum_plag_tag = QLabel(self.statut_report_box)
        self.minimum_plag_tag.setObjectName(u"minimum_plag_tag")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        self.minimum_plag_tag.setFont(font3)

        self.statut_report_box_layout.addWidget(self.minimum_plag_tag, 0, 0, 1, 1, Qt.AlignRight)

        self.plag_allowed_output = QLabel(self.statut_report_box)
        self.plag_allowed_output.setObjectName(u"plag_allowed_output")
        self.plag_allowed_output.setFont(font2)

        self.statut_report_box_layout.addWidget(self.plag_allowed_output, 0, 1, 1, 1)

        self.plagiarism_tag = QLabel(self.statut_report_box)
        self.plagiarism_tag.setObjectName(u"plagiarism_tag")
        self.plagiarism_tag.setFont(font3)

        self.statut_report_box_layout.addWidget(self.plagiarism_tag, 1, 0, 1, 1, Qt.AlignRight)

        self.plagiarism_ouput_lbl = QLabel(self.statut_report_box)
        self.plagiarism_ouput_lbl.setObjectName(u"plagiarism_ouput_lbl")
        self.plagiarism_ouput_lbl.setFont(font2)

        self.statut_report_box_layout.addWidget(self.plagiarism_ouput_lbl, 1, 1, 1, 1)

        self.doc_scan_tag = QLabel(self.statut_report_box)
        self.doc_scan_tag.setObjectName(u"doc_scan_tag")
        self.doc_scan_tag.setFont(font3)

        self.statut_report_box_layout.addWidget(self.doc_scan_tag, 2, 0, 1, 1, Qt.AlignRight)

        self.doc_scan_lbl = QLabel(self.statut_report_box)
        self.doc_scan_lbl.setObjectName(u"doc_scan_lbl")
        self.doc_scan_lbl.setFont(font2)

        self.statut_report_box_layout.addWidget(self.doc_scan_lbl, 2, 1, 1, 1)

        self.app_central_frame_layout.addWidget(self.statut_report_box)

        self.nave_btn_frame = QFrame(self.app_central_frame)
        self.nave_btn_frame.setObjectName(u"nave_btn_frame")
        self.nave_btn_frame_layout = QHBoxLayout(self.nave_btn_frame)
        self.nave_btn_frame_layout.setObjectName(u"nave_btn_frame_layout")
        self.status_update_tag = QLabel(self.nave_btn_frame)
        self.status_update_tag.setObjectName(u"status_update_tag")
        self.status_update_tag.setMaximumSize(QSize(50, 16777215))
        self.status_update_tag.setFont(font2)

        self.nave_btn_frame_layout.addWidget(self.status_update_tag)

        self.Status_update_lbl = QLabel(self.nave_btn_frame)
        self.Status_update_lbl.setObjectName(u"Status_update_lbl")

        self.nave_btn_frame_layout.addWidget(self.Status_update_lbl)

        self.reset_app_btn = QPushButton(self.nave_btn_frame)
        self.reset_app_btn.setObjectName(u"reset_app_btn")
        self.reset_app_btn.setMinimumSize(QSize(80, 35))
        self.reset_app_btn.setMaximumSize(QSize(100, 35))
        font4 = QFont()
        font4.setBold(True)
        self.reset_app_btn.setFont(font4)

        self.nave_btn_frame_layout.addWidget(self.reset_app_btn)

        self.scan_document_btn = QPushButton(self.nave_btn_frame)
        self.scan_document_btn.setObjectName(u"scan_document_btn")
        self.scan_document_btn.setMinimumSize(QSize(0, 35))
        self.scan_document_btn.setMaximumSize(QSize(100, 35))
        self.scan_document_btn.setFont(font4)

        self.nave_btn_frame_layout.addWidget(self.scan_document_btn)

        self.app_central_frame_layout.addWidget(self.nave_btn_frame)

        self.centralwidget_layout.addWidget(self.app_central_frame)

        self.app_footer_frame = QFrame(self.centralwidget)
        self.app_footer_frame.setObjectName(u"app_footer_frame")
        self.app_footer_frame.setEnabled(True)
        self.app_footer_frame.setMinimumSize(QSize(0, 40))
        self.app_footer_frame.setMaximumSize(QSize(16777215, 40))
        self.app_footer_frame.setFrameShape(QFrame.StyledPanel)
        self.app_footer_frame.setFrameShadow(QFrame.Raised)
        self.app_footer_frame_layout = QHBoxLayout(self.app_footer_frame)
        self.app_footer_frame_layout.setSpacing(0)
        self.app_footer_frame_layout.setObjectName(u"app_footer_frame_layout")
        self.app_footer_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.project_owner_lbl = QLabel(self.app_footer_frame)
        self.project_owner_lbl.setObjectName(u"project_owner_lbl")

        self.app_footer_frame_layout.addWidget(self.project_owner_lbl, 0, Qt.AlignHCenter)

        self.centralwidget_layout.addWidget(self.app_footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)


        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_logo_lbl.setText("")
        self.project_title_lbl.setText(
            QCoreApplication.translate("MainWindow", u"Plagiarism Detection In Documents", None))
        self.case_study_lbl.setText(
            QCoreApplication.translate("MainWindow", u"(Case Study of Computer Science PGD)", None))
        self.upload_document_btn.setText(QCoreApplication.translate("MainWindow", u"Upload Documents", None))
        self.train_model_btn.setText(QCoreApplication.translate("MainWindow", u"Train Model", None))
        self.target_doc_lbl.setText(QCoreApplication.translate("MainWindow", u"Import The Target File :", None))
        self.import_target_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.statut_report_box.setTitle(QCoreApplication.translate("MainWindow", u"Status Report", None))
        self.minimum_plag_tag.setText(QCoreApplication.translate("MainWindow", u"Plagiarism Threshold :", None))
        self.plag_allowed_output.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plagiarism_tag.setText(QCoreApplication.translate("MainWindow", u"Plagiarism Score:", None))
        self.plagiarism_ouput_lbl.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.doc_scan_tag.setText(QCoreApplication.translate("MainWindow", u"Plagiarism Detected :", None))
        self.doc_scan_lbl.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.status_update_tag.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.Status_update_lbl.setText(QCoreApplication.translate("MainWindow", u"Done!", None))
        self.reset_app_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.scan_document_btn.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.project_owner_lbl.setText(QCoreApplication.translate("MainWindow", u"Powered By: Owusu Julius", None))
    # retranslateUi

