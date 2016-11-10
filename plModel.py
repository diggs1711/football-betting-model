#imports 
import pandas as pd
import scipy.optimize as op
import numpy as np

class plModel(object):
	def __init__(self):
		#import csv
		self.fname = 'premierleague20132014.csv'
		self.df = pd.read_csv(self.name)
		print(self.df)
		#set index for teams
		self.df['HomeId'] = self.df.groupby(['HomeTeam']).grouper.group_info[0]
		self.df['AwayId'] = self.df.groupby(['AwayTeam']).grouper.group_info[0]
		#load data
		self.xTeam = self.df['HomeId'].tolist()
		self.yTeam = self.df['AwayId'].tolist()
		self.x = self.df['HG'].tolist()
		self.y = self.df['AG'].tolist()
		self.numberTeams = max(self.xTeam) + 1
		#set inital values for alpha and beta
		aplhas0 = [1 for i in range(self.numberTeams)]
		betas0 = [1 for i in range(self.numberTeams)]
		self.initial = (alphas0 + betas0)
		#add gamma
		self.inital.append(1)
	
	def minimize(self):
		nlnlikelihood = lambda *args: -self.lnlikelihood(*args)
		cons = ({'type':'eq', 'fun': lambda *args: self.norm_alphas(*args)})
		self.mresult = op.minimize(nlnlikelihood, self.initial, args=(self.x, self.y), constraints = cons)
		print(self.mresult)
	
	def norm_alphas(self, params):
		asum = 0
		for i in range(self.numberTeams):
			asum += params[i]
		return asum/self.numberTeams-1
		
	def lnlikelihood(self, params, x, y):
		lnsum = 0
		for i in range(len(self.x)):
			lambdaa = params[self.xTeam[i]]*params[self.numberTeams+selfyTeam[i]]*params[2*self.numberTeams]
			mu = params[self.yTeam[i]]*params[self.numberTeams+self.xTeam[i]]
			lnsum += (-lambdaa) + self.x[i] * np.log(lambdaa) + (-mu) + self.y[i] * np.log(mu)
		return lnsum
		
	

