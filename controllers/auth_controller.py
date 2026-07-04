from auth.auth_service import auth_service


class AuthController:

    def register(
        self,
        name,
        email,
        password,
        confirm_password,
        role
    ):

        if password != confirm_password:

            return False, "Passwords do not match."

        return auth_service.register(
            name,
            email,
            password,
            role
        )

    def login(
        self,
        email,
        password
    ):

        return auth_service.login(
            email,
            password
        )


auth_controller = AuthController()