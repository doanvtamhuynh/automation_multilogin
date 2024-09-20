class NewProfile:
    def __init__(self, profileID, folderID):
        self._profileID = profileID
        self._folderID = folderID

    @property
    def profileID(self):
        return self._profileID

    @property
    def folderID(self):
        return  self._folderID

    @profileID.setter
    def profileID(self, new_profileID):
        self._profileID = new_profileID

    @folderID.setter
    def folderID(self, new_folderID):
        self._folderID = new_folderID

    def __str__(self):
        return f"[INFO] Profile_ID: {self._profileID}, Folder_ID: {self._folderID}"