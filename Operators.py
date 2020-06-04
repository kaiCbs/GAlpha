class Preprocess:
    
    def __init__(self):
        super().__init__() 
    
    @classmethod
    def rank(cls, df):
        return df.rank()
    
    @classmethod
    def fillna_with_historical_mean(cls, df):
        return df.fillna(df.mean())
    
    @classmethod
    def fillna_with_cross_section_mean(cls, df):
        return df.T.fillna(df.T.mean()).T
    
    
class Transform:
    ...
    

class Compress:
    ...


class Pipeline:
    def __init__(self, operators):
        self.operators = list(operators)
        
    def add_operators(self, op):
        self.operators.append(op)
    
    def execute(self, df):
        logs = ""
        for op in self.operators:
            df = op(df)
            logs += "{}\n".format(op.__name__)
        return df