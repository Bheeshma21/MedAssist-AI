import os
import json

from agents.dashboard_agent import dashboard_agent
from agents.report_parser import report_parser

from database.database_service import database
from database.health_timeline import health_timeline
from memory.session_memory import session_memory


class UploadManager:

    def save_report(
        self,
        uploaded_file,
        user_id,
        session_id=None
    ):

        upload_folder = "data/uploaded_reports"

        os.makedirs(
            upload_folder,
            exist_ok=True
        )

        file_path = os.path.join(
            upload_folder,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:

            f.write(
                uploaded_file.getbuffer()
            )

        # ---------------------------------------
        # Parse Report
        # ---------------------------------------

        report_text = report_parser.parse(
            file_path
        )

        # ---------------------------------------
        # Generate Dashboard
        # ---------------------------------------

        dashboard = dashboard_agent.generate(
            report_text
        )

        if not isinstance(dashboard, dict):
            dashboard = {
                "report_type": "Unknown",
                "patient": {},
                "health_score": 0,
                "risk_level": "Unknown",
                "summary": str(dashboard),
                "body_systems": [],
                "tests": [],
                "possible_conditions": [],
                "recommendations": [],
                "action_plan": []
            }

        # ---------------------------------------
        # Save Report Metadata to Database
        # ---------------------------------------

        if session_id:
            database.save_uploaded_file(
                session_id=session_id,
                file_type="report",
                file_name=uploaded_file.name,
                file_path=file_path
            )

        # ---------------------------------------
        # Save Dashboard to Timeline
        # ---------------------------------------

        if hasattr(health_timeline, "save_report"):
            health_timeline.save_report(

                user_id=user_id,

                report_name=uploaded_file.name,

                report_type=dashboard.get(
                    "report_type",
                    "Unknown"
                ),

                health_score=dashboard.get(
                    "health_score",
                    0
                ),

                risk_level=dashboard.get(
                    "risk_level",
                    "Unknown"
                ),

                dashboard_json=json.dumps(
                    dashboard
                )

            )

        # ---------------------------------------
        # Save Session Memory
        # ---------------------------------------

        session_memory.clear_dashboard()

        session_memory.save_dashboard(
            dashboard
        )

        session_memory.save_report(
            file_path,
            report_text
        )

        # ---------------------------------------
        # Return
        # ---------------------------------------

        return {

            "success": True,

            "file_path": file_path,

            "filename": uploaded_file.name,

            "dashboard": dashboard

        }


upload_manager = UploadManager()