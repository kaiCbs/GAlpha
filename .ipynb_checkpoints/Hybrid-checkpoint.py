class N_N:
    def __init__(self):
        super().__init__() 
    
    @classmethod
    def prod(cls, fac1, fac2):
        return fac1 * fac2
    
    @classmethod
    def sum(cls, fac1, fac2):
        return fac1 + fac2
    

    
class NK_N:
    def __init__(self):
        super().__init__() 
        
    @classmethod
    def sum(cls, df, series):
        if not isinstance(series, pd.Series):
            df, series = series, df
        
        return (df.T + series).T

    
class NK_NK:
    def __init__(self):
        super().__init__() 
    
    @classmethod
    def prod(cls, df1, df2):
        return df1 * df2
    
    @classmethod
    def sum(cls, df1, df2):
        return df1 + df2