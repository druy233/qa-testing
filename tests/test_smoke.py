"""环境自检：确认 pytest / requests 可用。"""

import sys


def test_python_version():
    assert sys.version_info >= (3, 10), f"当前 Python {sys.version}"


def test_requests_import():
    import requests
    assert requests.__version__


def test_basic_math():
    # 一个必然通过的用例，用来确认 pytest 能跑
    assert sum([1, 2, 3]) == 6
