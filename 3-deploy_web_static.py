#!/usr/bin/python3
"""
Module for setting up webservers
usigng Fabric module
"""
import os
from fabric.api import local, task, put, env, run
from datetime import datetime


env.hosts = ['54.158.183.6', '54.237.54.173']
env.user = 'ubuntu'


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


@task
def do_deploy(archive_path):
    """
    distributes an archive to web servers
    """
    if os.path.exists(archive_path):
        put(archive_path, "/tmp/")
        path_date = archive_path.split("_")[-1].split(".")[0]
        run(f"mkdir -p /data/web_static/releases/web_static_{path_date}")
        run(
            f"tar -xzf /tmp/web_static_{path_date}.tgz -C \
            /data/web_static/releases/web_static_{path_date}/")
        run(f"rm -rf /tmp/web_static_{path_date}.tgz")
        run(
            f"mv \
            /data/web_static/releases/web_static_{path_date}/web_static/* \
            /data/web_static/releases/web_static_{path_date}/"
        )
        run(
            f"rm -rf \
            /data/web_static/releases/web_static_{path_date}/web_static"
        )
        run("rm -rf /data/web_static/current")
        run(
            f"ln -s /data/web_static/releases/web_static_{path_date}/ \
            /data/web_static/current")
        return True
    else:
        return False


@task
def deploy():
    """
    creates and distributes an archive to your web servers
    using the function deploy
    """
    result_path = do_pack()
    if result_path:
        deploy_res = do_deploy(result_path)
        return deploy_res
    else:
        return False
