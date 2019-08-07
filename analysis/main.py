import pandas as pd
import numpy as np
import datetime
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class Baseball_Analytics:
    def __init__(self):
        df = pd.read_csv('../core/people.csv', usecols = ['playerID', 'nameFirst', 'nameLast', 'finalGame'])
        df = df.astype({"playerID": str, "nameFirst": str, "nameLast": str, "finalGame": str})
        df = df[df['finalGame'].str.contains("2019")]
        playerID = df['playerID']
        df2 = pd.read_csv('../core/batting.csv', usecols=['playerID', 'yearID', 'AB', 'R', 'H', "2B", '3B', 'HR', 'RBI', 'SO', 'BB', 'HBP', 'SF'])
        df2 = df2[df2['playerID'].isin(playerID)]
        df2['OBP'] = (df2['H'] + df2['BB'] + df2['HBP']) / (df2['AB'] + df2['BB'] + df2['HBP'] + df2['SF'])
        df2['SLG'] = (df2['H'] + df2['2B'] + (2 * df2['3B']) + (3 * df2['HR'])) / df2['AB']
        df3 = pd.read_csv('../core/fielding.csv', usecols=['playerID', 'yearID', 'POS', 'PO', 'A', 'E', 'DP', 'PB', 'SB', 'CS'])
        df3 = df3[df3['playerID'].isin(playerID)]
        self.fielding = df3 
        self.batting = df2
        self.players = df
        
    def project_batting_value(self, playerID=None):        
        playerStats = None
        if playerID != None:
            playerStats = self.batting.loc[self.batting['playerID'] == playerID]
        else:
            playerStats = self.batting
        accessedPlayers = []
        for index, row in playerStats.iterrows():
            if row['playerID'] not in accessedPlayers:
                accessedPlayers.append(row['playerID'])
                currentPlayer = self.batting.loc[self.batting['playerID'] == row['playerID']]
                y = currentPlayer['SLG']
                x = currentPlayer['yearID']
                plt.plot(x, y)                    
        plt.show()

        

if __name__ == '__main__':
    analysis = Baseball_Analytics()
    analysis.project_batting_value()
    