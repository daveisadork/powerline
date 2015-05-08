# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

import os

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info


@requires_segment_info
class ReadOnlySegment(Segment):
	divider_highlight_group = None

	@staticmethod
	def get_directory(segment_info):
		return segment_info['getcwd']()

	def __call__(self, pl, segment_info):
		cwd = self.get_directory(segment_info)
		ret = []
		if not os.access(cwd, os.W_OK):
			ret.append({
				'contents': '',
				'highlight_groups': ['warning:regular'],
				'divider_highlight_group': None
			})
		return ret


read_only = with_docstring(ReadOnlySegment(),
'''Return the current VCS branch.

:param bool status_colors:
	Determines whether repository status will be used to determine highlighting.
	Default: False.
:param bool ignore_statuses:
	List of statuses which will not result in repo being marked as dirty. Most
	useful is setting this option to ``["U"]``: this will ignore repository
	which has just untracked files (i.e. repository with modified, deleted or
	removed files will be marked as dirty, while just untracked files will make
	segment show clean repository). Only applicable if ``status_colors`` option
	is True.

Highlight groups used: ``branch_clean``, ``branch_dirty``, ``branch``.
''')
