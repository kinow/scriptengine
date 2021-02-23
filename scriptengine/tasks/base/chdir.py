"""Chdir task for ScriptEngine."""

import os

from scriptengine.tasks import Task
from scriptengine.tasks.timing import timed_runner


class Chdir(Task):
    """Chdir task, changes the current working directory
    """
    _required_arguments = ('path', )

    def __init__(self, arguments):
        Chdir.check_arguments(arguments)
        super().__init__(arguments)

    @timed_runner
    def run(self, context):
        path = self.getarg('path', context)
        self.log_info(f"Change path to {path}")
        os.chdir(path)
