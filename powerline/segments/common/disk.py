# vim:fileencoding=utf-8:noet
"""Powerline disk segments."""
from __future__ import (
    unicode_literals, division, absolute_import, print_function)

import psutil


def format_number(number):
    """Format bytes into something human readable."""
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    for unit in units:
        if number < 1024:
            break
        number = number / 1024
    return '%.1f %s' % (number, unit)


def disk_free(pl):
    """Return the free disk space segment."""
    total, used, free, percent = psutil.disk_usage('/')
    contents = format_number(free)
    return [{
        'contents': contents,
        'highlight_groups': ['weather_temp_gradient'],
        'divider_highlight_group': 'background:divider',
        'gradient_level': percent
    }]
