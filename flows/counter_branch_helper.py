from metaflow import FlowSpec, step

class CounterBranchHelperFlow(FlowSpec):
    
    @step
    def start(self):
        self.creature = "dog"
        self.count = 0
        self.next(self.add_one, self.add_two)
        
    @step
    def add_one(self):
        '''this is the first branch'''
        self.increment = 1
        self.count += self.increment
        self.next(self.join)
    
    @step
    def add_two(self):
        '''this is the second branch'''
        self.increment = 2
        self.count += self.increment
        self.next(self.join)
    
    @step
    def join(self, inputs):
        
        self.count = max(inp.count for inp in inputs)
        print("count from add_one: ", inputs.add_one.count)
        print("count from add_two: ", inputs.add_two.count)
        
        # if upstream artifacts are not required, we can exclude them when we join the two branches:
        self.merge_artifacts(inputs, exclude=['increment'])
        self.next(self.end)
        
    @step
    def end(self):
        print("The creature is: ", self.creature)
        print("The final count is: ", self.count)
        
if __name__ == '__main__':
    CounterBranchHelperFlow()
        