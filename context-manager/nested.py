# import contextlib
#
# @contextlib.contextmanager
# def next_test(name):
#    print("Entering", name)
#    yield name
#    print("Exiting", name)
#
#
# with next_test('outer') as nl, next_test('inner' + nl):
#    pass


import contextlib
import sys

class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return "You're in a with-block!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__: '
                  'normal exit detected')
        else:
            print('LoggingContextManager.__exit__: '
                  'Exception detected! '
                  'type={}, value={}, traceback={}'.format(
                      exc_type, exc_val, exc_tb))

@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield "You're in a with-block!"
        print('logging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exceptional exit',
              sys.exc_info())
        raise

LoggingContextManager()
logging_context_manager()

with LoggingContextManager as lm:
    print(lm)

