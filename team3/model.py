from sklearn.svm import SVC

class MyModel:
    def __init__(self, seed):
        self.model = SVC(probability=True)

    def train(self, X, y):
        self.model.fit(X, y)

    def test(self, X, y):
        return self.model.score(X, y)
    
    def predict_proba(self, X):
        return self.model.predict_proba(X)
