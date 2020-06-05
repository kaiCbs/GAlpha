class Pipeline:
    def __init__(self, operators, opType = 1):
        self.operators = list(operators)
        if opType:
            self.numOperand = 1
            self.Operand = "fac" + str(opType)
        else:
            self.numOperand = 2
            self.Operand = ["fac1","fac2"]
            
        for op in self.operators:
            if len(inspect.signature(op).parameters) != self.numOperand:
                raise TypeError("[Error] {}.{} operates on {} object(s) but {} were expected.".
                                format(op.__self__.__name__,
                                       op.__name__,
                                       3-self.numOperand, 
                                       self.numOperand))
            
    def add_operators(self, op):
        self.operators.append(op)
    
    def execute(self, df):
        logs, nStep = "Steps: \n\n", 0 
        for op in self.operators:
            df = op(df)
            print(df.__name__)
            logs += "{:2}: {}\n".format(nStep:=nStep+1,op.__name__.replace("_"," "))
        print(logs)
        return df