from argparse import Namespace
import sys

import pytest
import converter

def test_runs():
    args = converter.parse(['text.txt'])
    assert type(args) is Namespace

def test_version(capsys):
    with pytest.raises(SystemExit):
        converter.parse(['-v'])
    captured = capsys.readouterr()
    assert 'Converter v2.0' in captured.out