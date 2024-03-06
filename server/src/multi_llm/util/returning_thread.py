import threading
from typing import Any, Optional

class ReturningThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result: Optional[Any] = None

    def run(self):
        if self._target is None:
            return
        try:
            self.result = self._target(*self._args, **self._kwargs)
        except Exception as err:
            print(err)

    def join(self, *args, **kwargs) -> Optional[Any]:
        super().join(*args, **kwargs)
        return self.result
