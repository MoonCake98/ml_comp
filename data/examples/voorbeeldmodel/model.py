class YeOleDummy():
    """YeOleDummy - Ye Ole Teacher's dummy-classifier model"""
    
    
    def predict(self, datafile='competition_test.csv'):
        """labels = predict(self, datafile)
        Predicts labels for a new datafile with instances.
        parameters:
            datafile = csv-file filled with a header and instances
        returns:
            labels   = list of assigned labels
        """
        
        import pandas as pd, pickle, pkg_resources
        
        # Lees het model in
        modelfile = pkg_resources.resource_filename(__name__, 'model.pkl')
        with open(modelfile, 'rb') as filehandle:
            model = pickle.load(filehandle)
        
        # Lees de data in
        data = pd.read_csv(datafile)
        # Hier kan nog meer pre-processing komen...
        
        # Bepaal de voorspellingen
        X = data.iloc[:, :-1].to_numpy()
        predictions = model.predict(X)
        
        return predictions
    
if __name__=='__main__':
    model = YeOleDummy()
    print(model.predict(datafile='competition-test.csv').shape)