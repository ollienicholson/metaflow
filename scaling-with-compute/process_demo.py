import os

from metaflow import FlowSpec, step

global_value = 5


class ProcessDemoFlow(FlowSpec):
    @step
    def start(self):
        global global_value
        global_value = 9
        print("Process ID is", os.getpid())
        print("global_value is", global_value)
        # global value is reassigned to 9
        self.next(self.end)

    @step
    def end(self):
        print("process ID is", os.getpid())
        print("global_value is", global_value)
        # global value is reset to 5


if __name__ == "__main__":
    ProcessDemoFlow()
