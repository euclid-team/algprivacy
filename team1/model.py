from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def get_model(seed):
    return RandomForestClassifier(max_depth=2, random_state=seed)