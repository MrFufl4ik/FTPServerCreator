from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

class FFTPServer:
    def __init__(self):
        self._ftp_users : list = []

    def start_ftp(self, ip : str, port : int):
        authorizer = DummyAuthorizer()
        for user in self._ftp_users:
            _user : dict = None
            if type(user) == dict: _user = user
            if _user is None: exit(1)

            authorizer.add_user(_user.get("user_name"), _user.get("user_pass"), _user.get("user_dir"), perm=_user.get("user_perm"))

        handler = FTPHandler
        handler.authorizer = authorizer

        address = (ip, port)
        server = FTPServer(address, handler)
        server.serve_forever()

    def add_user(self, user_name: str, user_pass : str, user_dir : str, user_perm: str):
        self._ftp_users.append({
            "user_name" : user_name,
            "user_pass" : user_pass,
            "user_dir"  : user_dir,
            "user_perm" : user_perm,
        })
