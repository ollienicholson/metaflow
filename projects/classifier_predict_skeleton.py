from metaflow import FlowSpec, step, Flow, Parameter, JSONType

class ClassifierPredictFlow(FlowSpec):
    
    vector = Parameter('vector', type=JSONType, required=True)
    
    @step
    def start(self):
        #  finds the latest training run using the Client API
        run = Flow('ClassifierTrainFlow').latest_run
        
        # saves the pathspec of the training run for lineage tracking
        self.train_run_id = run.pathspec
        
        # obtains the actual model object
        self.model = run['end'].task.data.model
        print("Input vector", self.vector)
        self.next(self.end)
        
    @step
    def end(self):
        print("Model", self.model)
        
if __name__ == '__main__':
    ClassifierPredictFlow()
