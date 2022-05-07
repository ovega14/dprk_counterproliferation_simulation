import numpy as np

class AirStrike(loc):

	t = 1.5 # time limit for mission flight in hours
	dist = loc.dist # miles to target from FOB
	craft = B2()

	# travel to the city
	speed = craft.accelerate()
	accuracies = craft.bombard()

	# execute the attack
	def forward():

		# people killed
		fatalities = np.random.normal(0.2*pop, 0.05*pop)
		fatalities += max(0, margin-accuracies[0])*(pop-fatalities)
		fatalities += accuracies[1]*(pop-fatalities)

		mortality = fatalities/pop

		# destruction range
		destroyed = max(accuracies)

		# time taken
		telapsed = 2*dist/speed

		return mortality, destroyed, telapsed
	
	# survey the results
	def report(mortality, destroyed, telapsed):
		kills = mortality*pop
		hit = (destroyed >= 0.85)
		window = max((t-telapsed), 0)/t


		return kills, hit, window


class ForwardAssault():

	def __init__(self):
		xxx

	def engage():

		kills = []
		hits = []
		durations = []

		for target in targets:
			attack = AirStrike(target)

			kill, hit, duration = report(attack.forward())
			kills.append(kill)
			hits.append(hit)
			durations.append(duration)
		return kills, hits, durations

	def report():
		total_pop = 0
		num_targets = len(targets)

		for target in targets:
			total_pop += pop

		death_rate = np.sum(self.engage()[0])/total_pop
		hit_rate = np.sum(self.engage()[1])/num_targets
		time_rate = np.average(self.engage()[2])

		score = 0.4*(1-death_rate) + 0.5*(hit_rate) + 0.1*time_rate

		return score


def simulate_campaign(n):

	scores = []

	for _ in range(n):
		score = ForwardAssault().report()
		scores.append(score)

	return np.average(scores)

