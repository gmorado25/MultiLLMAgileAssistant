import threading
from typing import Any

""" -----------------------------------------------------------------------
Summary:
    ReturningThread implements a simple change the python's base thread
    class to allow for returning a result from the thread.join() method.
----------------------------------------------------------------------- """ 
class ReturningThread(threading.Thread):

    """ -----------------------------------------------------------------------
    Summary:
        Constructs a thread with an additional 'result' field for capturing
        the return value of the target.
    ----------------------------------------------------------------------- """ 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = None

    """ -----------------------------------------------------------------------
    Summary:
        Runs the target method on the given arguments and captures the 
        result.
    ----------------------------------------------------------------------- """ 
    def run(self):
        if self._target is None:
            return
        try:
            self.result = self._target(*self._args, **self._kwargs)
        except Exception as err:
            print(err)

    """ -----------------------------------------------------------------------
    Summary:
        Blocks and waits for the thread to finish, and returns the result
        once done.

    Returns:
        Returns the result from the target run inside the thread.
    ----------------------------------------------------------------------- """ 
    def join(self, *args, **kwargs) -> Any | None:
        super().join(*args, **kwargs)
        return self.result