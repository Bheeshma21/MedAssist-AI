from agents.report_parser import report_parser

file_path = r"C:\Users\vinnu\Downloads\CBC-sample-report-with-notes_0.pdf"   # Change this if your PDF is elsewhere

text = report_parser.parse(file_path)

print("=" * 80)
print("EXTRACTED TEXT")
print("=" * 80)
print(text[:3000])  # Print first 3000 characters