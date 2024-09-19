class NewEmail:
    def __init__(self, email, password, recovery):
        self._email = email
        self._password = password
        self._recovery = recovery

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def recovery(self):
        return self._recovery

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @recovery.setter
    def recovery(self, new_recovery):
        self._recovery = new_recovery

    def __str__(self):
        return f"[INFO] Email: {self._email}, Password: {self._password}, Recovery Email: {self._recovery}"