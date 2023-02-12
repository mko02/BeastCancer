import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import scipy.stats as stats
import distribution as dist

#df is the dataframe that we compare to
def createGraph(df): 
    moneyY = pd.read_csv("CSV/health_spending.csv")
    fiscal2020 = moneyY[moneyY["TIME"] == "2020"]
    genStats = df[]
    for row in stats2020.iterrows:
        

