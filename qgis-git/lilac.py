#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}, {'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}, {'github': 'qgis/QGIS'}]
build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build
time_limit_hours = 5

if __name__ == '__main__':
    single_main(build_prefix)
