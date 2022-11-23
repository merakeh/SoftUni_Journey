
class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        if len(new_pass) < 8 or not any(s.isdigit() for s in new_pass) or \
                not any(c.isalpha() and c == c.upper() for c in new_pass):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = new_pass

    def __str__(self):
        return f"You have a profile with username: \"{self.__username}\" and password: {len(self.__password) * '*'}"



