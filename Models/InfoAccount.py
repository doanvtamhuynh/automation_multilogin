class NewInfo:
    def __init__(self, password, recovery, ten, ho, homeAddress, workAddress):
        self._password = password
        self._recovery = recovery
        self._ten = ten
        self._ho = ho
        self._homeAddress = homeAddress
        self._workAddress = workAddress

    @property
    def password(self):
        return self._password

    @property
    def recovery(self):
        return self._recovery

    @property
    def ten(self):
        return self._ten

    @property
    def ho(self):
        return self._ho

    @property
    def homeAddress(self):
        return self._homeAddress

    @property
    def workAddress(self):
        return self._workAddress

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @recovery.setter
    def recovery(self, new_recovery):
        self._recovery = new_recovery

    @ten.setter
    def ten(self, new_ten):
        self._ten = new_ten

    @ho.setter
    def ho(self, new_ho):
        self._ho = new_ho

    @homeAddress.setter
    def homeAddress(self, new_homeAddress):
        self._homeAddress = new_homeAddress

    @workAddress.setter
    def workAddress(self, new_workAddress):
        self._workAddress = new_workAddress

    def __str__(self):
        return f"[INFO] Info Account Password: {self._password}, Recovery Email: {self._recovery}, Ten: {self._ten}, Ho: {self._ho}, Address: {self._homeAddress}/{self._workAddress}"