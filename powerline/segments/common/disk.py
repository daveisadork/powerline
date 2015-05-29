# vim:fileencoding=utf-8:noet
"""Powerline disk segments."""
from __future__ import (
    unicode_literals, division, absolute_import, print_function)

import psutil
from powerline.lib.humanize_bytes import humanize_bytes


def disk_free(pl):
    """Return the free disk space segment."""
    total, used, free, percent = psutil.disk_usage('/')
    contents = humanize_bytes(free, 'B')
    return [{
        'contents': contents,
        'highlight_groups': ['weather_temp_gradient'],
        'divider_highlight_group': 'background:divider',
        'gradient_level': percent
    }]
