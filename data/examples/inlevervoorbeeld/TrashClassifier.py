import numpy as np
import pandas as pd

class TrashClassifier:
    """
    Trash (also known as unhelpful) Classifier

    This classifier is only meant for demonstration purposes. 

    Parameters
    ----------
    true_or_false : bool, default=False
    Whether to always return True of False, regardless of the properties of the observations.
    """

    def __init__(self, true_or_false=False):
        self.true_or_false = true_or_false

    def predict(self, filename='competition-test.csv'):
        """
        Creates the predictions 
        This method always returns a vector of all False or all True, dependent on
        the value of self.true_or_false.

        Parameters
        ----------
        filename : string, default='competition_test.csv'
            Location of the filename to be used in the prediction. 
            This can be either a relative of an absolute path.

        Returns
        -------
        y_pred: ndarray of shape (n_samples)
            Vector containing the class labels for each sample.
        """
        df = pd.read_csv(filename)
        X = df.to_numpy()
        m,n = X.shape
        return np.full( (m,), self.true_or_false)

    
if __name__ == '__main__':
    model = TrashClassifier(true_or_false=False)
    print (model.predict())
