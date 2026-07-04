from database.database_service import database


class AuthService:

    def register(
        self,
        name,
        email,
        password,
        role
    ):

        user = database.get_user(email)

        if user:

            return False, "Email already registered."

        success = database.create_user(
            name,
            email,
            password,
            role
        )

        if success:

            user = database.get_user(email)

            database.update_credits(
                user["id"],
                20
            )

            return True, "Registration Successful."

        return False, "Registration Failed."

    def login(
        self,
        email,
        password
    ):

        user = database.login(
            email,
            password
        )

        if user:

            return True, user

        return False, "Invalid email or password."


auth_service = AuthService()