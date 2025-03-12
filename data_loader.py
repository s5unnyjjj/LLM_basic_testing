
import fitz
import os

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def run(self, files):
        text = ''
        for file in files:
            if file.endswith('pdf'):
                text += self.load_pdf(file)
        return text

    def load_pdf(self, file):
        doc = fitz.open(os.path.join(self.file_path, file))
        text = ''
        for page in doc:
            text += page.get_text()
        return text

