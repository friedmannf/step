# noinspection SpellCheckingInspection
from collections import Callable

from before_after_wrapper import FuncManager

__author__ = "Felix Friedmann"
__copyright__ = "Copyright 2019"

from unittest import TestCase
from unittest.mock import patch

from step import step

DUMMY_FUNC_RESULT = 2


def _dummy_func():
    return DUMMY_FUNC_RESULT


_log_mem = []


class _DummyFuncManager(FuncManager):
    def __init__(self, func: Callable):
        """ Overridden FuncManager that logs to module-level variable for testing"""
        super().__init__(func, logger_function=_log_mem.append)


class TestStep(TestCase):
    @patch('before_after_wrapper.FuncManager', _DummyFuncManager)
    def test_step(self):
        # mock_class.func.set_return_value(1) #.func = 1
        step(_dummy_func)()
        self.assertTrue("start at" in _log_mem[0])
        self.assertTrue("stop  at" in _log_mem[1])
