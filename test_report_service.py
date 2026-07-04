from services.report_service import report_service

result = report_service.analyze(
    r"C:\Users\vinnu\Downloads\CBC-sample-report-with-notes_0.pdf"
)

print("=" * 80)
print("AI REPORT ANALYSIS")
print("=" * 80)

print(result["analysis"])