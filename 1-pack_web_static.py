#!/usr/bin/python3
from fabric.api import local
from datetime import datetime as t
"""
Creates a .tgz archive from the web_static folder's archives
"""


def do_pack():

    date = [
        t.now().year, t.now().month,
        t.now().day, t.now().hour,
        t.now().minute, t.now().second
    ]
    directory = "web_static"
    file_tgz = "{}_{}0{}0{}{}{}{}.tgz".format(directory,
                                            date[0], date[1],
                                            date[2], date[3],
                                            date[4], date[4],
                                            date[5])

    local("mkdir -p versions")
    path = local("tar cavf versions/{} {}".format(file_tgz, directory))

    if path.failed:
        return None
    else:
        return file_tgz
