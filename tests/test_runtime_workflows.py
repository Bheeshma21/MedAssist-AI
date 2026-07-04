import sys
import types
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.database_service import database
import services.upload_manager as upload_manager_module


def test_database_supports_credit_updates():
    assert hasattr(database, "update_credits")


def test_database_supports_latest_uploaded_file_lookup():
    assert hasattr(database, "get_latest_uploaded_file")


def test_upload_manager_persists_report_to_database(tmp_path, monkeypatch):
    class FakeUploadFile:
        name = "report.pdf"

        def getbuffer(self):
            return b"%PDF-1.4"

    saved = {}

    class FakeDatabase:
        def save_uploaded_file(self, session_id, file_type, file_name, file_path):
            saved["session_id"] = session_id
            saved["file_type"] = file_type
            saved["file_name"] = file_name
            saved["file_path"] = file_path

    monkeypatch.setattr(upload_manager_module, "database", FakeDatabase())
    monkeypatch.setattr(
        upload_manager_module,
        "report_parser",
        types.SimpleNamespace(parse=lambda path: "report text"),
    )
    monkeypatch.setattr(
        upload_manager_module,
        "dashboard_agent",
        types.SimpleNamespace(
            generate=lambda report_text: {
                "report_type": "Lab",
                "patient": {},
                "health_score": 70,
                "risk_level": "Moderate",
                "summary": "ok",
                "body_systems": [],
                "tests": [],
                "possible_conditions": [],
                "recommendations": [],
                "action_plan": [],
            }
        ),
    )
    monkeypatch.setattr(
        upload_manager_module,
        "health_timeline",
        types.SimpleNamespace(save_report=lambda **kwargs: None),
    )
    monkeypatch.setattr(upload_manager_module.session_memory, "clear_dashboard", lambda: None)
    monkeypatch.setattr(upload_manager_module.session_memory, "save_dashboard", lambda dashboard: None)
    monkeypatch.setattr(upload_manager_module.session_memory, "save_report", lambda file_path, report_text: None)

    monkeypatch.chdir(tmp_path)

    upload_manager_module.upload_manager.save_report(
        FakeUploadFile(),
        user_id=1,
        session_id=7,
    )

    assert saved["session_id"] == 7
    assert saved["file_type"] == "report"
    assert saved["file_name"] == "report.pdf"
    assert saved["file_path"].endswith("report.pdf")
