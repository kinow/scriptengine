"""Time task for ScriptEngine, provides the current absolute time or elapsed
   time since a reference in the context.
"""

import datetime

from scriptengine.tasks.base import Task
from scriptengine.tasks.base.timing import timed_runner


class Time(Task):
    """Task class for measuring time in ScriptEngine
    """

    def __init__(self, parameters):
        super().__init__(__name__, parameters, required_parameters=['set'])

    @timed_runner
    def run(self, context):

        key = self.getarg("set", context)
        since = self.getarg("since", context, default=None)

        if since:
            self.log_info(f"Storing time delta in '{key}'")
        else:
            self.log_info(f"Storing datetime in '{key}'")

        now = datetime.datetime.now()

        if since:
            context[key] = now - since
        else:
            context[key] = now