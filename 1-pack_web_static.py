#!/usr/bin/python3
"""
Module for setting up webservers
usigng Fabric module
"""
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    """
    packs contents of webstatic using '.tgz'
    """
    formatted_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(formatted_dt)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None
