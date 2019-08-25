# Step

Step is a small Python module that enables wrapping code around arbitrary Python functions, particularly for timing purposes.

The module consists of the following files (as of 25.08.2019):
  - before_after_wrapper.py: generic wrapper/decorator that allows to execute code before and after call a function 
  - step.py: wrapper/decorator derived from 'before_after_wrapper' that logs timing information before and after execution of the wrapped function
  - main.py: sample application demonstrating the timing wrapper
  - ... tests ...
  