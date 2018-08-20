#!/usr/bin/env python

import os
import re
import shutil
import sys


def convert_name(filename):
    # centos名称模板
    centos_template = 'centos\g<version>'
    # 匹配名为rhel，RedHat等类似字符串
    rhelsearch = re.compile('(?:rhel|red.*?hat)(?P<version>\s*\d+.\d+|\s*\d+)', flags=re.I)
    rhelname = rhelsearch.search(filename)
    if rhelname:
        centos_name = rhelname.expand(centos_template)
    else:
        centos_name = None
    return centos_name

def get_all_dirname(path):
    dir_list = [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]
    print('\033[1;32m' + 'find dir list:','\n', '\033[0m', dir_list)
    return dir_list

def do(path):
    rheldir_list = [dirname for dirname in get_all_dirname(path) if convert_name(dirname)]
    print('\033[1;32m' + 'find rhel dir:', '\n', '\033[0m', rheldir_list)
    print('\033[1;32mStart copy:\033[0m')
    for name in rheldir_list:
        try:
            shutil.copytree(os.path.join(path,name), os.path.join(path, convert_name(name)))
        except FileExistsError as e:
            print('\033[1;31m', 'file exists:{oldname}===>{newname}'.format(oldname=os.path.join(path, name), newname=os.path.join(path, convert_name(name))), '\033[0m')
            continue
        print('\033[1;32m', 'copy {oldname} to {newname}.'.format(oldname=os.path.join(path, name), newname=os.path.join(path, convert_name(name))), '\033[0m')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\033[1;33mplease input directory name\033[0m')
        sys.exit(1)
    do(sys.argv[1])
