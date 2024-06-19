# tutorial #1

from metaflow import FlowSpec, step


class HellowWorldFlow(FlowSpec):

    @step
    def start(self):
        '''This is the starting point'''
        print("this is the first step")
        self.next(self.hello)

    @step
    def hello(self):
        '''Just saying hi'''
        print("Hello world")
        self.next(self.end)

    @step
    def end(self):
        '''Finish line'''
        print("this is the end step")


if __name__ == '__main__':
    HellowWorldFlow()
