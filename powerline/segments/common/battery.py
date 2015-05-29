# vim:fileencoding=utf-8
"""Powerline disk segments."""
from __future__ import (
    unicode_literals, division, absolute_import, print_function)

import re

from powerline.lib.shell import run_cmd


BATTERY_AC_POWER = re.compile(r'\b(AC Power)\b')
BATTERY_CHARGING = re.compile(r'\b(charging)\b')
BATTERY_PERCENT = re.compile(r'(\d+)%')
BATTERY_TIME = re.compile(r'(\d*:\d*) remaining')
BATTERY_STATUS = re.compile(r'Battery Warning: \b(\w+)\b')


def battery(pl):
    """Return the battery segment."""
    stats = run_cmd(pl, ['pmset', '-g', 'batt'])
    plugged_in = bool(BATTERY_AC_POWER.search(stats))
    charging = bool(BATTERY_CHARGING.search(stats))
    percent = int(BATTERY_PERCENT.search(stats).group(1))
    warning = BATTERY_STATUS.search(stats)
    try:
        remaining = BATTERY_TIME.search(stats).group(1)
    except:
        remaining = 'no estimate'
    remaining
    ret = []
    fmt = '{value}%'
    if plugged_in:
        gradient_level = 0
        if charging:
            # highlight_groups = ['battery_gradient_ac']
            highlight_groups = ['battery_ac_charging']
        else:
            # highlight_groups = ['battery_gradient_ac_charged']
            highlight_groups = ['battery_ac_not_charging']
        ret.append({
            'contents': '●',
            'highlight_groups': highlight_groups,
        })
    else:
        gradient_level = 100 - percent
    if warning:
        if warning.group(1) == 'Final':
            highlight_groups = ['warning:critical']
        else:
            highlight_groups = ['warning:regular']
    else:
        highlight_groups = ['battery_gradient']
    ret.append({
        'contents': fmt.format(value=percent),
        'highlight_groups': highlight_groups,
        'gradient_level': gradient_level
    })
    ret[0]['divider_highlight_group'] = 'background:divider'
    return ret
