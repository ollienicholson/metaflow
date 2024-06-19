from metaflow import FlowSpec, step

class CounterBranchFlow(FlowSpec):
    
    @step
    def start(self):
        self.creature = "dog"
        self.count = 0
        self.next(self.add_one, self.add_two)
        
    @step
    def add_one(self):
        '''first branch'''

        self.count +=1
        self.next(self.join)
    
    @step
    def add_two(self):
        '''second branch'''
        self.count+= 2
        self.cat = "cat"
        self.next(self.join)
    
    @step
    def join(self, inputs):
        
        self.count = max(inp.count for inp in inputs)
        print("count from add_one: ", inputs.add_one.count)
        print("count from add_two: ", inputs.add_two.count)
        
        self.creature = inputs[0].creature
        # accessing a different branch by index e.g. add_two by reassigning variable in join to inputs[1].variable
        self.cat = inputs[1].cat
        self.next(self.end)
        
    @step
    def end(self):
        print("The creature is: ", self.creature)
        print("The max count is: ", self.count)
        print("The animal is a: ", self.cat)
        
if __name__ == '__main__':
    CounterBranchFlow()
        