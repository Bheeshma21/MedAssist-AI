from agents.report_parser import report_parser

from database.database_service import database
from memory.session_memory import session_memory


class FileRestoreService:

    def restore(self, session_id):

        # ----------------------------
        # Report
        # ----------------------------

        report = database.get_latest_uploaded_file(
            session_id,
            "report"
        )

        if report:

            report_text = report_parser.parse(
                report["file_path"]
            )

            session_memory.save_report(

                report["file_path"],

                report_text

            )

        # ----------------------------
        # Image
        # ----------------------------

        image = database.get_latest_uploaded_file(
            session_id,
            "image"
        )

        if image:

            session_memory.save_image(

                image["file_path"]

            )


file_restore_service = FileRestoreService()