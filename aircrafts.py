import numpy as np

# B-2 bomber
class B2():

	def __init__(self, *args):

		self.name = 'B-2'
		self.speed = 620
		self.ammo = MOP()

	def accelerate(self):
		vel = self.speed + np.random.normal(self.speed, 5)
		return vel

	def bombard(self):
		accuracy1 = np.random.uniform(0.92,1.0)
		accuracy2 = np.random.uniform(0.92,1.0)

		return accuracy1, accuracy2


# B-1 bomber
class B1():
	def __init__(self, *args):


		self.name = 'B-2'
		self.speed = 