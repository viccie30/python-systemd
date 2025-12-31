# SPDX-License-Identifier: LGPL-2.1-or-later

from systemd._reader import _Reader

import pytest

def test_reader_init_with_empty_files_sequence():
    _Reader(files=[], flags=0)
