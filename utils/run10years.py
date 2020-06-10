import os
import sys
import numpy as np
import time
from scipy.stats import kurtosis, skew
from random import sample
from pathlib import Path
from random import random

sys.path.append(os.getcwd())


from KATE.AlphaBasePure import *
from GAlpha import Transformer, Pipeline, Hybrid
from GAlpha.Transformer import Preprocess



class Alpha(Intraday):  
    def __init__(self, sim_start, sim_end, alphaNums, **kwargs):
        super().__init__(sim_start, sim_end, **kwargs)
        self.alphaNums = alphaNums
        self.description = ",".join(self.alphaNums) + "\n" + open(__file__).read()
        self.clean = Pipeline.Pipeline([Preprocess.fillna_with_time_series_mean,
                                        Preprocess.rank])
        self.childName = "[{}]x[{}]".format(*self.alphaNums)
        self.generation = "Gen_1"
        self.candidate = "Gen_1_valid"
        self.savePath = "./{}/{}".format(self.generation, self.childName)
        if not os.path.isdir(self.savePath):
            os.mkdir(self.savePath)
        
        
    def timeSeris(self):

        
        fac1, fac2 = [self.clean.execute(x) for x in self.baseValues]       
        df = Hybrid.NK_NK.sum(fac1, fac2)
        #print(fac1.shape, fac2.shape)
        

        
        df.to_pickle(self.savePath + "/{}.pkl".format(self.now))
        if len(self.history) < self.historySize:
            return 
        self.preSignal = df.mean(axis=1).loc[self.preSignal.index]
        
        
    def treatment(self):
        """
        self defined treatment
        """
        self.timeSeris()
        self.crossSection()
        
    
    def review(self):
        
        mostCorrelated = self.corrReport[:1]["corr"][0]
        top5Correlated = self.corrReport[:5]["corr"].mean()
        ir = self.simResult.loc["Avg.", "ir"] 
        bp = self.simResult.loc["Avg.","bp(hedged)"]
        return mostCorrelated, top5Correlated, ir, bp
        
if __name__ == "__main__":
    
    time.sleep(random())
    Y2 = [f for f in os.listdir("Gen_1_valid/years2") if f.endswith(".txt")]
    Y10 = [f for f in os.listdir("Gen_1_valid/years10") if f.endswith(".txt")]
    
    toSim = [f for f in Y2 if f not in Y10]

    if toSim:
        print("{} simulation to go...".format(len(toSim)))
        chosen = toSim[0]
        Path('Gen_1_valid/years10/{}'.format(chosen)).touch()
        
        
        
        with open("Gen_1_valid/years2/{}".format(chosen)) as f:
            parents = eval(f.readline().split(" (")[0])
        
        agent = Alpha("2010-01-05", "2020-05-30", parents, verbose = 1)
        agent.run()