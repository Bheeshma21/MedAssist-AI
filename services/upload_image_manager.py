import os

from memory.session_memory import session_memory
from database.database_service import database


class UploadImageManager:

    def save_image(
        self,
        uploaded_file,
        session_id=None
    ):

        upload_folder = "data/uploaded_images"

        os.makedirs(
            upload_folder,
            exist_ok=True
        )

        file_path = os.path.join(
            upload_folder,
            uploaded_file.name
        )

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        session_memory.save_image(
            file_path
        )

        if session_id:

            database.save_uploaded_file(

                session_id=session_id,

                file_type="image",

                file_name=uploaded_file.name,

                file_path=file_path

            )

        return {

            "success": True,

            "filename": uploaded_file.name,

            "path": file_path

        }


upload_image_manager = UploadImageManager()