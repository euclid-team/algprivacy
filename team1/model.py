from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

def get_model(seed, name='forest'):
    if name == 'forest':
        return RandomForestClassifier(max_depth=2, random_state=seed)
    elif name == 'logreg':
        return LogisticRegression(solver="lbfgs",  random_state=seed)
    elif name == 'knn':
        return KNeighborsClassifier(n_neighbors=3)