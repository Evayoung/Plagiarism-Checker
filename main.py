# this the entry point of the application

# this software is developed by Impath Lab Technology

# And its therefore only be Authorized under Impath-lab


import os
import sys
import threading
import time
import shutil
from difflib import SequenceMatcher

import PyPDF2
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from nltk.corpus import stopwords
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

from app_stylesheet import StyleSheet
from app_ui import Ui_MainWindow


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(StyleSheet)
        # self.setWindowIcon(QIcon("Assets/defualt/logo.png"))
        self.setWindowTitle('PLAGIARISM DETECTION')
        self.process_checker = True
        # self.des = "assets/txtfiles"
        self.finalText = ""
        self.setupUi(self)

        self.retranslateUi(self)

        self.upload_document_btn.clicked.connect(self.get_source_document)
        self.train_model_btn.clicked.connect(self.prepare_document_for_training)
        self.scan_document_btn.clicked.connect(self.call_test_model)
        self.import_target_btn.clicked.connect(self.openFileNameDialog)
        self.reset_app_btn.clicked.connect(self.reset_app)

    def get_source_document(self):
        doc_count = 0
        destination_folder = "assets/source_documents"
        try:
            source_folder = QFileDialog.getExistingDirectory(None, "Select Source Folder", os.path.expanduser("~"))
            if not source_folder:
                self.Status_update_lbl.setText(f"No file was uploaded")
                return

            for filename in os.listdir(source_folder):
                if filename.endswith(".pdf"):
                    source_path = os.path.join(source_folder, filename)
                    destination_path = os.path.join(destination_folder, filename)
                    shutil.copy(source_path, destination_path)
                    self.Status_update_lbl.setText(destination_path)
                    doc_count += 1
            self.Status_update_lbl.setText(f"{doc_count} documents uploaded successfully!")
        except Exception as e:
            print(e)



    def prepare_document_for_training(self):
        self.process_checker = True
        threading.Thread(target=self.preprocess_and_save_data_for_training, daemon=True).start()
        threading.Thread(target=self.make_process, daemon=True).start() # thread that run the operation function

    # this function is called by a separate thread to get the data from the files uploaded, clean the data by making it
    # fit for model training, it then save the treated data in another folder, so it doesn't have to do that every time
    def preprocess_and_save_data_for_training(self):
        destination_folder = "assets/source_documents"
        save_path = "assets/training_document"

        for filename in os.listdir(destination_folder):
            file = os.path.join(destination_folder, filename)
            if not filename:
                self.Status_update_lbl.setText(f"Data not available, please upload data and try again")
                return

            with open(file, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ''
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()

            stemmed_tokens = self.check_common_words(text)

            # Save the processed text to a .txt file
            filename = filename.split('.')[0] + '.txt'
            training_path = os.path.join(save_path, filename)
            with open(training_path, 'w', encoding='utf-8') as txt_file:
                words_per_line = 15  # Adjust this value as needed
                for i in range(0, len(stemmed_tokens), words_per_line):
                    txt_file.write(' '.join(stemmed_tokens[i:i + words_per_line]) + '\n')

        self.process_checker = False

    def make_process(self):
        operation_time = 0
        proces = [" \ ", " - ", " / ", " | "]
        while self.process_checker:
            for i in proces:
                time.sleep(.5)
                operation_time += 5
                self.Status_update_lbl.setText(f"Running Operation, please wait...{i}")

        self.Status_update_lbl.setText(f"Task completed successfully! time taken = {operation_time/10} seconds!")

    def openFileNameDialog(self, value):  # get document path using the gui
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Document " "Files (*.doc, *.docx)",
                                                  options=options)

        if fileName:
            self.target_document_input.setText(fileName)
            tosend2 = (fileName, value)
            threading.Thread(target=self.convert_to_txt(tosend2), daemon=True).start()
            # self.plagiarism_app_status_lbl.setText("Target file received and ready!!")

    def dovalidate(self, data):
        self.plagiarism_app_status_lbl.setText("validating file..")
        data = data.split("/")
        _name = data[-1].split(".")[0]
        print(_name)
        return _name

    def make_txt(self):
        file_path = "assets/target_document"
        for filename in os.listdir(file_path):
            file = os.path.join(file_path, filename)
            if not filename:
                self.Status_update_lbl.setText(f"Data not available, please upload data and try again")
                return

    def convert_to_txt(self, data):
        self.Status_update_lbl.setText("Converting source file..")
        name_ = self.dovalidate(data[0])

        fin_nam = "assets/target_document" + '/' + name_
        # finalText = []
        self.clear_folder()
        try:
            with open(data[0], 'rb') as infile:
                with open(fin_nam + '.txt', 'w', encoding='utf-8') as outfile:
                    doc = docx2txt.process(infile)
                    outfile.write(doc)
            self.Status_update_lbl.setText("File received and ready!!")
        except Exception as e:
            print(e)
            self.Status_update_lbl.setText("Error processing file! Please try again")
            self.target_document_input.setText("")

    def check_common_words(self, data):
        # Perform text cleaning, tokenization, and other preprocessing steps here
        text = data.lower()

        # Example: Tokenization
        tokens = text.split()

        # Example: Stopword removal (assuming 'stopwords' is a list of common stopwords)
        stopwords_set = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stopwords_set]

        # Example: Stemming or Lemmatization (using NLTK for stemming)
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word) for word in tokens]

        return stemmed_tokens


    def dovalidate(self, data):
        self.Status_update_lbl.setText("validating file..")
        data = data.split("/")
        _name = data[-1].split(".")[0]
        return _name

    def extract_text(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    def load_data_from_files(self, folder_path):
        texts = []
        # labels = []

        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                with open(os.path.join(folder_path, filename), "r", encoding='utf-8') as file:
                    text = file.read()
                    texts.append(text)
                    # labels.append(0)  # Label as plagiarized

        return texts

    def load_single_target_file(self, file_path):
        for filename in os.listdir(file_path):
            if filename.endswith(".txt"):
                with open(os.path.join(file_path, filename), "r", encoding='utf-8') as file:
                    text = file.read()
                return text

    def max_text_similarity(self, text1, texts):
        max_similarity = 0
        for text2 in texts:
            similarity = SequenceMatcher(None, text1, text2).ratio()
            max_similarity = max(max_similarity, similarity)
        return max_similarity * 100


    def clear_folder(self):
        file_path = "assets/target_document"
        try:
            for file in os.listdir(file_path):
                if file:
                    filepath = os.path.join(file_path, file)
                    os.remove(filepath)
        except Exception as e:
            print(e)

    def train_and_test_model(self):
        # Path to the folder containing training files

        training_folder = "assets/training_document"

        target_file = "assets/target_document"

        target_texts = self.load_single_target_file(target_file)

        if not target_texts:
            self.Status_update_lbl.setText("Error! source documents not ready")
            return

        # Load and preprocess training data
        training_texts = self.load_data_from_files(training_folder)
        if not training_texts:
            self.Status_update_lbl.setText("Error! Target document not ready")
            return

        if not self.process_checker:
            self.process_checker = True


# Calculate the maximum similarity between the target text and training texts
        max_similarity = self.max_text_similarity(target_texts, training_texts)

        # Set a plagiarism threshold percentage
        plagiarism_threshold = 10  # Adjust as needed

        # Check if the maximum similarity is above the threshold
        is_plagiarized = max_similarity >= plagiarism_threshold

        # Show the maximum similarity and the result
        self.plagiarism_ouput_lbl.setText(f"{max_similarity:.2f}%")
        self.plag_allowed_output.setText(f"{plagiarism_threshold}")
        self.doc_scan_lbl.setText("Yes" if is_plagiarized else "No")
        self.process_checker = False




    def reset_app(self):
        directories = ["assets/target_document", "assets/training_document"]
        for i in directories:
            for file in os.listdir(i):
                if file:
                    filepath = os.path.join(i, file)
                    os.remove(filepath)

        self.plagiarism_ouput_lbl.setText("")
        self.plag_allowed_output.setText("")
        self.doc_scan_lbl.setText("")
        self.target_document_input.setText("")
        self.Status_update_lbl.setText("Application data has been reset.")

    def call_test_model(self):
        self.process_checker = True
        self.plagiarism_ouput_lbl.setText("")
        self.plag_allowed_output.setText("")
        self.doc_scan_lbl.setText("")
        threading.Thread(target=self.train_and_test_model, daemon=True).start()
        threading.Thread(target=self.make_process, daemon=True).start()

    def make_utility_folders(self):
        folders = ["assets", "assets/source_documents", "assets/target_document", "assets/training_document"]
        for i in folders:
            if not os.path.exists(i):
                os.mkdir(i)


def main():
    app = QApplication(sys.argv)
    w = Main_Window()
    w.show()
    w.make_utility_folders()
    # w.reset_data()
    w.clear_folder()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


"""
import textract

def textract_text_from_file(file_path):
    text = textract.process(file_path)
    return text.decode()
"""

"""
import docx2txt
import glob

directory = glob.glob('C:/folder_name/*.docx')

for file_name in directory:
    with open(file_name, 'rb') as infile:
        with open(file_name[:-5]+'.txt', 'w', encoding='utf-8') as outfile:
            doc = docx2txt.process(infile)
            outfile.write(doc)

print("=========")
print("All done!")
"""

"""
self.Status_update_lbl.setText("Converting source file..")
name_ = self.dovalidate(data[0])

fin_nam = "assets/target_document" + '/' + name_
# finalText = []
self.clear_folder()
try:
    # get document and convert to .txt format for similarity test
    text = textract.process(data[0])
    with open(f"{fin_nam}.txt", 'wb') as txt_file:
        txt_file.write(text)
    self.Status_update_lbl.setText("File received and ready!!")
except Exception as e:
    print(e)
    self.Status_update_lbl.setText("Error processing file! Please try again")
    self.target_document_input.setText("")
"""
