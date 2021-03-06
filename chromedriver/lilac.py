#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
repo_depends = ['gconf']
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    with open('PKGBUILD', 'a') as f:
        f.write('export http_proxy=127.0.0.1:8123\n')
        f.write('export https_proxy=127.0.0.1:8123\n')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
