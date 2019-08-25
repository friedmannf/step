# noinspection SpellCheckingInspection
__author__ = "Felix Friedmann"
__copyright__ = "Copyright 2019"

from unittest import TestCase
from unittest.mock import patch

from step import step

DUMMY_FUNC_RESULT = 2


def _dummy_func():
    return DUMMY_FUNC_RESULT


class TestStep(TestCase):
    @patch('before_after_wrapper.FuncManager')
    def test_step(self, mock_class):
        step(_dummy_func)()
        start_statements = 0
        stop_statements = 0
        for call in mock_class.mock_calls:
            if "start at" in str(call):
                start_statements += 1
            if "stop  at" in str(call):
                stop_statements += 1
        self.assertTrue(start_statements == 1 and stop_statements == 1)
