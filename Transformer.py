import pandas as pd
import numpy as np


class Preprocess:
    
    def __init__(self):
        super().__init__() 
    
    @classmethod
    def rank(cls, df):
        return df.rank()
    
    @classmethod
    def fillna_with_time_series_mean(cls, df):
        return df.fillna(df.mean())
    
    @classmethod
    def fillna_with_cross_section_mean(cls, df):
        return df.T.fillna(df.T.mean()).T
    
    @classmethod
    def normalize_on_time_series(cls, df):
        return (df - df.mean())/df.std()
    
    @classmethod
    def normalize_on_cross_section(cls, df):
        return ((df.T - df.T.mean())/df.T.std()).T


class NK2NK:
    def __init__(self):
        super().__init__() 
    
    @classmethod
    def rank(cls, df):
        return df.rank()
    
    @classmethod
    def logm1p(cls, df):
        return np.log1p(df - df.min().min())
    
    @classmethod
    def identical(cls, df):
        return df
    
class NK2N:
    def __init__(self):
        super().__init__() 
    
    @classmethod
    def mean(cls, df):
        return df.mean(axis=1)
    
    @classmethod
    def std(cls, df):
        return df.std(axis=1)
    
class N2NK:
    def __init__(self):
        super().__init__() 
    
    @classmethod
    def duplicate(cls, series, K=7):
        return pd.concat([series] * K, axis=1)
    
    @classmethod
    def linear_decay(cls, series, K=7):
        return pd.concat([series * (i+1)/K for i in range(K)] , axis=1)

class N2N:
    def __init__(self):
        super().__init__() 

    @classmethod
    def rank(cls, series):
        return series.rank()
    
    @classmethod
    def logm1p(cls, series):
        return np.log1p(series - series.min())
    
    @classmethod
    def identical(cls, series):
        return series