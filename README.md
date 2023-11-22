# Plagiarism-Checker
This is a plagiarism checker using Bayes theory, the aim of the project is to design a simple system that leverage on the similarity test
of the Baye's theorem to implement a system that compare documents.

# Quick Overview
The app is built with a very basic user interface with a button to upload all source documents
once the the source documents are uploaded, there is another button to clean the document, convert it to
a .txt file and remove all common words and save the each document in a training folder.

The target document can now be uploaded, processed cleaned at the same time and prepared for testing.
there is a scan button that can be used to initiate the similarity test process, the similarity percent
will be shown with a 10 % thresh hold.

# Requirements
The user interface is designed using PyQt5, a python framework
Frameworks like NLTK, SCIKIT-LEARN, PyPdf, docx2txt, were used for the model.

# License
MIT License

