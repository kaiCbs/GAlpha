import inspect

class Pipeline:
    def __init__(self, operators = list(), numOperand = 1, verbose = 0):
        self.operators = list(operators)
        self.numOperand = numOperand
        self.verbose = verbose
        if self.operators:
            self.validate()
            

    
    def validate(self):
        logs, nStep = "Valid pipeline, steps: \n\n", 0 
        for op in self.operators:
            logs += "{:2}: {}\n".format(nStep:=nStep+1,op.__name__.replace("_"," "))
            if len(inspect.signature(op).parameters) != self.numOperand:
                raise TypeError("[Error] {}.{} operates on {} object(s) but {} were expected.".
                                format(op.__self__.__name__,
                                       op.__name__,
                                       3-self.numOperand, 
                                       self.numOperand))
        if self.verbose:
            print(logs)
    
    def add_operators(self, op):
        if isinstance(op, list):
            self.operators.extend(op)
        else:
            self.operators.append(op)
        self.validate()
        
        
    def execute(self, df):
        if self.numOperand == 1:
            for op in self.operators:
                df = op(df)
            return df
        else:
            for op in self.operators:
                df = op(df)
            return df