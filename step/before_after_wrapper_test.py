# noinspection SpellCheckingInspection
__author__ = "Felix Friedmann"
__copyright__ = "Copyright 2019"

from typing import Dict, List, Tuple
from unittest import TestCase

from before_after_wrapper import before_after_wrapper, _stub_func, RESULT_LIT, FuncManager

DUMMY_FUNC_RESULT = 2
TEST = "test"
BEFORE = 1
AFTER = 3
BEFORE_AFTER_TARGET = (BEFORE, DUMMY_FUNC_RESULT, AFTER)


def _dummy_func():
    return DUMMY_FUNC_RESULT


def _test_before_func(func_manager: FuncManager, *args: List, **kwargs: Dict) -> \
        Tuple[FuncManager, Tuple, Dict]:
    """ 'before' function that introduces data into the FuncManager's memory """
    func_manager.mem[TEST] = [BEFORE]
    return func_manager, args, kwargs


def _test_after_func(func_manager: FuncManager, *args: List, **kwargs: Dict) -> \
        Tuple[FuncManager, Tuple, Dict]:
    """ 'after' function that introduces data into the FuncManager's memory """
    mem = func_manager.mem
    mem[TEST] += [mem[RESULT_LIT], AFTER]
    func_manager.mem = {RESULT_LIT: tuple(mem[TEST])}
    return func_manager, args, kwargs


# noinspection PyPep8Naming
class Test_before_after_wrapper(TestCase):
    """ test for 'before_after_wrapper' """
    def test_before_after_wrapper_simple(self):
        """ ensure that only the actual function's result is returned if 'before" and 'after' functions are stubbed """
        result = before_after_wrapper(_stub_func, _stub_func)(_dummy_func)()
        self.assertEqual(result, DUMMY_FUNC_RESULT)

    def test_before_after_wrapper_with_functions(self):
        """ ensure that 'before" and 'after' functions are called before and after actual function """
        result = before_after_wrapper(_test_before_func, _test_after_func)(_dummy_func)()
        self.assertEqual(result, BEFORE_AFTER_TARGET)

    def test_before_after_wrapper_with_functions_disabled(self):
        """ ensure that 'before" and 'after' functions are called before and after actual function """
        result = before_after_wrapper(_test_before_func, _test_after_func, False)(_dummy_func)()
        self.assertEqual(result, DUMMY_FUNC_RESULT)
