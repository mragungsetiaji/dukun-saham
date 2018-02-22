'''
    Data Normalization
'''
from sklearn import preprocessing

class Normalization(object):
    
    def __init__(self, dataframe, cols):
        
        self.dataframe = dataframe
        self.cols = cols

    def normalize(self):
        
        for col in self.cols:
            preprocessing.normalize(self.dataframe[col],
                                    norm='12',
                                    axis=1,
                                    copy=False)
        return self.dataframe


