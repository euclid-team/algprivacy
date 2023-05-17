from sklearn.svm import SVC

def get_model(seed):
    return SVC(probability=True)