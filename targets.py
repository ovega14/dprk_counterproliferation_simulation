import numpy as np

# missile launcher targets
hoejung_ni = {name: 'Hoejung-ni', margin: 0.95, pop: 1000, dist: 580}
tonghae = {name: 'Tonghae', margin: 0.94, pop: 5000, dist: 437}
sangnam_ni = {name: 'Sangnam_ni', margin: 0.98, pop: 1000, dist: 469}
sino_ri = {name: 'Sino-ri', margin: 0.96, pop: 5000, dist: 673}
sohae = {name: 'Sohae', margin: 0.94, pop: 5000, dist: 707}
yusang_ni = {name: 'Yusang_ni', margin: 0.93, pop: 10000, dist: 629}

targets = [hoejung_ni, tonghae, sangnam_ni, sino_ri, sohae, yusang_ni]

class Target(loc):

	def __init__(self, loc):
		self.name = loc[name]
		self.margin = loc[margin]
		self.pop = loc[pop]
		self.dist = loc[dist]
		#self.rigidity
