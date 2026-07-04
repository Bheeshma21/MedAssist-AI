from backend.ai_service import ai_service

response = ai_service.generate(
    "Explain PCOD in simple language."
)

print(response)