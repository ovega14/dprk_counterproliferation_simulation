import numpy as np

# weights generator for launch site attack attributes
def launch_weights():
	'''
	how important is each factor to the modeler?
	'''
	ats = ['fob distance', 'capacity', 'collateral', 'terrain']
	w = []
	for at in ats:
		wt = int(input("What weight will you assign to " + at: ))
		w.append(wt)
	return w


# weights generator for nuclear facility attack attributes
def nuclear_weights():
	'''
	how important is each factor to the modeler?
	'''
	ats = ['fob distance', 'research', 'collateral', 'terrain']
	w = []
	for at in ats:
		wt = int(input("What weight will you assign to " + at: ))
		w.append(wt)
	return w


# risk score calculator
def risk_score(w, x):
	'''
	Inputs: weights vector w, attribute score vector x
	Outputs: overall target priority score
	'''
	return np.dot(w,x)



