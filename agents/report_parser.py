import os
from pypdf import PdfReader


class ReportParser:

    def parse(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return self._parse_pdf(file_path)

        elif extension == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()

        else:
            raise ValueError("Unsupported file type.")

    def _parse_pdf(self, file_path):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text


report_parser = ReportParser()