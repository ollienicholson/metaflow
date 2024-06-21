from metaflow import FlowSpec, step


class ClassifierTrainFlow(FlowSpec):

    @step
    def start(self):
        # no changes in the start step besides the updated self.next()
        from sklearn import datasets
        from sklearn.model_selection import train_test_split

        # loads the dataset
        # train_test_split splits the dataset into a test set (containing 20% of the rows) and a training set (with the rest of the data)
        X, y = datasets.load_wine(return_X_y=True)
        self.train_data, \
            self.test_data, \
            self.train_labels, \
            self.test_labels = train_test_split(X, y, test_size=0.2, random_state=0)
        print("Data loaded successfully")
        self.next(self.train_knn, self.train_svm) 

    # 3 new training steps are added below
    @step
    def train_knn(self):
        from sklearn.neighbors import KNeighborsClassifier
        
        self.model = KNeighborsClassifier()
        self.model.fit(self.train_data, self.train_labels)
        self.next(self.choose_model)
    
    @step
    def train_svm(self):
        from sklearn import svm
        
        
        self.model = svm.SVC(kernel='poly') # arg should be poly, not polynomial
        self.model.fit(self.train_data, self.train_labels)
        self.next(self.choose_model)
    
    @step
    def choose_model(self, inputs):
        def score(inp):
            return inp.model, \
                inp.model.score(inp.test_data, inp.test_labels)
        self.results = sorted(map(score, inputs), key=lambda x: -x[1])
        self.model = self.results[0][0]
        self.next(self.end)    
    
    
    @step
    def end(self):
        # the end step is modified to print out information about the models
        print("Scores:")
        print('\n'.join('%s %f' % res for res in self.results))


if __name__ == '__main__':
    ClassifierTrainFlow()

# test vector for this exercise:
# '[14.3, 1.92, 2.72, 20.0, 120.0, 2.8, 3.14, 0.33, 1.97, 6.2, 1.07, 2.65, 1280.0]'

# run the following:
# python3 classifier_predict.py run --vector '[14.3, 1.92, 2.72, 20.0, 120.0, 2.8, 3.14, 0.33, 1.97, 6.2, 1.07, 2.65, 1280.0]'

# Output should be: 'Predicted class 0'