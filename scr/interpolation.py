'''
    Data Interpolation

    >   Cara menentukan nilai yang berada di antara dua nilai diketahui
        berdasarkan suatu fungsi persamaan
'''

import os, sys
import pandas as pd

class Interpolation(object):
    
    def __init__(self, df, cols, dir_path):
        '''
        df
        >   Dataframe

        cols
        >   Nama column untuk interpolasi

        dir_path
        >   dir_path
        '''
        self.df = df
        self.cols = cols
        self.dir_path = dir_path

    def interpolate(self):
        
        for col in self.cols:
            df[col] = df[col].interpolate('spline', order=2)

        return df 

    def process(self):
        
        files = os.listdir(self.dir_path)
        for file_name in files:
            dataframe = pd.read_csv(os.path.join(self.dir_path, file_name))
            dataframe = interpolate(dataframe, ['high', 'open', 
                                                'low', 'close', 
                                                'volume'. 'adj_close'])
            print dataframe

            break



            
            


