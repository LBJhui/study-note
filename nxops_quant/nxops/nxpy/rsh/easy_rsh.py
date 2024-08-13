# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2020-10-19 13:34:59
LastEditTime : 2020-10-19 13:35:05
LastEditors  : yi.mt
Description  : 
'''
from nxpy.log.logger import LoggerUtils
import os
import stat
import paramiko

from nxpy.os.path import PathUtils

class EasyRSH():
    def __init__(self, use_sftp=True):
        self.ssh = None
        self.sftp = None

        self.use_sftp = use_sftp

    def connect(self, host, port, user, password=None):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=port, username=user, password=password)
        self.ssh = ssh
        if self.use_sftp:
            self.open_sftp()

    def connect_s(self, config):
        self.connect(config.get("host"), config.get("port", 22), config.get("user"), config.get("password", None))

    def open_sftp(self):
        if not self.sftp:
            if self.ssh:
                self.sftp = self.ssh.open_sftp()
        return self.sftp

    def disconnect(self):
        if self.ssh:
            self.ssh.close()

    def remote_path(self, path_str):
        stdin, stdout, stderr = self.execute("echo %s" % (path_str,))
        remote_path = str(stdout.read(), encoding="UTF-8")
        if remote_path is not None:
            remote_path = remote_path.replace("\n", "")
        return remote_path

    def remote_basename(self, path_str):
        stdin, stdout, stderr = self.execute("basename %s" % (path_str,))
        remote_basename = str(stdout.read(), encoding="UTF-8")
        if remote_basename is not None:
            remote_basename = remote_basename.replace("\n", "")
        return remote_basename

    def remote_dirname(self, path_str):
        stdin, stdout, stderr = self.execute("dirname %s" % (path_str,))
        remote_basename = str(stdout.read(), encoding="UTF-8")
        if remote_basename is not None:
            remote_basename = remote_basename.replace("\n", "")
        return remote_basename

    def remote_exists(self, file_path):
        try:
            self.sftp.stat(file_path)
            return True
        except:
            return False

    def execute(self, command):
        return self.ssh.exec_command(command)

    def put(self, source, target):
        try:
            if self.sftp:
                self.sftp.put(source, target)
        except Exception as e:
            LoggerUtils.error(f"[rsh put] [{source}]->[{target}] failed: [{e}]")
            raise e

    def get(self, source, target):
        try:
            if self.sftp:
                self.sftp.get(source, target)
        except Exception as e:
            LoggerUtils.error(f"[rsh get] [{source}]->[{target}] failed: [{e}]")
            raise e


def get_all_files_in_local_dir(local_dir):
    all_files = []

    files = os.listdir(local_dir)
    for file in files:
        file_path = os.path.join(local_dir, file)
        if os.path.isdir(file_path):
            all_files.extend(get_all_files_in_local_dir(file_path))
        else:
            all_files.append(file_path)
    return all_files


def get_all_files_in_remote_dir(rsh, remote_dir):
    all_files = []

    if remote_dir[-1] == '/':
        remote_dir = remote_dir[0:-1]

    sftp = rsh.open_sftp()
    if sftp:
        files = sftp.listdir_attr(remote_dir)
        for file in files:
            file_path = remote_dir + '/' + file.filename
            if stat.S_ISDIR(file.st_mode):
                all_files.extend(get_all_files_in_remote_dir(rsh, file_path))
            else:
                all_files.append(file_path)
    return all_files


class EasyRSHUtils():
    @staticmethod
    def put_dir(rsh, source_dir, target_dir, ignore_existed=False):
        real_source_dir = PathUtils.get_real_path(source_dir)
        real_target_dir = rsh.remote_path(target_dir)
        all_files = get_all_files_in_local_dir(real_source_dir)

        for source_file in all_files:
            relative_path = os.path.relpath(source_file, real_source_dir).replace("\\", "/")
            target_file = real_target_dir + "/" + relative_path
            target_file_dir = rsh.remote_dirname(target_file)

            if ignore_existed and rsh.remote_exists(target_file):
                LoggerUtils.debug(f"{target_file} existed")
            else:
                rsh.execute("mkdir -p %s" % target_file_dir)
                LoggerUtils.debug(f"rsync {source_file}->{target_file}")
                rsh.put(source_file, target_file)

    @staticmethod
    def put_file_to_dir(rsh, source_file, target_dir, target_name=None, ignore_existed=False):
        real_source_file = PathUtils.get_real_path(source_file)
        source_file_name = os.path.basename(real_source_file)
        real_target_dir = rsh.remote_path(target_dir)
        target_file_name = target_name if target_name else source_file_name
        target_file = real_target_dir + "/" + target_file_name

        if ignore_existed and rsh.remote_exists(target_file):
            LoggerUtils.debug(f"{target_file} existed")
        else:
            rsh.execute("mkdir -p %s" % real_target_dir)
            LoggerUtils.debug(f"rsync {real_source_file}->{target_file}")
            rsh.put(real_source_file, target_file)

    @staticmethod
    def put_file_to_file(rsh, source_file, target_file, ignore_existed=False):
        real_source_file = PathUtils.get_real_path(source_file)
        real_target_file = rsh.remote_path(target_file)
        real_target_dir = rsh.remote_dirname(real_target_file)

        if ignore_existed and rsh.remote_exists(real_target_file):
            LoggerUtils.debug(f"{target_file} existed")
        else:
            rsh.execute("mkdir -p %s" % real_target_dir)
            LoggerUtils.debug(f"rsync {real_source_file}->{real_target_file}")
            rsh.put(real_source_file, real_target_file)

    @staticmethod
    def get_dir(rsh, source_dir, target_dir, ignore_existed=False):
        real_source_dir = rsh.remote_path(source_dir)
        real_target_dir = PathUtils.get_real_path(target_dir)
        all_files = get_all_files_in_remote_dir(rsh, real_source_dir)

        for source_file in all_files:
            relative_path = os.path.relpath(source_file, real_source_dir).replace("\\", "/")
            target_file = real_target_dir + "/" + relative_path
            target_file_dir = os.path.dirname(target_file)

            if ignore_existed and os.path.exists(target_file):
                LoggerUtils.debug(f"{target_file} existed")
            else:
                os.makedirs(target_file_dir, exist_ok=True)
                LoggerUtils.debug(f"rsync {source_file}->{target_file}")
                rsh.get(source_file, target_file)

    @staticmethod
    def get_file_to_dir(rsh, source_file, target_dir, target_name=None, ignore_existed=False):
        real_source_file = rsh.remote_path(source_file)
        source_file_name = rsh.remote_basename(real_source_file)
        real_target_dir = PathUtils.get_real_path(target_dir)
        target_file_name = target_name if target_name else source_file_name
        target_file = real_target_dir + os.sep + target_file_name

        if ignore_existed and os.path.exists(target_file):
            LoggerUtils.debug(f"{target_file} existed")
        else:
            os.makedirs(real_target_dir, exist_ok=True)
            LoggerUtils.debug(f"rsync {real_source_file}->{target_file}")
            rsh.get(real_source_file, target_file)

    @staticmethod
    def get_file_to_file(rsh, source_file, target_file, ignore_existed=False):
        real_source_file = rsh.remote_path(source_file)
        real_target_file = PathUtils.get_real_path(target_file)
        real_target_dir = os.path.dirname(real_target_file)

        if ignore_existed and os.path.exists(real_target_file):
            LoggerUtils.debug(f"{target_file} existed")
        else:
            os.makedirs(real_target_dir, exist_ok=True)
            LoggerUtils.debug(f"rsync {real_source_file}->{real_target_file}")
            rsh.get(real_source_file, real_target_file)


if __name__ == "__main__":
    #print(get_all_files_in_local_dir("E:\\tmp"))

    rsh = EasyRSH()
    rsh.connect("10.189.65.67", 22, "trade", "trade")

    #print(rsh.parse_remote_path("${HOME}/run/tinit/csv"))

    #print(get_all_files_in_remote_dir(rsh, rsh.parse_remote_path("${HOME}/run/tinit/csv")))

    rsh.put("E:\\tmp\\policyorder", "${HOME}/temptest")
    #.get_dir(rsh, "${HOME}/temptest", "E:\\testtmp")
