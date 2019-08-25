# noinspection SpellCheckingInspection
__author__ = "Felix Friedmann"
__copyright__ = "Copyright 2019"

import datetime
from typing import List, Dict, Tuple

from before_after_wrapper import before_after_wrapper, FuncManager

LIT_START_TIME = 'start_time'
LIT_ITERATION = 'iteration'


def start(func_manager: FuncManager, *args: List, **kwargs: Dict) -> \
        Tuple[FuncManager, Tuple, Dict]:
    """ Print time BEFORE function call """

    time = datetime.datetime.now()
    func_manager.mem[LIT_START_TIME] = time
    if LIT_ITERATION not in func_manager.static_mem:
        func_manager.static_mem[LIT_ITERATION] = 0
    func_manager.static_mem[LIT_ITERATION] += 1
    func_manager.logger_function("%i) %s: start at %s" % (
        func_manager.static_mem[LIT_ITERATION], str(func_manager.func), time))
    return func_manager, args, kwargs


def stop(func_manager: FuncManager, *args: List, **kwargs: Dict) -> \
        Tuple[FuncManager, Tuple, Dict]:
    """ Print time AFTER function call """

    time = datetime.datetime.now()
    start_time = func_manager.mem[LIT_START_TIME]
    dif = time - start_time
    func_manager.logger_function("%i) %s: stop  at %s; %s elapsed" %
                                 (func_manager.static_mem[LIT_ITERATION], str(func_manager.func), time, dif))
    return func_manager, args, kwargs


# step wraps functions with time measurement logs
step = before_after_wrapper(start, stop)
