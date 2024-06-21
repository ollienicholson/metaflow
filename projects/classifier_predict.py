from metaflow import FlowSpec, step, Flow, Parameter, JSONType

class ClassifierPredictFlow(FlowSpec):
    
    vector = Parameter('vector', type=JSONType, required=True)
    
    @step
    def start(self):
        run = Flow('ClassifierTrainFlow').latest_run
        self.train_run_id = run.pathspec
        self.model = run['end'].task.data.model
        print("Input vector", self.vector)
        self.next(self.end)
        
    @step
    def end(self):
        print("Predicted class", self.model.predict([self.vector])[0])
        
if __name__ == '__main__':
    ClassifierPredictFlow()


# test vector for this exercise:
# '[14.3, 1.92, 2.72, 20.0, 120.0, 2.8, 3.14, 0.33, 1.97, 6.2, 1.07, 2.65, 1280.0]'

# run the following:
# python3 classifier_predict.py run --vector '[14.3, 1.92, 2.72, 20.0, 120.0, 2.8, 3.14, 0.33, 1.97, 6.2, 1.07, 2.65, 1280.0]'

# Output should be: 'Predicted class 0'