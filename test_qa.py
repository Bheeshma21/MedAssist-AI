from services.qa_service import qa_service

result = qa_service.answer(
    "What care should women with PCOD take?"
)

print(result["answer"])
print("\nSources:")
print(result["sources"])