import os, config_manager, consts

from ftp_manager import FFTPServer


def main():
    current_directory = os.getcwd()
    json = config_manager.get_json(os.path.join(current_directory, consts.CONFIG_FILE))
    if json is None: exit(1)

    user_list : list = json.get("users_list")
    ftp_ip : str = json.get("ftp_ip")
    ftp_port : int = json.get("ftp_port")

    fftp_server = FFTPServer()
    for user in user_list:
        _user : dict = None
        if type(user) == dict: _user = user
        if _user is None: exit(1)

        fftp_server.add_user(_user.get("user_name"), _user.get("user_pass"), _user.get("user_dir"), _user.get("user_perm"))

    fftp_server.start_ftp(ftp_ip, ftp_port)


if __name__ == "__main__":
    main()