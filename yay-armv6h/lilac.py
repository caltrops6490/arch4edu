#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': 'yay'}]
build_prefix = 'action-extra-armv6h'
time_limit_hours = 3

def pre_build():
    aur_pre_build('yay')

post_build = aur_post_build

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
