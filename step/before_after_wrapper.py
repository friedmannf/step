# noinspection SpellCheckingInspection
__author__ = "Felix Friedmann"
__copyright__ = "Copyright 2019"

from collections import Callable
from typing import Tuple, Dict, List

_IS_ACTIVE = True  # this parameter will disable the 'before' and 'after' functions
RESULT_LIT = 'result'


def _logger_print(string: str):
    """ Use standard print for logging a string"""
    print(string)


class FuncManager:
    def __init__(self, func: Callable, logger_function: Callable = _logger_print):
        """ Holds function related data """
        self.func = func
        self.mem = dict()
        self.logger_function = logger_function


def _stub_func(func_manager: FuncManager, *args: List, **kwargs: Dict) -> \
        Tuple[FuncManager, Tuple, Dict]:
    """ Stub function for before_after_wrapper that does nothing."""
    return func_manager, args, kwargs


def before_after_wrapper(before: Callable = _stub_func, after: Callable = _stub_func, active: bool = _IS_ACTIVE) \
        -> Callable:
    """ Decorator that calls functions before and after calling the wrapper function."""

    def wrapped_func(func: Callable):
        # actual decorator
        def call_func(*args: Tuple, **kwargs: Dict):
            # Call 'before' function, wrapped function and finally 'after' function
            fn = func
            func_manager = FuncManager(func)
            if active:
                func_manager, args, kwargs = before(func_manager, *args, **kwargs)
            result = fn(*args, **kwargs)
            func_manager.mem[RESULT_LIT] = result
            if active:
                func_manager, _, _ = after(func_manager, *args, **kwargs)
            result = func_manager.mem[RESULT_LIT]
            return result

        return call_func

    return wrapped_func
